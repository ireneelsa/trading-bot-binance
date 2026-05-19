import logging
from pathlib import Path

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    
    # Prevent adding handlers multiple times if logger is requested again
    if logger.hasHandlers():
        return logger

    # Set the base logger to DEBUG so it captures all levels
    logger.setLevel(logging.DEBUG)

    # Define the required log format
    formatter = logging.Formatter(
        fmt="[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # --- Console Handler ---
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # --- File Handler ---
    # Determine the absolute path to the project root (one level up from this file)
    project_root = Path(__file__).parent.parent
    log_file_path = project_root / "bot.log"
    
    # Create the file handler (append mode 'a' is default, but explicit is better)
    file_handler = logging.FileHandler(log_file_path, mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
