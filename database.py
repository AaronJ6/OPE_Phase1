# This file contains the functions to connect to the database and execute queries
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    # connecting to the database
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWORD"),
        database=os.getenv("DATABASE")
    )
    return connection

def execute_query(query):
    connection = get_connection()
    cursor = connection.cursor()
    #execute and return result
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    #make an array of dictionaries from the result
    result = [dict(zip([key[0] for key in cursor.description], row)) for row in result]
    
    return result

