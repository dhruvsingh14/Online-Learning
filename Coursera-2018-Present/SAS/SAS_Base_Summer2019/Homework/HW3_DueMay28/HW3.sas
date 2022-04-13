data work.donations;
   set orion.Employee_donations;
   keep Employee_ID Qtr1 Qtr2 Qtr3 Qtr4;
   Total=sum(Qtr1,Qtr2,Qtr3,Qtr4);
run;

proc print data=work.donations;

