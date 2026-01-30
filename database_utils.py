import mysql.connector
import streamlit as st

def get_db_connection():
    # Using secrets.toml for safety
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )

def fetch_foods_by_category(category):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT food_name FROM recipes WHERE category = %s", (category,))
    results = cursor.fetchall()
    conn.close()
    return [row['food_name'] for row in results]

def fetch_food_details(food_name):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    # Search for the food name
    cursor.execute("SELECT description, is_healthy FROM recipes WHERE food_name LIKE %s", (f"%{food_name}%",))
    result = cursor.fetchone()
    conn.close()
    return result