import streamlit as st

# Set page title
st.set_page_config(page_title="Healthy Food Guide", page_icon="🥗")
st.title("🥗 Healthy Eating Guide")

# 1. Initialize Session State variables
# 'step' tracks where the user is in your 10-step plan
if "step" not in st.session_state:
    st.session_state.step = 1
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. Step 1: Initial Welcome Message
if st.session_state.step == 1:
    with st.chat_message("assistant"):
        st.write("I'm your healthy eating guider. Do you know what is healthy food?")
    
    # User Button to proceed
    if st.button("I like to know it"):
        # Move to the explanation phase
        st.session_state.step = 2
        st.rerun()

# 3. Step 1: The Explanation (Triggered after button press)
if st.session_state.step == 2:
    # Show the previous interaction for context
    with st.chat_message("assistant"):
        st.write("I'm your healthy eating guider. Do you know what is healthy food?")
    with st.chat_message("user"):
        st.write("I like to know it")
        
    # Show the detailed explanation
    with st.chat_message("assistant"):
        st.info("""
        **Healthy food gives your body the nutrients it needs to:**
        * Grow properly
        * Stay energetic
        * Fight diseases
        * Keep your brain sharp
        
        It is natural, balanced, and low in harmful fats, sugar, and salt.
        """)
    
    # Placeholder for Step 2
    st.success("Step 1 Complete! Ready for Step 2?")