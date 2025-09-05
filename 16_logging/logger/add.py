from logger import logging

# log messages  with different severity  levels
def add(a, b):
    logging.info("add function performed")
    return a + b

logging.debug("The addition function is called")
result = add(5, 3)
logging.info(f"The result of addition is {result}")