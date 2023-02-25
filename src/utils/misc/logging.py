import logging.handlers

from src.data import config

logger = logging.getLogger(__name__)

file_handler = logging.handlers.RotatingFileHandler(
    filename=config.LOG_PATH + 'admin_logs.log',
    maxBytes=config.LOG_SIZE,
    backupCount=config.N_LOGS,
    encoding=config.ENCODING
)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
