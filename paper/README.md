## Final Report

We have uploaded the pdf as report_final.pdf but you can always recompile it using the method below:

The Makefile contains recipes to generate the report. 

- `make all`: Generates the PDF of our report, including appendices. 

- `make clean`: `make all` generates a lot of intermediate files besides the 
desired PDF, so `make clean` will remove all these other files. 

- `make reset`: does the same thing as make clean, but also removes the report 
PDF, effectively reseting the directory to the state it was in prior to calling 
`make all`.

