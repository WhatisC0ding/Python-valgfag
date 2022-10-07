import logging

#Bruges i 12.1 Logging.py

def myFunc():
    logger = logging.getLogger('myLogger')
    logger.warning('My warning (mymodule)')
    logger.debug ('My debugging message (mymodule)')