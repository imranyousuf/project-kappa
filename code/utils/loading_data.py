import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import os




def cond_file(subject, run, cond):
        """ Opens a condition txt for a subject and one of their runs. """
        sub_path = os.path.realpath('../../data/ds105/'+subject)
        sub_path_cond= os.path.join(sub_path,'model/model001/onsets','task001_run00'+str(run),'cond00'+str(cond))
        return sub_path_cond

def list_cond_file(subject, run):
        sub_path = os.path.realpath('../../data/ds105/'+str(subject))
        sub_path_cond= sub_path + '/model/model001/onsets'
        cond_path = [ i for i in os.listdir(sub_path_cond) ]
        list_cond_path= [sub_path_cond + '/' + i for i in cond_path if not (i.startswith('.'))]
        cond_txt = [i for i in os.listdir(list_cond_path[run-1])]
        cond_paths = [list_cond_path[run-1] + '/' + i for i in cond_txt if not (i.startswith('.'))]
        return cond_paths

def bold_data(subject, run):
        sub_path = os.path.realpath('../../data/preprocessed_ds105/'+str(subject))
        direct_path = os.path.join(sub_path,'model/model001','task001_run00'+str(run)+'.feat','filtered_func_data_mni.nii.gz')
        img= nib.load(direct_path)
        data = img.get_data()
        return data
