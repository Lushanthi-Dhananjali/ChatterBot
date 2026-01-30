import streamlit as st

st.set_page_config(page_title="Healthy Food Guide", page_icon="🥗")
st.title("🥗 Healthy Eating Guide")

# Initialize Session State
if "step" not in st.session_state:
    st.session_state.step = 1

# --- STEP 1: WELCOME ---
if st.session_state.step == 1:
    with st.chat_message("assistant"):
        st.write("I'm your healthy eating guider. Do you know what is healthy food?")
    
    if st.button("I like to know it"):
        st.session_state.step = 2
        st.rerun()

# --- STEP 1: EXPLANATION ---
if st.session_state.step == 2:
    with st.chat_message("assistant"):
        st.info("""
        **Healthy food gives your body the nutrients it needs to:**
        * Grow properly
        * Stay energetic
        * Fight diseases
        * Keep your brain sharp
        
        It is natural, balanced, and low in harmful fats, sugar, and salt.
        """)
    
    # Step 2 Trigger Question
    with st.chat_message("assistant"):
        st.write("Are you like get knowlege of type of healthy food?")
    
    if st.button("Yes i like"):
        st.session_state.step = 3
        st.rerun()

# --- STEP 2: TYPES OF HEALTHY FOOD ---
if st.session_state.step == 3:
    # We display the previous definition and question for flow
    with st.chat_message("assistant"):
        st.write("Are you like get knowlege of type of healthy food?")
    with st.chat_message("user"):
        st.write("Yes i like")

    with st.chat_message("assistant"):
        st.markdown("""
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
        * **Examples:** * *Animal:* Fish, eggs, milk, chicken
            * *Plant:* Lentils, beans, nuts
        * **Benefits:** Builds muscles, repairs body tissues, strengthens immunity

        ### 🥑 Healthy Fats
        * **Examples:** Nuts, seeds, avocado, olive oil
        * **Benefits:** Good for heart and brain, helps absorb vitamins
        """)
    
    st.success("Step 2 Complete! Ready for Step 3?")