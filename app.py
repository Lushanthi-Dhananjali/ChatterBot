import streamlit as st
import mysql.connector

# --- CONFIGURATION ---
st.set_page_config(page_title="Healthy Food Guide", page_icon="🥗")
st.title("🥗 Healthy Eating Guide")

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
if "step" not in st.session_state:
    st.session_state.step = 1

# --- DATABASE CONNECTION FUNCTIONS ---

def get_db_connection():
    # Credentials must be in .streamlit/secrets.toml
    return mysql.connector.connect(**st.secrets["mysql"])

def fetch_categories():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM food_categories")
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        return f"Database error: {e}"

def fetch_food_list(category):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT food_name FROM recipes WHERE category = %s", (category,))
        foods = [row[0] for row in cursor.fetchall()]
        conn.close()
        return foods
    except Exception as e:
        return [f"Database error: {e}"]

# --- DISPLAY SAVED HISTORY (Continual Chat) ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --- STEP 1: WELCOME ---
if st.session_state.step == 1:
    welcome_q = "I'm your healthy eating guider. Are you know what is healthy food?"
    with st.chat_message("assistant"):
        st.write(welcome_q)
    
    if st.button("I like to know it"):
        ans1 = """Healthy food gives your body the nutrients it needs to grow properly, 
        stay energetic, fight diseases, and keep your brain sharp."""
        st.session_state.messages.append({"role": "assistant", "content": welcome_q})
        st.session_state.messages.append({"role": "user", "content": "I like to know it"})
        st.session_state.messages.append({"role": "assistant", "content": ans1})
        st.session_state.step = 2
        st.rerun()

# --- STEP 2: CATEGORY KNOWLEDGE ---
elif st.session_state.step == 2:
    q2 = "Are you like get knowlege of type of healthy food?"
    with st.chat_message("assistant"):
        st.write(q2)
    
    if st.button("Yes i like"):
        cat_data = fetch_categories()
        if isinstance(cat_data, list):
            full_info = ""
            for item in cat_data:
                full_info += f"### {item['category_name']}\n"
                full_info += f"* **Examples:** {item['examples']}\n"
                full_info += f"* **Benefits:** {item['benefits']}\n\n"
        else:
            full_info = cat_data 

        st.session_state.messages.append({"role": "assistant", "content": q2})
        st.session_state.messages.append({"role": "user", "content": "Yes i like"})
        st.session_state.messages.append({"role": "assistant", "content": full_info})
        st.session_state.step = 3
        st.rerun()

# --- STEP 3: MEAL SELECTION ---
elif st.session_state.step == 3:
    question_3 = "Would like get idea about healthy food recipe for Breakfast, Lunch or Dinner?"
    with st.chat_message("assistant"):
        st.write(question_3)

    col1, col2, col3 = st.columns(3)
    choice = None
    if col1.button("Breakfast"): choice = "Breakfast"
    if col2.button("Lunch"): choice = "Lunch"
    if col3.button("Dinner"): choice = "Dinner"

    if choice:
        food_list = fetch_food_list(choice)
        list_msg = f"**{choice} List:**\n" + "\n".join([f"* {f}" for f in food_list])
        
        st.session_state.messages.append({"role": "assistant", "content": question_3})
        st.session_state.messages.append({"role": "user", "content": choice})
        st.session_state.messages.append({"role": "assistant", "content": list_msg})
        st.session_state.step = 4
        st.rerun()

# --- STEP 4: ASK FOR SPECIFIC FOOD ---
elif st.session_state.step == 4:
    question_4 = "Would you like to know why a specific food from the list is healthy? Type the food name below!"
    with st.chat_message("assistant"):
        st.write(question_4)

    if user_food := st.chat_input("Type a food name (e.g., Oats, Salmon)..."):
        st.session_state.messages.append({"role": "assistant", "content": question_4})
        st.session_state.messages.append({"role": "user", "content": user_food})
        
        # Save the input to session state for Step 5 to use
        st.session_state.selected_food = user_food
        st.session_state.step = 5
        st.rerun()

# --- STEP 5: PLACEHOLDER ---
elif st.session_state.step == 5:
    with st.chat_message("assistant"):
        st.write(f"I am now searching for information about: **{st.session_state.selected_food}**")