#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 23:05:54 2024

@author: zx
"""

import os
import re
import subprocess
currpath=os.getcwd()

filname=os.listdir(currpath)

#print(filname)
pattern=r'^202\d+$'

machlist=[s for s in filname if re.match(pattern, s)]

#print(machlist)


command_ls=['ls']
for i in machlist:
    
    command_vit=['mcap_converter','--data_folder',i,'-o',i+'.mcap']
    result=subprocess.run(command_vit, capture_output=True,text=True)
    #print(result.stdout,type(result.stdout))