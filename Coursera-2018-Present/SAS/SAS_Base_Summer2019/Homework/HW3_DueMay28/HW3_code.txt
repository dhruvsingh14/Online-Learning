/*******************************************************************/
/* Program Name: Assignment 3                                      */
/* Program Location: C:\Users\dsingh\Dropbox\Stat_604\Homework\HW3 */
/* Date Created: 5/25/2019                                         */
/* Author: Dhruv Singh                                             */
/* Purpose: Permanent data sets, Proc contents, ODS, Reports       */


/* Creating library using directory containing orion dataset */
libname orion 'C:\Users\dsingh\Dropbox\Stat_604\CourseMaterials\PRG1_Data_and_Programs' access=readonly;
libname donation 'C:\Users\dsingh\Dropbox\Stat_604\Homework\HW3';



/* Creating temporary dataset using orion employee data, quarterly donations */
/*data work.donations;*/
/*   set orion.Employee_donations;*/
/*   keep Employee_ID Qtr1 Qtr2 Qtr3 Qtr4;*/
/*   Total=sum(Qtr1,Qtr2,Qtr3,Qtr4);*/
/*run;*/

/* Printing quarterly donations */
*proc print data=work.donations;

/* Saving data to permanent library */
/*data donation.donations;*/
/*   set orion.Employee_donations;*/
/*   keep Employee_ID Qtr1 Qtr2 Qtr3 Qtr4;*/
/*   Total=sum(Qtr1,Qtr2,Qtr3,Qtr4);*/
/*run;*/


/* Output delivery system - pdf */
/*ods pdf file='DSingh_HW03_outputA.pdf' bookmarkgen=no;*/
/*title 'Descriptor Portion of Donations Permanent Data Set';*/
/*proc contents data=donation.donations;*/
/*run;*/
/**/
/*title 'Descriptor Portion of All Data Sets in Work Library';*/
/*proc contents data=work._ALL_;*/
/*run;*/
/**/
/*title 'List of Data Sets in Orion Library';*/
/*proc contents data=orion._ALL_ nods;*/
/*run;*/
/*ods pdf close;*/


/* Output delivery system - pdf */
ods pdf file='DSingh_HW03_outputB.pdf' style=ocean bookmarkgen=no;
title 'Descriptor Portion of Donations Permanent Data Set';
proc contents data=donation.donations;
run;

title 'Descriptor Portion of All Data Sets in Work Library';
proc contents data=work._ALL_;
run;

title 'List of Data Sets in Orion Library';
proc contents data=orion._ALL_ nods;
run;
ods pdf close;


