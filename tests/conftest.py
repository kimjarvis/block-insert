# conftest.py
import logging

def pytest_configure():
    logging.basicConfig(
        level=logging.DEBUG,
        filename="pytest_logs.log",  # Log file name
        filemode="a",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )