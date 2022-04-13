***********************************************************;
*  Activity 1.05a (Enterprise Guide)                      *;
*  1) Use the DATA step debugger to step through one      *;
*     iteration of the DATA step. Observe the values of   *;
*     Year and ProjectedSales as they are updated.        *;
*  2) Close the debugger and run the program. Examine the *;
*     log and output data. How many rows are in the input *;
*     and output tables?                                  *;
***********************************************************;

proc contents data=sashelp.shoes;
run;

data forecast;
	set sashelp.shoes;
	keep Region Product Subsidiary Year ProjectedSales;
	format ProjectedSales dollar10.;
    Year=1;
	ProjectedSales=Sales*1.05;
	Year=2;
	ProjectedSales=ProjectedSales*1.05;
	Year=3;
	ProjectedSales=ProjectedSales*1.05;
run;

/* because there isn't an explicit output statement after each projected sales assignment, 
only the last one for year=3 is written to the pdv */
