import streamlit as st

st.set_page_config(page_title="Healthy Food Guide", page_icon="🥗")
st.title("🥗 Healthy Eating Guide")

# 1. Initialize the Message History and Step Counter
if "messages" not in st.session_state:
    st.session_state.messages = []
if "step" not in st.session_state:
    st.session_state.step = 1

# 2. Function to display all saved messages in the UI
# This ensures that every time the script reruns, previous chats stay visible
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --- LOGIC FOR STEP 1 ---
if st.session_state.step == 1:
    # Bot asks the first question
    welcome_text = "I'm your healthy eating guider. Do you know what is healthy food?"
    with st.chat_message("assistant"):
        st.write(welcome_text)
    
    if st.button("I like to know it"):
        # Save the interaction to history
        st.session_state.messages.append({"role": "assistant", "content": welcome_text})
        st.session_state.messages.append({"role": "user", "content": "I like to know it"})
        
        # Move to Step 2
        st.session_state.step = 2
        st.rerun()

# --- LOGIC FOR STEP 2 ---
elif st.session_state.step == 2:
    explanation = """
    **Healthy food gives your body the nutrients it needs to:**
    * Grow properly
    * Stay energetic
    * Fight diseases
    * Keep your brain sharp
    
    It is natural, balanced, and low in harmful fats, sugar, and salt.
    """
    question_2 = "Are you like get knowlege of type of healthy food?"
    
    with st.chat_message("assistant"):
        st.info(explanation)
        st.write(question_2)
    
    if st.button("Yes i like"):
        # Save this explanation and question to history
        st.session_state.messages.append({"role": "assistant", "content": explanation})
        st.session_state.messages.append({"role": "assistant", "content": question_2})
        st.session_state.messages.append({"role": "user", "content": "Yes i like"})
        
        # Move to Step 3
        st.session_state.step = 3
        st.rerun()

# --- LOGIC FOR STEP 3 (The Types List) ---
elif st.session_state.step == 3:
    types_info = """
    ### 🍎 Fruits
    * **Examples:** Apple, banana, orange, papaya, mango
    * **Benefits:** Rich in vitamins & fiber, improves digestion, boosts immunity

    ### 🥦 Vegetables
    * **Examples:** Carrot, spinach, broccoli, beans
    * **Benefits:** Good for eyes, skin, and blood, prevents diseases, low in calories

    ### 🌾 Whole Grains
    * **Examples:** Brown rice, oats, whole-wheat bread
    * **Benefits:** Gives long-lasting energy, good for digestion, controls blood sugar

    ### 🍗 Protein Foods
    * **Examples:** Animal (Fish, eggs), Plant (Lentils, beans)
    * **Benefits:** Builds muscles, repairs body tissues, strengthens immunity

    ### 🥑 Healthy Fats
    * **Examples:** Nuts, seeds, avocado, olive oil
    * **Benefits:** Good for heart and brain, helps absorb vitamins
    """
    
    with st.chat_message("assistant"):
        st.markdown(types_info)
    
    # Save to history so it stays when you move to Step 4
    st.session_state.messages.append({"role": "assistant", "content": types_info})
    
    st.success("Steps 1 & 2 are complete and saved in history!")