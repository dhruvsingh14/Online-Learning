/*******************************************************************/
/* Program Name: HW8                                               */
/* Program Location: C:\Users\dsingh\Dropbox\Stat_604\Homework\HW8 */
/* Date Created:  6/20/2019                                        */
/* Author: Dhruv Singh                                             */
/* Purpose: User defined formats, raw data files                   */

libname hwdata 'C:\Users\dsingh\Dropbox\Tamu\Stat_604\Homework\hwdata';
filename report 'C:\Users\dsingh\Dropbox\Tamu\Stat_604\Homework\HW8_DueJuly2\HW8DSingh_HW08_PCoutput.pdf';

/* step 1: raw data filename */

filename election 'C:\Users\dsingh\Dropbox\Tamu\Stat_604\Homework\hwdata\election_hist.csv';
filename region 'C:\Users\dsingh\Dropbox\Tamu\Stat_604\Homework\hwdata\region6.dat';

/* step 2: raw data filename, defined formats */
proc format;
	value $ camp_type 'I' = "Incumbent"
					'C' = "Challenger"
					'O' = "OpenSeat"
					other = "N/A"
					mssing = "N/A";
run;
					
proc format;
	value $ party 1 = "Democratic"
				2 = "Republican"
				3 = "Other"
				other = "N/A"
				mssing = "N/A";
run;

proc format;
	value $ status 'L' = "Lost"
				 'W' = "Won"
				 'R' = "Runoff"
				 other = "N/A"
				 mssing = "N/A";
run;

/* step 3: infile statements */
data elections;
	infile election dsd firstobs = 2;
	length Cand_ID $9 Cand_Name $38 Type $1 Party_Desig $3 State $2 District $2 Special_Stat $1 Primary_Stat $1 
		   Runoff_Stat $1 General_Stat $1 Year 8. Party $1 Receipts Transfers_From Disbursements
		   Transfers_To Start_Cash End_Cash Cand_Contrib Cand_Loans Other_Loans Cand_Repay
		   Other_Repay Debts Ind_Contrib General_Pct Pol_Contrib Party_Contrib End_Date 
		   Ind_Refunds Ctte_Refunds 8.;

	* 3a,b;
	input Year Cand_ID $ Cand_Name $ Type Party Party_Desig $ Receipts Transfers_From Disbursements Transfers_To 
		  Start_Cash End_Cash Cand_Contrib Cand_Loans Other_Loans Cand_Repay Other_Repay Debts Ind_Contrib State $
		  District $ Special_Stat $ Primary_Stat $ Runoff_Stat $ General_Stat $ General_Pct Pol_Contrib Party_Contrib 
		  End_Date Ind_Refunds Ctte_Refunds;
	
	* 3c;
	format Type $camp_type. Party $party. Special_Stat Primary_Stat Runoff_Stat General_Stat $status. End_Date worddate.;
run; 
