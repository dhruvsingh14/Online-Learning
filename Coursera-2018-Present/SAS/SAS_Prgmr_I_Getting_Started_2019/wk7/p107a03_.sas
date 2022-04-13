***********************************************************;
*  Activity 7.03                                          *;
*    1) Modify the query to create a temporary table      *;
*       named TOP_DAMAGE.                                 *;
*    2) Add an additional query in the same PROC SQL step *;
*       to generate a report that lists all the columns   *;
*       for the first 10 storms in the top_damage table.  *;
*    3) Add a TITLE statement before the second query to  *;
*       display the following text: Top 10 Storms by      *;
*       Damage Cost.                                      *;
*    4) How many of the top 10 storms occurred in 2005?   *;
***********************************************************;

libname pg1 'C:\Users\dsingh\Dropbox\Misc\Coursera\pg194_ue\EPG194\data' access=readonly;


proc sql ;
create table top_damage as
select Event, 
	Date format=monyy7., 
	Cost format=dollar16.
    from pg1.storm_damage
    order by Cost desc;

title "Top 10 Storms by Damage Cost"; *missed a semi colon here;
	select * from top_damage(obs=10); * asterisk used for all columns // both queries separated by semi colon, (obs=n) gives first n rows; 
quit;
