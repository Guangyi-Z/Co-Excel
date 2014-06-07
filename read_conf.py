#!/usr/bin/python
#-*- coding: utf-8 -*-

import os

def read_config(key):
    '''
        read configuration "key=value" from 'config/config.txt' file
    '''
    res= None
    fname_conf='.' + os.path.sep + 'config' + os.path.sep + 'config.txt'
    fconf= file(fname_conf)
    for line in fconf:
        if line.startswith(key):
            line= line.rstrip() # remove the new line char
            res= line[len(key)+1:]
    fconf.close()
    return res