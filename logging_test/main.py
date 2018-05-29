from config import logger
try:
    a = 1/0
except Exception as e:
    logger.error("test")
    print(str(e))
