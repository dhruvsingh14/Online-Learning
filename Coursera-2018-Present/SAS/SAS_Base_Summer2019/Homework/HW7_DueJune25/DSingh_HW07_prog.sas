/*******************************************************************/
/* Program Name: HW7                                               */
/* Program Location: C:\Users\dsingh\Dropbox\Stat_604\Homework\HW3 */
/* Date Created:  6/20/2019                                        */
/* Author: Dhruv Singh                                             */
/* Purpose:                                                        */

libname hwdata 'C:\Users\dsingh\Dropbox\Tamu\Stat_604\Homework\hwdata';
filename report 'C:\Users\dsingh\Dropbox\Tamu\Stat_604\Homework\HW7_DueJune25\HW7DSingh_HW07_PCoutput.pdf';

/* step 1: reading in data */

* reading in middle school data;
data mid;
	set hwdata.ok_mid;
	label Grade7 = "MidGrade7"
		Grade8 = "MidGrade8"
		Grade9 = "MidGrade9"
		Grade10 = "MidGrade10"
		Grade11 = "MidGrade11"
		Grade12 = "MidGrade12";
run;

* sorting by merge vars ;
proc sort data = mid;
	by mapcity school;
run;

* reading in high school data;
data high;
	set hwdata.ok_high;
	label Grade7 = "HSGrade7"
		Grade8 = "HSGrade8"
		Grade9 = "HSGrade9"
		Grade10 = "HSGrade10"
		Grade11 = "HSGrade11"
		Grade12 = "HSGrade12";
run;
* sorting for merge; 
proc sort data = high;
	by mapcity school;
run;


/* step 2: merge into 3 data sets */
data matched_schools (drop = Teachers) 
	high_nomatch(keep = school mapcity mailcity county)
	mid_nomatch(keep = school mapcity mailcity county); 

	* merge step;
	merge mid(in=mid rename=(Grade7-Grade12=MidGrade7-MidGRade12 
								PTRatio = MidPTRatio))
	high(in=high rename=(Grade7-Grade12=HSGrade7-HSGRade12 
								PTRatio = HSPTRatio));
	by mapcity school;
	drop Ungraded -- HStotal; *dropping by position;

	* step 2a (i) ; 
	array h{*} hsgrade7-hsgrade12;
	array m{*} midgrade7-midgrade12;

	* array for sum ;
	array grade{*} grade7-grade12;

	*step 2a (ii) ;
	do i = 1 to 6;
		grade{i} = sum(h{i},m{i});
	end;

	* step 2a (iii) - (iv);
	* array for imputing teachers for individual datasets;
	array midimptchr{*} midimptchr7-midimptchr12; 
	array hsimptchr{*} hsimptchr7-hsimptchr12; 

	* array for imputed teachers total;
	array imptchr{*} imptchr7-imptchr12; 

	* imputed teacher for each school;
	do i = 1 to 6;
		midimptchr{i} = m{i}/MidPTRatio;
		hsimptchr{i} = h{i}/HSPTRatio;
		
		imptchr{i} = sum(midimptchr{i},hsimptchr{i});
	end;

	* rounding up imputed teacher values;
	teachertotal = ceil(sum(of imptchr7-imptchr12));
	drop imptchr7-imptchr12 hsimptchr7-hsimptchr12 midimptchr7-midimptchr12 i;	

	* step 2a (v) ;
	studenttotal = sum(of grade7-grade12);

	* step 2a (vi) ;
	format ptrrevised 6.2;
	if (teachertotal ne 0) and (teachertotal ne .) then ptrrevised = studenttotal/teachertotal;

	* outputting merged datasets;
	*drop mapcity midgrade7 -- grade12;

	if mid=1 and high=1 then output matched_schools;

	* step 2b ;
	else if high=1 and mid=0 then output high_nomatch;

	* step 2c ; 
	else if high=0 and mid=1 then output mid_nomatch; 

run;


* formatting;

data matched_schools_fmtd (rename = (mapcity = City teachertotal = Teachers studenttotal = Students ptrrevised = PupilTeacherRatio));
	set matched_schools;
	keep School mapcity County teachertotal studenttotal ptrrevised;
	label ptrrevised = "Pupil/Teacher Ratio"
		mapcity = "City";
run;


/* step 3: printing options */

/* step 4: sorting data */
proc sort data = matched_schools_fmtd;
	by descending PupilTeacherRatio Students;
run;


options orientation = landscape dtreset nonumber;
ods pdf file = report;

title 'Oklahoma Public Schools';
title3 'Twenty-five Schools with Highest Pupil/Teacher Ratios';
footnote 'Source: National Center for Education Statistics (nces.ed.gov)';

/* step 5: printing top 25 */
proc print data = matched_schools_fmtd (obs=25);
run;

/* step 6: resetting options */
options nodate;
footnote;

/* step 7: proc freq */
title2 'Number of Schools by County';

proc freq data = matched_schools_fmtd;
	tables county / nocum ;
run;

/* step 8: proc means */
title3 'Analysis of Pupil/Teacher Ratio by County';

proc means data = matched_schools_fmtd n mean median;
class county;
run;

/* step 9: proc tab */
/*proc tabulate data = matched_schools_fmtd;*/
/*class county;*/
/*table school;*/
/*var PupilTeacherRatio Students;*/
/*run;*/

proc contents data=_all_;
run;

ods pdf close;
