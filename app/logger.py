import logging

# Define a logger
logger = logging.getLogger('offramp_logger') # Create a named logger
logger.setLevel(logging.INFO) # Set the global logging level

# Prevent the logger from propagating to the root logger
logger.propagate = False

# Create a file handler if the logger doesn't have one
if not logger.handlers:
    # Create a file handler
    file_handler = logging.FileHandler('offramp_api.log') # Logs to 'offramp_api.log'
    file_handler.setLevel(logging.INFO) # Set the file handler's level

    # Create a console handler
    console_handler = logging.StreamHandler() # Logs to the console
    console_handler.setLevel(logging.INFO) # Set the console handler's level

    # Define a common log format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter) # Apply the formatter to the file handler
    console_handler.setFormatter(formatter) # Apply the formatter to the console handler

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)