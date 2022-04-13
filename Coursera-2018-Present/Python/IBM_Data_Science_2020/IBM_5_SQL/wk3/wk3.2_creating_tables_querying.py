#####################################
# Week 3.2: Connect to Db2 database #
#####################################

############################################
# Task 1: Import the ibm_db Python library #
############################################

import ibm_db


########################################################
# Task 2: Identify the database connection credentials #
########################################################

#Replace the placeholder values with the actuals for your Db2 Service Credentials
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_hostname = "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"            # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_port = "50000"                    # e.g. "50000"
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_uid = "bzr25790"                 # e.g. "abc12345"
dsn_pwd = "9nqsnndjss-d342r"                 # e.g. "7dBZ3wWt9XN6$o0J"

##########################################
# Task 3: Create the database connection #
##########################################

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

##########################################
# Task 4: Create a table in the database #
##########################################

#Lets first drop the table INSTRUCTOR in case it exists from a previous attempt
dropQuery = "drop table INSTRUCTOR"

#Now execute the drop statment
dropStmt = ibm_db.exec_immediate(conn, dropQuery)

#Construct the Create Table DDL statement - replace the ... with rest of the statement
createQuery = "create table INSTRUCTOR(id INTEGER PRIMARY KEY NOT NULL, fname VARCHAR(20), lname VARCHAR(20), city VARCHAR(20), ccode VARCHAR(20))"

#Now fill in the name of the method and execute the statement
createStmt = ibm_db.exec_immediate(conn, createQuery)

######################################
# Task 5: Insert data into the table #
######################################

#Construct the query - replace ... with the insert statement
insertQuery = "INSERT INTO INSTRUCTOR (id, fname, lname, city, ccode) VALUES ('1', 'Ahuja', 'Rav', 'Toronto', 'CA');"

#execute the insert statement
insertStmt = ibm_db.exec_immediate(conn, insertQuery)

#replace ... with the insert statement that inerts the remaining two rows of data
insertQuery2 = "INSERT INTO INSTRUCTOR (id, fname, lname, city, ccode) VALUES (2, 'Chong', 'Raul', 'Toronto', 'CA'), (3, 'Vasudevan', 'Hima', 'Chicago', 'US');"

#execute the statement
insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)




































# in order to display plot within window
# plt.show()
