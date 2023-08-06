"""This script sets up logger."""

import logging
# import os
# import sys
# from pathlib import Path

# try:
#     data = Path(os.environ["XDG_DATA_HOME"]).absolute() / "image_dl"
# except KeyError:
#     data = Path(os.environ["HOME"]).absolute() / ".local" / "share" / "image_dl"

# data.mkdir(parents=True, exist_ok=True)

# logger = logging.getLogger(__package__)
# logger.setLevel(logging.DEBUG)

# file_formatter = logging.Formatter(
#     "%(asctime)s - %(pathname)s[line:%(lineno)d] - %(funcName)s - %(levelname)s: %(message)s",
#     datefmt="%H:%M:%S",
# )
# file_handler = logging.FileHandler(str(data / "image_dl.log"))
# file_handler.setLevel(logging.ERROR)
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)

# stream_formatter = logging.Formatter(
#     fmt="%(asctime)s %(levelname)s %(filename)s[%(lineno)d] %(message)s", 
#     datefmt="%Y-%m-%d %H:%M:%S")
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.DEBUG)
# stream_handler.setFormatter(stream_formatter)
# logger.addHandler(stream_handler)

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(filename)s[%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

logger = logging.getLogger(__package__)
