/*******************************************************************/
/* Date Last Submitted: 6/4/2019                                   */
/* Program Name:                                                   */
/* Program Location: C:\Users\dsingh\Dropbox\Stat_604\Homework\HW3 */
/* Date Created:                                                   */
/* Author: Dhruv Singh                                             */
/* Purpose:                                                        */

/* Step 2: creating libref to tx_schools dataset */
libname txsch 'C:\Users\dsingh\Dropbox\Tamu\Stat_604\Homework\hwdata' access = readonly;

* reading in tx_schools dataset;
data texas_hs;
	set txsch.tx_schools;
run;

/* Step 3: creating libref to permanent data directory */
libname my_lib 'C:\Users\dsingh\Dropbox\Tamu\Stat_604\Homework\HW4';

/* Step 4: pdf fileref */
filename dns 'C:\Users\dsingh\Dropbox\Tamu\Stat_604\Homework\HW4\DSingh_HW04_output.pdf';

/* Step 5: subsetting to relevant observations */
data my_lib.texas_hs;
	set work.texas_hs;
	where (sr>=1) or (jr>=1) or (so>=1) or (fr>=1);
	drop state type level f16 f17;
	label fte_teachers = 'Teachers (FTE)'
		  ptr = 'Student/Teacher Ratio'
		  control = 'School Type'
		  gr8 = 'Eighth Graders'
	      fr = 'Freshmen'
		  so = 'Sophomores'
		  jr = 'Juniors'
		  sr = 'Seniors';
run;

* creating new variable to compute enrollment;
data my_lib.texas_hs;
	set my_lib.texas_hs;
	enrollment = sum(fr, so, jr, sr);
	label enrollment = 'HS Enrolment';	
run;

* creating new variable to compute current date;
data my_lib.texas_hs;
	set my_lib.texas_hs;
	origin_date = today();
	label origin_date = 'Origin Date';
	format origin_date MMDDYY10.;
run;


/* ods */
ods pdf file= dns notoc;

/* Step 6: ods, printing the descriptor portion */
title 'Step 6: Descriptor Portion of Revised Texas High School Data Set';

proc contents data = my_lib.texas_hs;
run;

/* Step 7: printing the first 10 observations */
title 'Step 7: First 10 Observations of Revised Texas High School Data Set';

proc print data = my_lib.texas_hs(obs=10) label;
run;

/* Step 8: creating temporary data set for academy list */
data work.academy_list;
	set my_lib.texas_hs;
	keep school enrollment county control;
	where school contains 'ACADEMY' and school not eq 'ACADEMY H S';
run;

/* Step 9: printing academy list */
title 'Step 9: List of Academies';

proc print data = work.academy_list label;
var school enrollment county control;
run;


/* Step 10: creating temporary data set for seniors proportion */
data work.seniors;
	set my_lib.texas_hs;
	keep school county gr8 fr so jr sr enrollment;
	where sr > .25*(enrollment) and not(fr=. & jr=. & so=.);
run;

/* Step 11: printing academy list */
title 'Step 11: Schools with Larger Senior Class';

proc print data = work.seniors label noobs;
var school enrollment sr jr so fr gr8 county;
run;

/* Step 12: creating multiple temp datasets */
data SixA (drop = Division) TAPS3 (drop = Division County) Align19;
	set my_lib.texas_hs;
	drop control fte_teachers ptr;
	where (sr >= 1) and (jr >= 1) and (so >= 1) and (fr >= 1);
	Division = 'TAPS0';
	if Control = 'Public' and (Enrollment < 81) then Division = '1A' ;
	else if Control = 'Public' and (81 <= Enrollment <= 200) then Division = '2A';
	else if Control = 'Public' and (201 <= Enrollment <= 400) then Division = '3A';
	else if Control = 'Public' and (401 <= Enrollment <= 800) then Division = '4A';
	else if Control = 'Public' and (801 <= Enrollment <= 1600) then Division = '5A';
	else if Control = 'Public' and (1601 <= Enrollment) then Division = '6A'; 

	if Control = 'Private' and (Enrollment <= 55) then Division = 'TAPS1';
	else if Control = 'Private' and (56 <= Enrollment <= 110) then Division = 'TAPS2';
	else if Control = 'Private' and (111 <= Enrollment) then Division = 'TAPS3';

	select (Division);
		when ('6A') output SixA;
		when ('TAPS3') output TAPS3;
		when ('1A', '2A', '3A', '4A', '5A', '6A', 'TAPS1', 'TAPS2', 'TAPS3') output Align19;
		otherwise;
	end;
run;

/* Step 13: creating GradeCount dataset */
data GradeCount (keep = school division grade students);
	set align19;
	if gr8 ne 0 | gr8 ne . then do;
		grade = 'Eighth';
		students = gr8;
	end;
	output;
	if fr ne 0 | fr ne . then do;
		grade = 'Freshman';
		students = fr;
	end;
	output;
	if so ne 0 | so ne . then do;
		grade = 'Sophomore';
		students = so;
	end;
	output;
	if jr ne 0 | jr ne . then do;
		grade = 'Junior';
		students = jr;
	end;
	output;
	if sr ne 0 | sr ne . then do;
		grade = 'Senior';
		students = sr;
	end;
	output;
run;

/* Step 14: displaying proc contents for all temp datasets*/
title 'Step 14: List of Data Sets in Work Library';

proc contents data = work._ALL_ nods;
run; 

/* Step 15: printing from firstobs = b f terry onward */
title 'Step 15: Sample of Align19 Data Set';

proc print data = work.align19 (firstobs = 50 obs=50) noobs;
run;

/* Step 16: printing last 30 obs of sixA data */
title 'Step 16: Last 30 Observations of SixA Data Set';

proc print data = work.SixA (firstobs = 20 obs=30);
run;

/* Step 17: printing taps3 dataset */
title 'Step 17: Taps3 Data Set';

proc print data = work.taps3;
run;

/* Step 18: printing gradecount data sample */
title 'Step 18: Sample of GradeCount Data Set';

proc print data = work.gradecount (obs=35);
run;

/* Step 19: proc tabulate */
title 'Step 19: Number of Students by Grade and Division';

proc tabulate data=gradecount; class division grade; var students;

table grade='Grade', division*students=' '*sum=' '*f=comma7.;

run;


ods pdf close;

