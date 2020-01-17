#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:58:41 2020

@author: nachshon
"""
import os
import glob
import json

ses = {}
root_dir='/media/Data/Aging/test/'
file_stracture = 'sub-*/ses-1/func/sub-*_ses-1*.json'
glober = root_dir+file_stracture

# get all subjects data in a dicionary
for sub in glob.glob(glober):
    name = sub.split(sep="/")
    if name[5] not in ses:
        ses[name[5]] = {}
    if "rest" not in sub:  
        with open(sub, "r") as read_file:
            data = json.load(read_file)
            name = sub.split(sep="/")
            ses[name[5]][name[8].split("_")[2]]=data['SeriesNumber']    

# rearange order and set it to start at 1
for key in ses:
    sub = ses[key]
    key_min = min(sub.keys(), key=(lambda k: sub[k]))
    value_min = sub[key_min]
    for k in sub:
        sub[k]=sub[k]-value_min+1
        
for key in ses:
    sub =ses[key]
    for task in sub:
        oldnifti = root_dir+key+'/ses-1/func/'+key+"_ses-1_"+task+"_bold.nii.gz"
        newnifti = root_dir+key+'/ses-1/func/'+key+"_ses-1_task-task"+str(sub[task])+"_bold.nii.gz"
               
        oldjson = root_dir+key+'/ses-1/func/'+key+"_ses-1_"+task+"_bold.json"
        newjson = root_dir+key+'/ses-1/func/'+key+"_ses-1_task-task"+str(sub[task])+"_bold.json"
        os.rename(oldnifti,newnifti)
        os.rename(oldjson,newjson)
