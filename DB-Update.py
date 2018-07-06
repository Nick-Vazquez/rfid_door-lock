#!/usr/bin/python2
# Import all necessary libraries and set the pymysql mode
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

# Ask for input from the user for the card UID that would have been scanned
user = input('What UID did we recieve?: ')

# Connect to the MySQL database
# Host is usually 'localhost'
db = MySQLdb.connect("host", "username", "password", "database")

# Set the cursor variable
cursor = db.cursor()

# Query the DB for the user that is attached to the tag that was scanned (Entered for now)
cursor.execute("SELECT ID FROM status WHERE RFIDTag = %s;", (user))

# Set the result variable to the output from the Query
result = (cursor.fetchone())

# Execute an Update Query
cursor.execute("UPDATE status SET Status = IF(Status = 'IN', 'OUT', 'IN') WHERE ID = %s;", (result))

# Commit the Update Query with db.commit()
db.commit()

# Close the DB connection
db.close()

# Print All Done to inform the user of the change
print("All Done!")
