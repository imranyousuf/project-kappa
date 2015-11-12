<<<<<<< HEAD
% Project Kappa Progress Report
% Zheng Chang, Giancarlo Escobar, Noel Pimentel, Imran Yousuf, 
% November 12, 2015

# Background

## The Paper

- from OpenFMRI.org
- ds001

## The Data

- 12 subjects
- 2 conditions per subject


## The Method

- linear regression
- machine learning

# Initial work

## EDA

- downloaded data
- simple plots, summary statistics

## Task Time Course 
![picture](https://github.com/changzheng1993/project-kappa/blob/master/slides/time_course_cond001_task001%20copy.png )

# Next steps

## Preprocessing / Validation

- PCA

## Statistical Analysis

- linear model
=======
% Project Kappa Progress Report
% Zheng Chang, Giancarlo Escobar, Noel Pimentel, Imran Yousuf, 
% November 12, 2015

# Background

## The Paper
- "Distributed and overlapping representations of faces and objects in ventral temporal cortex" Haxby et al.
- "Combinatorial codes in ventral temporal lobe for object recognition: Haxby (2001). revisited: is there a ?face? area?" Hanson et al.
- "Partially distributed representations of objects and faces in ventral temporal cortex" O'Toole et al.
- from OpenFMRI.org
- ds105 

## The Data

- 6 subjects (sub001, sub002,...,sub006)
- 1 task (object viewing)
- 8 conditions per task (house, scrambled, cat, shoe, bottle, scissors, chair, face)
- 12 runs per subject (72 bold.nii files)

## The Method

- Haxby Similarity Method
- Convolution
- Linear Regression
- Machine Learning

# Initial work

## EDA

- Downloaded data
- Simple plots, summary statistics
- Folder structure of ds105
- Coded to merge individual 12 bold.nii files for sub001, sub002, etc.

# Next steps

## Preprocessing / Validation

- Feture Selection(Lasso/Ridge regression/)
- PCA

## Statistical Analysis

- linear model
>>>>>>> d0004f208f8f120e15a21d6373c20f28a95638bc
