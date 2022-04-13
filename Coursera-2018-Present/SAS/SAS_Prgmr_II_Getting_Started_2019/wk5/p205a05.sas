***********************************************************;
*  Activity 5.05                                          *;
*  1) Run the program. Which values for AvgTemp appear in *;
*     the output table?                                   *;
*  2) Change the order of the tables listed in the MERGE  *;
*     statement. Are the values for AvgTemp different?    *;
***********************************************************;

data weather_sanfran;
	merge pg2.weather_sanfran2017 pg2.weather_sanfran2016;
	by month;
run;
