***********************************************************;
*  Activity 3.02                                          *;
*  1) Examine the program and notice that all quiz scores *;
*     for two students are changed to missing values.     *;
*     Highlight the first DATA step and submit the        *;
*     selected code.                                      *;
*  2) In a web browser, access SAS Help at                *;
*     http://support.sas.com/documentation. In the Syntax *;
*     Shortcuts section, click the 9.4 link next to SAS   *;
*     Language Elements by Name, Product, and Category.   *;
*  3) Access the alphabetical listing for CALL routines.  *;
*     Use the documentation to read about the CALL        *;
*     MISSING routine.                                    *;
*  4) Simplify the second DATA step by using CALL MISSING *;
*     to assign missing values for the two students' quiz *;
*     scores. Run the step.                               *;
***********************************************************;
/* Step 1 */

libname pg2 'C:\Users\dsingh\Dropbox\Misc\Coursera\pg294_ue\EPG294\data';

data quiz_report;
    set pg2.class_quiz;
	if Name in("Barbara", "James") then do;
		Quiz1=.;
		Quiz2=.;
		Quiz3=.;
		Quiz4=.;
		Quiz5=.;
	end;
run;

/* Step 4 */
data quiz_report;
    set pg2.class_quiz;
	if Name in("Barbara", "James") then call missing(of Quiz1-Quiz5); /* alternatively - call missing(of Q:)*/
run;

