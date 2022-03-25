import logging

__version__ = "0.1.0"

logging.basicConfig(format="%(asctime)s %(levelname)s:%(name)s: %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel('INFO')
logger.info("Version %s", __version__)
