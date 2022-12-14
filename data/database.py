import mysql.connector

try:
    main_db = mysql.connector.connect(host='45.200.120.127',
                                      database='tuxisoft_dms',
                                      user='datamanagmentsystem',
                                      password='y8z1I3^y1')
except mysql.connector.Error as ex:
    print("Error connection from database")

