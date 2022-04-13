**************************************************;
*  Activity 2.05                                 *;
*    Add a subsetting IF statement to output     *;
*    only the final day of each month.           *;
**************************************************;

libname pg2 'C:\Users\dsingh\Dropbox\Misc\Coursera\pg294_ue\EPG294\data';

data houston_monthly;
	set pg2.weather_houston;
	keep Date Month DailyRain MTDRain;
	by Month;
	if first.Month=1 then MTDRain=0;
	if last.Month;
	MTDRain+DailyRain;
run;       

