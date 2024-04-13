#!/usr/bin/env python3

"""Module that lists all states from the hbtn_0e_0_usa database,
   handling potential errors and providing user-friendly output."""

import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials and search name from command-line arguments
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
    except IndexError:
        print("Error: Missing required arguments.")
        sys.exit(1)

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database)
        c = db.cursor()
    except MySQLdb.Error as err:
        print("Error connecting to MySQL database:", err)
        sys.exit(1)

    # Execute the SQL query with parameterized query for security
    try:
        query = "SELECT * FROM `states` WHERE BINARY `name` = %s"
        c.execute(query, (sys.argv[4],))
    except MySQLdb.Error as err:
        print("Error executing query:", err)
        db.close()  # Close connection on error
        sys.exit(1)

    # Fetch all rows and print states in a formatted way
    states = c.fetchall()
    if not states:
        print("No states found for the given name.")
    else:
        for state in states:
            print(state[0])  # Print state names only

    # Close the connection
    db.close()

