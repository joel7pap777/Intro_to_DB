#!/usr/bin/python3
"""Creates the database alx_book_store in a MySQL server."""

import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)

finally:
    try:
        cursor.close()
        db.close()
    except Exception:
        pass
