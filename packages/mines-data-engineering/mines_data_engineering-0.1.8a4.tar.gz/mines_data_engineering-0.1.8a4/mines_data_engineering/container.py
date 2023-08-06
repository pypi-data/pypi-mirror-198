import os
from pickle import GLOBAL
import time
import logging
import shutil
import threading
import tempfile
from pathlib import Path
from typing import Tuple
try:
    from spython.main import get_client
    from spython.utils import check_install
    USE_DOCKER = False
    client = get_client(quiet=True)
    if not check_install():
        raise ImportError("Singularity not available")
except ImportError:
    from docker import from_env
    import docker
    USE_DOCKER = True
    client = from_env()


_SINGULARITY_MONGO_IMAGE = "/sw/apps/singularity-images/mines_data_engineering/mongo.sif"
_SINGULARITY_TIMESCALE_IMAGE =  "/sw/apps/singularity-images/mines_data_engineering/timescaledb-pg14.sif"

_TIMESCALE_INSTANCE = f"data-engineering-timescaledb-{os.getenv('USER')}"

#logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

DBDIR: Path = Path(os.getenv("HOME")) / "scratch/tmp"
PG_DBDIR: Path = Path(os.getenv("HOME")) / "scratch/tmp/postgres"
shutil.rmtree(PG_DBDIR, ignore_errors=True)
os.makedirs(PG_DBDIR)

    
class Service:
    singularity_container: str
    docker_container: Tuple[str, str]

    @classmethod
    def pull(cls, singularity_filename: str):
        if USE_DOCKER:
            #logging.info(f"Pulling contaner: {cls.docker_container}")
            client.images.pull(cls.docker_container[0], tag=cls.docker_container[1])
        elif not os.path.exists(singularity_filename):
            #logging.info(f"Pulling contaner: {cls.singularity_container}")
            client.pull(image=cls.singularity_container)
        else:
            pass
            #logging.info(f"Using existing image: {singularity_filename}")

    @classmethod
    def run(cls):
        raise NotImplementedError

    @classmethod
    def stop(cls, instance):
        if USE_DOCKER:
            pass
        else:
            client.instance.Instance.stop(f"instance://{instance.name}")


class MongoDB(Service):
    singularity_container = "docker://mongo:latest"
    docker_container = ("mongo", "latest")

    @classmethod
    def run(cls, image_file: str = _SINGULARITY_MONGO_IMAGE):
        if USE_DOCKER:
            cls.pull(image_file)
            try:
                con = client.containers.get("data-engineering-mongodb")
                con.remove(force=True)
                raise docker.errors.NotFound("")
            except docker.errors.NotFound:
                return client.containers.run(':'.join(cls.docker_container), ports= {'27017/tcp':27017}, detach=True, auto_remove=False, name="data-engineering-mongodb")
        else:
            inst = client.instance.instance(image=image_file, options=[f"-B {DBDIR}:/data/db", f"-B {DBDIR}:/tmp"], name='data-engineering-mongodb')
            def _run_mongo():
                client.execute(image=f"instance://{inst.name}", command=["mongod"])
            t = threading.Thread(target=_run_mongo)
            t.start()
            return inst

    @classmethod
    def ready(cls) -> bool:
        if USE_DOCKER:
            time.sleep(30)
            return True
        loc = f"{DBDIR}/mongodb-27017.sock"
        return os.path.exists(loc)

    @classmethod
    def wait_until_ready(cls):
        while not cls.ready():
            time.sleep(2)

    @classmethod
    def conn_string(cls):
        if USE_DOCKER:
            return None
        else:
            return "mongodb://" + f"{DBDIR}/mongodb-27017.sock".replace('/', '%2F')


class TimescaleDB(Service):
    singularity_container = "docker://timescale/timescaledb:latest-pg14"
    docker_container = ("timescale/timescaledb", "latest-pg14")

    @classmethod
    def run(cls, image_file: str = _SINGULARITY_TIMESCALE_IMAGE):
        if USE_DOCKER:
            cls.pull(image_file)
            try:
                con = client.containers.get(_TIMESCALE_INSTANCE)
                con.remove(force=True)
                raise docker.errors.NotFound("")
            except docker.errors.NotFound:
                return client.containers.run(':'.join(cls.docker_container), environment={"POSTGRES_PASSWORD": "password"}, ports= {'5432/tcp':5432}, detach=True, auto_remove=False, name=_TIMESCALE_INSTANCE)
        else:
            os.environ["POSTGRES_PASSWORD"] = "password"
            inst = client.instance.instance(image=image_file, options=[f"-B {PG_DBDIR}:/var/lib/postgresql/data", f"-B {PG_DBDIR}:/var/run/postgresql", f"--env=POSTGRES_PASSWORD"], name=_TIMESCALE_INSTANCE)
            def _run_timescale():
                client.execute(image=f"instance://{inst.name}", command=["/usr/local/bin/docker-entrypoint.sh", "postgres", "-c", "listen_addresses=''"])
            t = threading.Thread(target=_run_timescale)
            t.start()
            return inst

    @classmethod
    def ready(cls) -> bool:
        if USE_DOCKER:
            time.sleep(30)
            return True
        loc = PG_DBDIR / '.s.PGSQL.5432'
        return os.path.exists(loc)

    @classmethod
    def wait_until_ready(cls):
        while not cls.ready():
            time.sleep(2)

    @classmethod
    def conn_string(cls):
        if USE_DOCKER:
            return "user=postgres password=password host=localhost port=5432"
        else:
            return f"user=postgres password=password host={PG_DBDIR}"

    @classmethod
    def sqlmagic(cls):
        if USE_DOCKER:
            return "postgresql:///postgres?user=postgres&password=password&host=localhost&port=5432"
        else:
            return f"postgresql:///postgres?user=postgres&password=password&host={PG_DBDIR}"
