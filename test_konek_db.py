#!/usr/bin/python3

import os #library yang berhubungan dengan OS, misalnya path
import json #library untuk membaca json
import psycopg2 #library untuk postgreSQL

if __name__ == '__main__':
    path = os.getcwd() #untuk mendapatkan path direktory
    with open(path+'/'+'config.json') as file:
        conf = json.load(file)['postgresql']
    
    try:
        conn = psycopg2.connect(host="localhost",
                                database="digitalskola",
                                user="postgres",
                                password=12345
                                )
        print(f"[INFO] Success connect to PostgreSQL")
    except:
        print(f"[INFO] Can't connect to PostgreSQL")
