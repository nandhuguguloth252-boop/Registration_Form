import streamlit as st
import sqlite3
import pandas as pd
###################################################

conn=sqlite3.connect("student1.db",check_same_thread=False)
cursor=conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS student1(eid integer,name text PRIMARY KEY,phone integer,password text)""")
conn.commit()
#######################################################
menu=["LOGIN","REGISTER"]
choice=st.sidebar.selectbox("MENU",menu)
if choice=="REGISTER":
    eid=st.number_input("ID")
    name=st.text_input("USERNAME")
    phone=st.number_input("PHONE_NO")
    password=st.text_input("PASSWORD",type="password")
    if st.button("REGISTER"):
        cursor.execute("""INSERT INTO student1(eid,name,phone,password)VALUES(?,?,?,?)""",(eid,name,phone,password))
        conn.commit()
        st.snow()
        st.success("STUDENT ADDED SUCCESSFULLY")
##########################################################
    
if choice=="LOGIN":
    name=st.text_input("USERNAME")
    password=st.text_input("PASSWORD",type="password")
    if st.button("LOGIN"):
        cursor.execute("""SELECT*FROM student1 WHERE
        name=? AND password=?""",(name,password))
        result=cursor.fetchone()
        if result:
            st.success("valid user")
        else:
            st.error("Invalid")
