***********************************************************;
*  Activity 2.01                                          *;
*  1) Modify the program to retain TotalRain and set the  *;
*     initial value to 0.                                 *;
*  2) Run the program and examine the results. Why are    *;
*     all values for TotalRain missing after row 4?       *;
*  3) Change the assignment statement to use the SUM      *;
*     function instead of the plus symbol. Run the        *;
*     program again. Why are the results different?       *;
***********************************************************;

libname pg2 'C:\Users\dsingh\Dropbox\Misc\Coursera\pg294_ue\EPG294\data';

data zurich2017;
	set pg2.weather_zurich;
	retain totalrain 0;
	TotalRain=sum(TotalRain, Rain_mm);
run;
