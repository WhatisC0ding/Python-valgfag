import logging
#from importlib import reload
#reload(logging)

#Gemmer logging i en ny fil som hedder mylog.log
logging.basicConfig(filename='mylog.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.debug('My debugging message')

myvar = 42

logging.warning('My warning. myvar is %d', myvar)

#Importere det selvlavede modul mymodule.py
import 12.1 mymodule


logger = logging.getLogger('myLogger')

myvar = 42

logger.warning('My warning. myvar is %d', myvar)
logger.debug('My debugging message')

mymodule.myFunc()




