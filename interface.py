#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is the interface for the SHA0 executable/dll call.
"""
__author__ = 'David Celný'
__version__ = '0.0.1'

# Built-in/Generic Imports
import os
import subprocess
# […]
import time
import numpy as np
# Libs
from ctypes import *

# Own modules

SHA0HashSize = 20
get_hash = None

def init_lib(lib_name:str = 'sha0.so'):
	global get_hash
	sha0 = cdll.LoadLibrary(os.path.realpath(lib_name))
	get_hash = sha0.get_hash
	get_hash.argtypes = [POINTER(c_uint8), c_uint, POINTER(c_uint8)]

def get_hash_subprocess(message:str) -> str:
	""" obtain the hash from subprocess call to exe, 1iteration ~ 3.5e-3 s"""
	sub = subprocess.Popen([f"./sha0 {message}"], shell=True, stdout=subprocess.PIPE)
	res, _ = sub.communicate()
	return res.decode("utf-8")
	# return res

def get_hash_dll(message:str) -> str:
	""" obtain the hash from call to dynamic library, 1iteration ~ 4e-5 s"""
	c_mess = np.asarray(tuple(message.encode()), dtype=c_uint8)
	hash_list = np.asarray([0]*SHA0HashSize, dtype=c_uint8)
	get_hash(c_mess.ctypes.data_as(POINTER(c_uint8)), len(message), hash_list.ctypes.data_as(POINTER(c_uint8)))				
	return "".join(["{:x}".format(l) for l in hash_list])

if __name__ == "__main__":
	init_lib()
	
	message = "test"
	numiter = 10

	start = time.time()
	for i in range(numiter):
		h = get_hash_dll(message)
		# print(message, ">", h)	
	end = time.time()
	dll_call = end - start
	
	start = time.time()
	for i in range(numiter):
		h = get_hash_subprocess(message)
		# print(message, ">", h)
	end = time.time()
	sub_call = end - start
	
	print(f"DLL    call: total= {dll_call:16.10f}[s], 1 iteration= {dll_call/numiter:16.10f} [s]")
	print(f"DIRECT call: total= {sub_call:16.10f}[s], 1 iteration= {sub_call/numiter:16.10f} [s]")
	
