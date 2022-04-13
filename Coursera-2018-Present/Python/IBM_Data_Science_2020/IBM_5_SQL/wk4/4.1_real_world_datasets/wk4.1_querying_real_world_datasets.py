##########################################
# Week 4.1: Querying Real World Datasets #
##########################################

####################################
# Import the ibm_db Python library #
####################################

import ibm_db

################################################
# Identify the database connection credentials #
################################################

#Replace the placeholder values with the actuals for your Db2 Service Credentials
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_hostname = "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"            # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_port = "50000"                    # e.g. "50000"
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_uid = "bzr25790"                 # e.g. "abc12345"
dsn_pwd = "9nqsnndjss-d342r"                 # e.g. "7dBZ3wWt9XN6$o0J"

##################################
# Create the database connection #
##################################

#Create database connection
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )

#################################################
# Using Python Variables in your SQL Statements #
#################################################

import pandas as pd
import matplotlib.pyplot as plt
import ibm_db_dbi
import seaborn

#connection for pandas
pconn = ibm_db_dbi.Connection(conn)

schools_query = "SELECT * from SYSCAT.Tables;"
dataframe = pd.read_sql(schools_query, pconn)
# print(dataframe)

##################
# Table Metadata #
##################
schools_table = """SELECT TABSCHEMA, TABNAME, CREATE_TIME
        from syscat.Tables
        where tabschema = 'BZR25790'
        """
df = pd.read_sql(schools_table, pconn)
df

###################
# Column Metadata #
###################
schools_cols = """SELECT *
        from syscat.columns
        where tabname = 'CHICAGO_SCHOOLS'
        """
cols = pd.read_sql(schools_cols, pconn)
cols
# 78 columns

#####################
# Column Properties #
#####################
column_properties = """SELECT distinct(colname),typename, length
        from syscat.columns
        where tabname = 'CHICAGO_SCHOOLS'
        """
col_props = pd.read_sql(column_properties, pconn)
col_props

#########################
# Questions To Consider #
#########################

# 1
# school id is in mixed characters - upper and lower

# 2
# varname: COMMUNITY_AREA_NAME, all caps

# 3
# most column names having a space in raw format, are replaced with underscores
# variables such as rate per 100 see parentheses replaced with underscores

#############
# Problem 1 #
#############
elementary_schools = """SELECT count(*)
        from CHICAGO_SCHOOLS
        where "Elementary, Middle, or High School" = 'ES';
        """
el_schools = pd.read_sql(elementary_schools, pconn)
el_schools

#############
# Problem 2 #
#############
safety_scores_high = """SELECT max(SAFETY_SCORE)
        from CHICAGO_SCHOOLS;
        """
sfty_scr_mx = pd.read_sql(safety_scores_high, pconn)
sfty_scr_mx
# 99 is the highest safety score

#############
# Problem 3 #
#############
safest_schools = """SELECT NAME_OF_SCHOOL
        from CHICAGO_SCHOOLS
        where SAFETY_SCORE = 99;
        """
safe_schools = pd.read_sql(safest_schools, pconn)
safe_schools

#############
# Problem 4 #
#############
highest_attendance = """SELECT NAME_OF_SCHOOL, AVERAGE_STUDENT_ATTENDANCE
        from CHICAGO_SCHOOLS
        where AVERAGE_STUDENT_ATTENDANCE is not null
        order by AVERAGE_STUDENT_ATTENDANCE desc
        limit 10;
        """
attendance_h = pd.read_sql(highest_attendance, pconn)
attendance_h

#############
# Problem 5 #
#############
lowest_attendance = """SELECT NAME_OF_SCHOOL, AVERAGE_STUDENT_ATTENDANCE
        from CHICAGO_SCHOOLS
        where AVERAGE_STUDENT_ATTENDANCE is not null
        order by AVERAGE_STUDENT_ATTENDANCE
        limit 5;
        """
attendance_l = pd.read_sql(lowest_attendance, pconn)
attendance_l

#############
# Problem 6 #
#############
attendance_num = """SELECT NAME_OF_SCHOOL,
        substring(AVERAGE_STUDENT_ATTENDANCE,1,5)
            as Avg_Attendance
        from CHICAGO_SCHOOLS
        where AVERAGE_STUDENT_ATTENDANCE is not null
        order by AVERAGE_STUDENT_ATTENDANCE
        limit 5;
        """
attendance_n = pd.read_sql(attendance_num, pconn)
attendance_n

#############
# Problem 7 #
#############
attendance_pctile = """SELECT NAME_OF_SCHOOL,
        substring(AVERAGE_STUDENT_ATTENDANCE,1,2)
            as Avg_Attendance
        from CHICAGO_SCHOOLS
        where AVERAGE_STUDENT_ATTENDANCE is not null
        and not AVERAGE_STUDENT_ATTENDANCE like '9%'
        and not AVERAGE_STUDENT_ATTENDANCE like '8%'
        and not AVERAGE_STUDENT_ATTENDANCE like '7%'
        order by AVERAGE_STUDENT_ATTENDANCE desc;
        """
attendance_pct = pd.read_sql(attendance_pctile, pconn)
attendance_pct

#############
# Problem 8 #
#############
# 77 comm areas
# checking total school enrollment in each

total = """SELECT COMMUNITY_AREA_NAME, SUM(COLLEGE_ENROLLMENT) as Total_Enrolled
        from CHICAGO_SCHOOLS
        GROUP BY COMMUNITY_AREA_NAME;
        """
el_tot = pd.read_sql(total, pconn)
el_tot

#############
# Problem 9 #
#############
# lowest enrollment community areas

total2 = """SELECT COMMUNITY_AREA_NAME, SUM(COLLEGE_ENROLLMENT) as Total_Enrolled
        from CHICAGO_SCHOOLS
        GROUP BY COMMUNITY_AREA_NAME
        ORDER BY Total_Enrolled
        LIMIT 5;
        """
el_tot2 = pd.read_sql(total2, pconn)
el_tot2

##############
# Problem 10 #
##############
# hardship index given enrollment
hardship_join = """SELECT SCH.COMMUNITY_AREA_NAME, SES.HARDSHIP_INDEX,
        SCH.COMMUNITY_AREA_NUMBER, SES.COMMUNITY_AREA_NUMBER,
        SCH.COLLEGE_ENROLLMENT
        from CHICAGO_SCHOOLS SCH, CHICAGO_SES SES
        WHERE SCH.COMMUNITY_AREA_NUMBER = SES.COMMUNITY_AREA_NUMBER
        AND SCH.COLLEGE_ENROLLMENT = 4368
        ORDER BY SCH.COLLEGE_ENROLLMENT DESC;
        """
enrollment_hardship = pd.read_sql(hardship_join, pconn)
enrollment_hardship

##############
# Problem 11 #
##############
# highest enrol ca, hardship index
high_enroll_ca = """SELECT SCH.COMMUNITY_AREA_NAME, SES.HARDSHIP_INDEX,
        SCH.COLLEGE_ENROLLMENT
        from CHICAGO_SCHOOLS SCH, CHICAGO_SES SES
        WHERE SCH.COMMUNITY_AREA_NUMBER = SES.COMMUNITY_AREA_NUMBER
        ORDER BY SCH.COLLEGE_ENROLLMENT DESC
        LIMIT 1;
        """
high_enroll_hardship = pd.read_sql(high_enroll_ca, pconn)
print(high_enroll_hardship)




















# in order to display plot within window
# plt.show()
