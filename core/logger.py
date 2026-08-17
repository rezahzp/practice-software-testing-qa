import logging
import sys

def get_logger(name: str) -> logging.Logger:
    """
    Configures and returns a custom logger.
    Outputs to standard out so Pytest captures it in HTML reports.
    """
    logger = logging.getLogger(name)
    
    # Only configure the logger if it hasn't been configured yet
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            fmt='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger