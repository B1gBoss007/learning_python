#!/usr/bin/python

import logging


formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
def setup_logger(name, log_file, level=logging.WARNING):
    """Function setup as many loggers as you want"""
    #creat file handler
    handler = logging.FileHandler(log_file,'w')
    #creat formatter and add it to the handlers
    handler.setFormatter(formatter)
    #creat a logger
    logger = logging.getLogger(name)
    #set level
    logger.setLevel(level)
    #add handlers
    logger.addHandler(handler)

    return logger

if __name__ == "__main__":
    t1 = setup_logger('t1','1.log')
    t1.info('info')
    t1.warning('warning')
    t1.debug('debug')
    t1.info('info')
    t2 = setup_logger('t2','2.log')
    t2.critical('test two')
    try:
        open('/no/such/file','rb')
    except(SystemExit,KeyboardInterrupt):
       raise
    except Exception,e:
        t1.error('Failed to open file',exc_info=True)
        t2.critical('Failed to open file',exc_info=True)
