import psycopg2
from flask import Flask, render_template, json, request, redirect, url_for, flash, jsonify
from sql import *

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


@app.route('/')
@app.route('/category')
def showCategory():
    cur.execute(select_order)
    row = cur.fetchall()
    return render_template('index.html', value=row)


"""
# <int:category_id>/
@app.route('/category')
def showItems(category_id):
    cur.execute("select * from ama_order_export")
    items = cur.fetchall()
    #cur.execute("SELECT * FROM category WHERE id="+category_id)
    #category = cur.fetchone()
    #items = cur.fetchall()
    return render_template('items.html')
"""


if __name__ == "__main__":
    app.run(port=5002)
