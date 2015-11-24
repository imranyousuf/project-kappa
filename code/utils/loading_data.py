import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import os
import diagnostics as dg



def cond_psth(subject, run):
        """ Open Condiiton files """

        sub_path = os.path.realpath(subject)
        sub_path_cond= sub_path + '/model/model001/onsets'
        cond_path = [ i for i in os.listdir(sub_path_cond) ]
        list_cond_path= [sub_path_cond + '/' + i for i in cond_path]
        cond_txt = [i for i in os.listdir(list_cond_path[run-1])]
        cond_paths = [list_cond_path[run-1] + '/' + i for i in cond_txt]
        return cond_paths

def open_bold(subject, run):
        sub_path = os.path.realpath(subject)
        sub_path_bold= sub_path + '/BOLD'
        bold_path = [ i for i in os.listdir(sub_path_bold) ]
        list_bold_path= [sub_path_bold + '/' + i for i in bold_path]
        select_run =  list_bold_path[run-1] + '/' + 'bold.nii'
        return nib.load(select_run).get_data()
