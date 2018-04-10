# -*- coding: utf-8 -*-
from sys import stdout
import logging
# from tempfile import gettempdir
# tmp = gettempdir()
def config_log():
    # file_handler = logging.FileHandler(filename=tmp+'\\tmp.log')
    stdout_handler = logging.StreamHandler(stdout)
    handlers = [stdout_handler]
    logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=handlers)
    logger = logging.getLogger('process_cartolaFC')
    return logger