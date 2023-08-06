import logging
import time
from mines_data_engineering.container import MongoDB, TimescaleDB, USE_DOCKER, _SINGULARITY_MONGO_IMAGE, _SINGULARITY_TIMESCALE_IMAGE

#logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

_mongo_instance = None
_pg_instance = None


def init():
    """
    Handles setup for the environment
    """
    if not USE_DOCKER:
        from spython.logger import bot
        bot.level = -4 # CRITICAL
    #logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)

def start_mongo(image_file: str = _SINGULARITY_MONGO_IMAGE):
    """
    Starts MongoDB and returns the connection string
    """
    global _mongo_instance
    if _mongo_instance is not None:
        #logging.info("MongoDB is already running!")
        return MongoDB.conn_string()
    #logging.info("Starting MongoDB")
    _mongo_instance = MongoDB.run(image_file)
    #logging.info("Sleeping for 2 seconds to let MongoDB start")
    MongoDB.wait_until_ready()
    return MongoDB.conn_string()


def stop_mongo():
    global _mongo_instance
    if _mongo_instance is None:
        _mongo_instance = MongoDB.run(_SINGULARITY_MONGO_IMAGE)
    _mongo_instance.stop()
    _mongo_instance = None


def start_postgres(connstring='connstring'):
    """
    Starts Postgres w/ TimescaleDB extension and returns the connection string
    """
    #logging.info("Starting Postgres")
    TimescaleDB.run(_SINGULARITY_TIMESCALE_IMAGE)
    #logging.info("Waiting until Postgres is running...")
    TimescaleDB.wait_until_ready()
    if connstring == 'connstring':
        return TimescaleDB.conn_string()
    elif connstring == 'sqlmagic':
        return TimescaleDB.sqlmagic()
    else: # default
        return TimescaleDB.conn_string()

def stop_postgres():
    global _pg_instance
    if _pg_instance is None:
        _pg_instance = TimescaleDB.run(_SINGULARITY_TIMESCALE_IMAGE)
    _pg_instance.stop()
    _pg_instance = None
