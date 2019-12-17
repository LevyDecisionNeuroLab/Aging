# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:00:15 2019

@author: yl2268
"""

import numpy as np
import os
#import scipy.io as spio
import pandas as pd
from pathlib import Path
import glob
data_behav_root = Path('c:/Users/yl2268/Documents/Aging/RawData/')
out_root = 'c:/Users/yl2268/Documents/Aging/RA_aging/Behavior Analysis/'

# load .csv file from post scan survey: PostScanSurvey.csv file
getFile=glob.glob(os.path.join(data_behav_root,'RA_PostTaskSurvey'+'*.csv'))
RawData = pd.read_csv(getFile[0])
RawData = RawData.loc[2:,]
data = pd.DataFrame(columns=['id','is_med','rating0','rating1','rating2','rating3','rating4'])
headers = ['Q34','Q19_1','Q19_2','Q19_3','Q19_4','Q19_5','RMed_4','RMed_1','RMed_2','RMed_3','RMed_8']
subj = RawData[headers[0]].to_numpy()
Mon = RawData[headers[1:6]].to_numpy()
Med = RawData[headers[6:11]].to_numpy()
data['id']=np.concatenate((subj,subj))
data['is_med']=np.concatenate((np.repeat(0,len(subj)),np.repeat(1,len(subj))))
data.loc[range(len(subj)*2),['rating0','rating1','rating2','rating3','rating4']] = np.concatenate((Mon,Med),axis=0)
data.to_csv(os.path.join(out_root+'PostTaskSurveyRating_12172019.csv'),index=False)
