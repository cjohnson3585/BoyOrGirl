"""
9/21/20
Web app for interacting with a DB and a voting website
"""
from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
import time
from datetime import datetime
import pandas as pd


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/vote')
def order():
    return render_template("vote.html")

@app.route('/thankyou')
def thankyou():
    query = "SELECT * FROM votes where sex != ''"
    conn = sqlite3.connect('votes.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    results = rows
    tots = int(len(results))
    cur.execute("SELECT * FROM votes where sex in ('boy','Boy','BOY','BOy','bOY')")
    rows2 = cur.fetchall()
    bs = int(len(rows2))
    cur.execute("SELECT * FROM votes where sex in ('girl','Girl','GIRL','GIrl','GIRl','gIRL')")
    rows3 = cur.fetchall()
    gs = int(len(rows3))
    df = pd.read_sql(query, conn)
    print(df)
    bsp = round(float(bs/tots)*100.0,2)
    gsp = round(float(gs/tots)*100.0,2)
    return render_template("thankyou.html",results=results, bs=bs, gs=gs, tots=tots, bsp=bsp, gsp=gsp)

@app.route('/receiver', methods=['GET','POST'])
def receiver():
    default_name = '0'
    fn = request.form.get('fn', default_name)
    ln = request.form.get('ln', default_name)
    sex = request.form.get('sex', default_name)
    loc = request.form.get('loc', default_name)
    sql_edit_insert(''' INSERT INTO votes (first_name, last_name,sex, location) VALUES (?,?,?,?) ''', (fn,ln,sex,loc))
    return "Hello"


def sql_edit_insert(query,var):
    conn = sqlite3.connect('votes.db')
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()


if __name__ == '__main__':
    app.run(debug=True)
