libname stat1 '\\toaster\homes\d\h\dhnsingh\nt\est142_ue\est142_ue\est142\data';

************;
* quiz 1.1  ;
************;

data body_temp;
	set stat1.normtemp;
run;

proc univariate data = body_temp;
	var bodytemp heartrate;
	histogram;
run;

************;
* quiz 1.2  ;
************;

ods graphics on;

proc ttest h0 = 98.6 plots(showH0) sides = 2 alpha = 0.05;
	var bodytemp;
run;

ods graphics off; 

*************;
* quiz 1.07  ;
*************;

libname stat1 '\\toaster\homes\d\h\dhnsingh\nt\est142_ue\est142_ue\est142\data';

data german;
	set stat1.german;
run;

ods graphics;
proc ttest data = german plots(shownull) = interval;
	class group; /* must have exactly two levels --  can always use format to impose binary condition*/ 
	var change;
	title "Two Sample t-test comparing training program";
run;

title;
