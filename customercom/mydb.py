import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Damibillionaire1)'

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE customer_app")

print('ready now!')