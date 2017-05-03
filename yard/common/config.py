#! /usr/bin/env python
#coding=utf-8

import os
import ConfigParser

cfg_dir = os.path.expanduser('/tmp/cfg')

def get_cfg_dir():
    if not os.path.exists(cfg_dir):
        os.mkdir(cfg_dir)
    return cfg_dir

def get_cfg_path():
    return os.path.join(get_cfg_dir(), 'config.ini')    


def load_config():
    cf = get_cfg_path()
    if not os.path.exists(cf):
        f = open(cf, 'w')
        f.close()    

    config = ConfigParser.ConfigParser()
    config.read(cf)
    return config

def write():
    config=load_config()
    config.add_section("foo")
    config.set("foo",'option2','value2')
    config.write(open(get_cfg_path(),"w"))

def read():
    config=load_config()
    secs=config.sections()
    print ">>sections - "
    print secs
    print ">>options -"
    for x in secs:
        print x," ",config.options(x)
        for y in config.options(x):
            print y,"=",config.get(x,y)

if __name__ == "__main__":
    read()
    # write()
