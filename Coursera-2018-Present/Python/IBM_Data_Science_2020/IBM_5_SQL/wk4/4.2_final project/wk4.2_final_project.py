###########################
# Week 4.2: Final Project #
###########################

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

#############
# Problem 1 #
#############
# Number of rows in Crime table
rows = """SELECT COUNT(*)
        FROM CHICAGO_CRIME;
        """
crime_rows = pd.read_sql(rows, pconn)
crime_rows

#############
# Problem 2 #
#############
# First ten rows in Crime table
first10rows = """SELECT *
        FROM CHICAGO_CRIME
        LIMIT 10;
        """
head_crime = pd.read_sql(first10rows, pconn)
head_crime

#############
# Problem 3 #
#############
# Number of arrests
arrests = """SELECT COUNT(*)
        FROM CHICAGO_CRIME
        WHERE ARREST = 'TRUE';
        """
arrest_count = pd.read_sql(arrests, pconn)
arrest_count

#############
# Problem 4 #
#############
# types of crimes
crimes = """SELECT DISTINCT(PRIMARY_TYPE)
        FROM CHICAGO_CRIME
        WHERE LOCATION_DESCRIPTION = 'GAS STATION';
        """
crime_types = pd.read_sql(crimes, pconn)
crime_types

#############
# Problem 5 #
#############
# census data, letter b
census_area_b = """SELECT *
        FROM CHICAGO_SES
        WHERE COMMUNITY_AREA_NAME LIKE 'B%';
        """
census_subset = pd.read_sql(census_area_b, pconn)
census_subset

#############
# Problem 6 #
#############
# healthy schools
healthy_school = """SELECT NAME_OF_SCHOOL,HEALTHY_SCHOOL_CERTIFIED, COMMUNITY_AREA_NUMBER
        FROM CHICAGO_SCHOOLS
        WHERE COMMUNITY_AREA_NUMBER > 9
        AND COMMUNITY_AREA_NUMBER < 16
        AND HEALTHY_SCHOOL_CERTIFIED = 'Yes';
        """
school_health = pd.read_sql(healthy_school, pconn)
school_health

#############
# Problem 7 #
#############
# safe schools
safe_school = """SELECT AVG(SAFETY_SCORE)
        FROM CHICAGO_SCHOOLS;
        """
school_safety = pd.read_sql(safe_school, pconn)
school_safety

#############
# Problem 8 #
#############
# college enrollment
college_enrollment = """SELECT COMMUNITY_AREA_NAME, AVG(SAFETY_SCORE) as AVG_SAFETY
        FROM CHICAGO_SCHOOLS
        WHERE SAFETY_SCORE IS NOT NULL
        GROUP BY COMMUNITY_AREA_NAME
        ORDER BY AVG_SAFETY DESC
        LIMIT 5;
        """
enrollment = pd.read_sql(college_enrollment, pconn)
enrollment

#############
# Problem 9 #
#############
#  school safety by ca
ca_safety = """SELECT COMMUNITY_AREA_NAME, SAFETY_SCORE
        FROM CHICAGO_SCHOOLS
        WHERE SAFETY_SCORE =
        (SELECT MIN(SAFETY_SCORE) FROM CHICAGO_SCHOOLS);
        """
low_safety_schools = pd.read_sql(ca_safety, pconn)
low_safety_schools

##############
# Problem 10 #
##############
# per capita income, school safety
pci_ss = """SELECT SCH.COMMUNITY_AREA_NAME, SES.PER_CAPITA_INCOME,
        SCH.SAFETY_SCORE
        from CHICAGO_SCHOOLS SCH, CHICAGO_SES SES
        WHERE SCH.COMMUNITY_AREA_NUMBER = SES.COMMUNITY_AREA_NUMBER
        AND SCH.SAFETY_SCORE = 1;
        """
income_by_safety = pd.read_sql(pci_ss, pconn)
print(income_by_safety)
























# in order to display plot within window
# plt.show()
