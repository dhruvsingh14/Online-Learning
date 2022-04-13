***********************************************************;
*  Activity 4.03                                          *;
*  1) Review the PROC FORMAT step that creates the        *;
*     $REGION format that assigns basin codes into        *;
*     groups. Highlight the step and run the selected     *;
*     code.                                               *;
*  2) Notice the DATA step includes IF-THEN/ELSE          *;
*     statements to create a new column named BasinGroup. *;
*  3) Delete the IF-THEN/ELSE statements and replace it   *;
*     with an assignment statement to create the          *;
*     BasinGroup column. Use the PUT function with Basin  *;
*     as the first argument and $REGION. as the second    *;
*     argument.                                           *;
*  4) Highlight the DATA and PROC MEANS steps and run the *;
*     selected code. How many BasinGroup values are in    *;
*     the summary report?                                 *;
***********************************************************;

libname pg2 'C:\Users\dsingh\Dropbox\Misc\Coursera\pg294_ue\EPG294\data';

proc format;
    value $region 'NA'='Atlantic'
                  'WP','EP','SP'='Pacific'
                  'NI','SI'='Indian'
                  ' '='Missing'
                  other='Unknown';
run;

data storm_summary;
    set pg2.storm_summary;
    Basin=upcase(Basin);
	BasinGroup = Put(Basin, $REGION.);
run;

proc means data=storm_summary maxdec=1;
	class BasinGroup;
	var MaxWindMPH MinPressure;
run;
