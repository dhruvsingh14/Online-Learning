***********************************************************;
*  Activity 7.04                                          *;
*    1) Define aliases for STORM_SUMMARY and              *;
*       STORM_BASINCODES in the FROM clause.              *;
*    2) Use one table alias to qualify Basin in the       *;
*       SELECT clause.                                    *;
*    3) Complete the ON expression to match rows when     *;
*       Basin is equal in the two tables. Use the table   *;
*       aliases to qualify Basin in the expression. Run   *;
*       the step.                                         *;
***********************************************************;
*  Syntax                                                 *;
*     FROM table1 AS alias1 INNER JOIN table2 AS alias2   *;
*     ON alias1.column = alias2.column                    *;
***********************************************************;
libname pg1 'C:\Users\dsingh\Dropbox\Misc\Coursera\pg194_ue\EPG194\data' access=readonly;

proc sql;
select Season, Name, x.Basin, BasinName, MaxWindMPH 
    from pg1.storm_summary as x 
	inner join pg1.storm_basincodes as y
	on x.basin = y.basin 
	order by Season desc, Name;
quit;

