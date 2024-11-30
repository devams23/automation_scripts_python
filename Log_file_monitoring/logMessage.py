import logging
import time

# Create and configure logger
logging.basicConfig(
    filename="newfile.log",
    format="%(asctime)s %(levelname)s %(message)s",
    filemode="w",
    level=logging.DEBUG,
)

# Creating an object
logger = logging.getLogger('its_good')

data_list = [12, 0, 9, 13, 1, 34, 9, 1, 0, 2, 0, 3]

for i in range(len(data_list)):
    try: 
        0 / data_list[i]
    except ZeroDivisionError:
        logger.error("Did you try to divide  by zero?")  # Ensure the log is written immediately
        time.sleep(4)
