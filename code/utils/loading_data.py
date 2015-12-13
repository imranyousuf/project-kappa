import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import os

def cond_file(subject, run, cond):
    """ 
    This function returns the path of the condition file you choose 

    Parameter
    ---------
    subject : str
    	Please specific the subject. For example, you should input 'sub001' if choose the first subject.
    run : int
    	Please specific the subject. For example, you should input '01' if choose the first run '12' for the twelfth run.
    cond : int
        Please specific the subject. For example, you should input '1' if choose the first condition. 

    Return 
    ------
    path : str
	   This is the path of the condition file that you chose.
    """

    sub_path = os.path.realpath('../../data/ds105_cond/'+subject)
    sub_path_cond= os.path.join(sub_path,'model/model001/onsets','task001_run0'+str(run).zfill(2) ,'cond00'+str(cond))
    
    return sub_path_cond


def list_cond_file(subject, run):
    """ 
    This function returns condition list.

    Parameter
    ---------
    subject : str 
    	Please specify the number of the subject. For example, you should input 'sub001' if choose the first subject.
    run : int
    	Please specific the subject. For example, you should input '01' if choose the first run '12' for the twelfth run.

    Returns
    ------
    condition : list
    	It lists each conditions 
    """

    sub_path = os.path.realpath('../../data/ds105_cond/'+str(subject))
    sub_path_cond= sub_path + '/model/model001/onsets'
    cond_path = [ i for i in os.listdir(sub_path_cond) ]
    list_cond_path= [sub_path_cond + '/' + i for i in cond_path if not (i.startswith('.'))]
    cond_txt = [i for i in os.listdir(list_cond_path[run-1])]
    cond_paths = [list_cond_path[run-1] + '/' + i for i in cond_txt if not (i.startswith('.'))]
    
    return cond_paths


def bold_data(subject, run):
    """ 
    This function returns the fMRI data according to the subject number and task run number 

    Parameter
    ---------
    subject : str
    	Please specific the subject. For example, you should input 'sub001' if choose the first subject.
    run : int
    	Please specific the subject. For example, you should input '01' if choose the first run and '12' if you choose the twelfth.

    Return
    ------
    data : 4D matrix
    	fMRI data for subject for specific run
    """

    sub_path = os.path.realpath('../../data/ds105/'+str(subject))
    direct_path = os.path.join(sub_path,'model/model001','task001_run0'+str(run).zfill(2) +'.feat','filtered_func_data_mni.nii.gz')
    img= nib.load(direct_path)
    data = img.get_data()
    
    return data
