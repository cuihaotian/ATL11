# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:24:11 2017

@author: ben
"""
from glob import glob
import numpy as np
from ATL06_to_ATL11 import fit_ATL11
#import sys
 
np.seterr(invalid='ignore')

#try:
#    del sys.modules['ATL06_data']; 
#except:
#    pass
#from ATL06_data import ATL06_data 
#filenames=glob('/Volumes/ice1/ben/sdt/ATLxx_example/PIG_Collab_v13A/ATL06/run_1/rep_*/Track_462_D3.h5')
filenames=glob('/Volumes/ice1/ben/sdt/ATLxx_example/PIG_Collab_v13B_NoFirn_NoDz/ATL06/run_1/rep_*/Track_462_D3.h5') 
#x_ctr=33044510.0
x_ctr=33046250.0
#x_ctr=33046270.0

#filenames=glob('/Volumes/ice1/ben/sdt/ATLxx_example/PIG_Collab_v13B_NoFirn_NoDz/ATL06/run_1/rep_*/Track_469_D3.h5') 
#x_ctr=28512071.0
#filenames=glob('/Volumes/ice1/ben/sdt/ATLxx_example/PIG_Collab_v13B_NoFirn_NoDz/ATL06/run_1/rep_*/Track_972_D3.h5') 
#x_ctr=28470392.0
#filenames=filenames[0:3] 
# NEED TO TRY WITH THESE FILES AND PAIR=1

P11=fit_ATL11(filenames, beam_pair=3, seg_x_centers=x_ctr+np.arange(0, 60, 120), DOPLOT=True) # defined in ATL06_to_ATL11  step=60
