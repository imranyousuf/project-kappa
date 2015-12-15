## Analyzing the Data

The Makefile contains recipes to perform the intermediate analysis for the 
project, as well as generate some supplementary work and test all user-defined 
functions. The results of this directory should largely be regarded as 
transitional (but nonetheless valuable) steps in the progression of our work. 
Many of the scripts run processes that are no longer in use, or primarily 
serve as illustrative examples on how to utilize certain functions for a 
single subject. For those strictly interested in our final analysis, we 
recommend looking at our `project-kappa/final` directory instead. 

- `make all`: Performs all intermediate data analysis and eda

- `make clean`: Removes all extra files generated when compiling code. Does 
this recursively for all subdirectories. 

- `make test`: Tests all user-defined functions associated with analyzing the 
data. 


All output figures are saved in `project-kappa/images`, which also caches the 
figures required for the report and slides. These figures can be reproduced in 
their entirety by navigating to `project-kappa/final` and running `make all`. 