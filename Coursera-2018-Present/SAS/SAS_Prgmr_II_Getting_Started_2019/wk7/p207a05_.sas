***********************************************************;
*  Activity 7.05                                          *;
*  1) Run the program. Notice that, by default, PROC      *;
*     TRANSPOSE transposes all the numeric columns,       *;
*     Wind1-Wind4.                                        *;
*  2) Add a VAR statement in PROC TRANSPOSE to transpose  *;
*     only the Wind1 and Wind2 columns. Run the program.  *;
*  3) What are the names of the columns that contain the  *;
*     column names and values that have been transposed?  *;
***********************************************************;

libname pg2 'C:\Users\dsingh\Dropbox\Misc\Coursera\pg294_ue\EPG294\data';

title "Storm Wide";
proc print data=pg2.storm_top4_wide(obs=5);
run;

proc transpose data=pg2.storm_top4_wide out=storm_top4_narrow;
	by Season Basin Name;
	var Wind1 Wind2;
run;

title "Storm Narrow";
proc print data=storm_top4_narrow(obs=10);
run;
title;
