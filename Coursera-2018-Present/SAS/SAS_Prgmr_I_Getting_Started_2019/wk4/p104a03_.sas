***********************************************************;
*  Activity 4.03                                          *;
*    1) Change the name of the output table to            *;
*       STORM_CAT5.                                       *;
*    2) Include only Category 5 storms (MaxWindMPH        *;
*       greater than or equal to 156) with StartDate on   *;
*       or after 01JAN2000.                               *;
*    3) Add a statement to include the following columns  *;
*       in the output data: Season, Basin, Name, Type,    *;
*       and MaxWindMPH. How many Category 5 storms        *;
*       occurred since January 1, 2000?                   *;
***********************************************************;

libname pg1 "C:\Users\dsingh\Dropbox\Misc\Coursera\pg194_ue\EPG194\data" access = readonly;
libname out "C:\Users\dsingh\Dropbox\Misc\Coursera\pg194_ue\EPG194\output";

data out.STORM_CAT5 (keep = season basin name type maxwindmph);
    set pg1.storm_summary;	
	where maxwindmph >= 156 and year(startdate)>=2000; 
run;
