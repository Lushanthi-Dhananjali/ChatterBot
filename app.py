import streamlit as st

# 1. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your healthy eating guide. Would you like a recipe for Breakfast, Lunch, or Dinner?"}
    ]

st.title("🥗 Healthy Eating Guide")

# 2. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 3. Create Buttons for Quick Selection
st.write("Quick Options:")
col1, col2, col3 = st.columns(3)

def handle_click(choice):
    # Add user choice to history
    st.session_state.messages.append({"role": "user", "content": choice})
    # Add bot response (In next step, we will fetch this from MySQL)
    response = f"Great choice! Here is a healthy {choice} suggestion..."
    st.session_state.messages.append({"role": "assistant", "content": response})

if col1.button("Breakfast"):
    handle_click("Breakfast")
    st.rerun() # Refresh to show new messages

if col2.button("Lunch"):
    handle_click("Lunch")
    st.rerun()

if col3.button("Dinner"):
    handle_click("Dinner")
    st.rerun()

# 4. Regular Chat Input
if prompt := st.chat_input("Or ask me anything else..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Placeholder for AI/Database response
    with st.chat_message("assistant"):
        st.write("I am looking that up in my database for you...")