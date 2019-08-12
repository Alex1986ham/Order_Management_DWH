import psycopg2
import csv
from flask import Flask, render_template, json, request, redirect, url_for, flash, jsonify
import os
import glob

app = Flask(__name__)

try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=dwh user=postgres password=Dudko$010914")
    print("1. works")
except psycopg2.Error as e:
    print("Error")
    print(e)

try:
    cur = conn.cursor()
    print("2. cursor works")
except psycopg2.Error as e:
    print("Error")
    print(e)

conn.set_session(autocommit=True)


# Rename File in Directory
os.chdir('C:\\Users\\D&D\\Udacity\\Data_Engineer3\\Data_Engineer\\Postgres_DWH\\data')
i=1
for file in os.listdir():
    src=file
    dst="1"+".txt"
    os.rename(src,dst)
    i+=1


# Insert txt File into Database
try:
    with open('C:\\Users\\D&D\\Udacity\\Data_Engineer3\\Data_Engineer\\Postgres_DWH\\data\\1.txt', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader) # skip the header row
        for row in reader:
            cur.execute(
            "INSERT INTO dwh.public.ama_order_export25 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            row
            #print(row)
            )
        print("success")
except psycopg2.Error as e:
    print("Error")
    print(e)

# Removing the txt file
os.remove('C:\\Users\\D&D\\Udacity\\Data_Engineer3\\Data_Engineer\\Postgres_DWH\\data\\1.txt')
