#!   /usr/bin/python
#    coding:utf-8
#	 @file    a.py
#	 @author  Sean(jiangshaoyin@pku.edu.cn)
#	 @date    2018-11-01 12:53:42
 
 
import tensorflow as tf
import numpy as np

import os
print (os.path.abspath('.'))
print (os.path.relpath('/usr','.'))
print ('~/Python_Project'.split(os.path.sep))
print ('/usr/include/spawn.h'.split(os.path.sep))
print (os.listdir('.'))
print (os.path.getsize('.'))
