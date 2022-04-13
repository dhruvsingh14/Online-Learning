/*The pg1.np_westweather table contains weather-related information for four national parks: Death Valley National Park, Grand Canyon National Park, Yellowstone National Park, and Zion National Park. Use the MEANS procedure to analyze the data in this table.*/

/*What is the mean TempMin in DEATH VALLEY, CA US in 2016?*/


libname pg1 'C:\Users\dsingh\Dropbox\Misc\Coursera\pg194_ue\EPG194\data';

title 'Weather Statistics by Year and Park';

proc means data = pg1.np_westweather mean min max maxdec=2;
	var Precip Snow TempMin TempMax;
	class year name;	
run;

