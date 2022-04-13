***********************************************************;
*  Activity 5.06                                          *;
*    1) Add options to include N (count), MEAN, and MIN   *;
*       statistics. Round each statistic to the nearest   *;
*       integer.                                          *;
*    2) Add a CLASS statement to group the data by Season *;
*       and Ocean. Run the program.                       *;
*    3) Modify the program to add the WAYS statement so   *;
*       that separate reports are created for Season and  *;
*       Ocean statistics. Run the program.                *;
*       Which ocean had the lowest mean for minimum       *;
*       pressure?                                         *;
*       Which season had the lowest mean for minimum      *;
*       pressure?                                         *;
***********************************************************;

libname pg1 'C:\Users\dsingh\Dropbox\Misc\Coursera\pg194_ue\EPG194\data' access = readonly;




proc means data=pg1.storm_final N MEAN MIN maxdec=0;
	var MinPressure;
	class season ocean;
	ways 1;
	where Season >=2010;
run;
