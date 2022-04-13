***********************************************************;
*  Activity 6.02                                          *;
*  1) Run the program and view the Savings3K table.       *;
*  2) How many months until James exceeds 3000 in         *;
*     savings?                                            *;
*  3) How much savings does James have at that month?     *;
*  4) Change the DO UNTIL statement to a DO WHILE         *;
*     statement and modify the expression to produce the  *;
*     same results.                                       *;
*  5) Run the program and view the Savings3K table.       *;
*  6) Are the results for James identical with the DO     *;
*     WHILE as compared to the DO UNTIL?                  *;
***********************************************************;

libname pg2 'C:\Users\dsingh\Dropbox\Misc\Coursera\pg294_ue\EPG294\data';

data Savings3K;
   set pg2.savings;
   Month=0;
   Savings=0;
   do while (Savings<=3000);
      Month+1;
      Savings+Amount;
      Savings+(Savings*0.02/12);
   end;
   format Savings comma12.2;
run;


***********************************************************;
*  Quiz notes for module 6                                *;
***********************************************************;

data bikeinfo;
   input name $ bike;
   datalines;
Marco 12
Angela 10
;

data test;
    bike=10;
    do day=1 to 7 while (bike lt 13);
       bike=bike+2;
    end;
run;
