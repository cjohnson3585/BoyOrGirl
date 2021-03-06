"""
8/14/20
Funtion to creat sqlite dbs for testing purposes along with test functions.
"""
import os
import sqlite3
import pandas as pd



# Clear example.db if it exists
if not os.path.exists('votes.db'):

# Create a database
    conn = sqlite3.connect('votes.db')

# Add the data to our database
    data_url = [['Chris','Johnson','boy','Baltimore']]
#    headers = ['first_name','last_name','school','degree','field','year','current_employer','job_title','user_name','contact','password','location']
    headers = ['first_name','last_name','sex','location']
    data_table = pd.DataFrame(data=data_url, columns=headers, index=None)
    data_table.to_sql('votes', conn, dtype={
    'first_name':'VARCHAR(256)',
    'last_name':'VARCHAR(256)',
    'sex':'VARCHAR(10)',
    'location':'VARCHAR(256)'},
    index =False)

else:
    conn = sqlite3.connect('votes.db')

conn.row_factory = sqlite3.Row

# Make a convenience function for running SQL queries
def sql_query(query):
    conn = sqlite3.connect('votes.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    df = pd.read_sql(query, conn)
    return df

def authenticate(query,var):
    print(query, var)
    conn = sqlite3.connect('accounts.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    for rw in rows:
        print(rw['user_name'], rw['password'])
    return rows

def sql_edit_insert(query,var):
    conn = sqlite3.connect('accounts.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    conn = sqlite3.connect('accounts.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows

def sql_disconnect():
    conn.close()    

#f = sql_query("SELECT * FROM votes")
print(sql_query("SELECT * FROM votes"))