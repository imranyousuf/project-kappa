import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import os
import diagnostics as dg



def cond_txt(subject, run, cond):
        """ Opens a condition txt for a subject and one of their runs. """

        sub_path = os.path.realpath(subject)
        sub_path_cond= sub_path + '/model/model001/onsets'
        cond_path = [ i for i in os.listdir(sub_path_cond) ]
        list_cond_path= [sub_path_cond + '/' + i for i in cond_path]
        cond_txt = [i for i in os.listdir(list_cond_path[run-1])]
        cond_paths = [list_cond_path[run-1] + '/' + i for i in cond_txt]
        select_path = cond_paths[cond-1]
        return np.loadtxt(select_path)

def bold_data(subject, run):
        """ Returns data array of BOLD for a particular run for a subject. """

        sub_path = os.path.realpath(subject)
        sub_path_bold= sub_path + '/BOLD'
        bold_path = [ i for i in os.listdir(sub_path_bold) ]
        list_bold_path= [sub_path_bold + '/' + i for i in bold_path]
        select_run =  list_bold_path[run-1] + '/' + 'bold.nii'
        return nib.load(select_run).get_data()
