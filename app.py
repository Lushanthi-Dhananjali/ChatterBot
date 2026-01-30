import streamlit as st
from database_utils import fetch_foods_by_category, fetch_food_details

st.title(" Healthy Eating Guide")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your healthy eating guide. Would you like a recipe for Breakfast, Lunch, or Dinner?"}
    ]

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --- BUTTON SECTION ---
st.write("### Choose a category:")
cols = st.columns(3)
categories = ["Breakfast", "Lunch", "Dinner"]

for i, cat in enumerate(categories):
    if cols[i].button(cat):
        foods = fetch_foods_by_category(cat)
        food_list_str = ", ".join(foods)
        
        # Add to chat
        st.session_state.messages.append({"role": "user", "content": cat})
        bot_msg = f"For {cat}, you can try: **{food_list_str}**. \n\nGive me any food name from the list above, and I can briefly explain why it is suitable!"
        st.session_state.messages.append({"role": "assistant", "content": bot_msg})
        st.rerun()

# --- CHAT INPUT SECTION ---
if prompt := st.chat_input("Ask me about a specific food..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Check database for the food
    detail = fetch_food_details(prompt)
    
    if detail:
        if detail['is_healthy']:
            response = f" **{prompt}** is great! {detail['description']}"
        else:
            response = f" **{prompt}** is not considered a healthy food. {detail['description']}"
    else:
        response = " I'm sorry, I can't find that food in my database. Try asking about items in the lists above!"

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()