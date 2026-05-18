import streamlit as st

# Set up the page title and icon
st.set_page_config(page_title="My Personal Portfolio", page_icon="🚀", layout="centered")

# --- NAVIGATION TABS ---
# This creates the three tabs you requested at the top of the page
tab1, tab2, tab3 = st.tabs(["🏠 Home", "ℹ️ About Me", "👥 Friends & Family"])

# --- TAB 1: HOME PAGE ---
with tab1:
    st.title("🔥 Welcome to My Portfolio")
    
    # Boldly displays your name
    st.markdown("# **YOUR NAME HERE**")
    st.subheader("AP Computer Science Student")
    
    # Placeholder for your picture
    st.write("---")
    try:
        # Replace 'profile.jpg' with your actual image file name
        st.image("profile.jpg", caption="This is me!", width=300)
    except:
        st.warning("📸 Place your profile picture ('profile.jpg') in the same folder as this script to display it here.")

# --- TAB 2: PERSONAL INFORMATION ---
with tab2:
    st.title("📖 About Me")
    st.write("Here is a bit background about who I am and my journey so far.")
    
    st.markdown("### 📍 Background")
    st.write("**Born:** City, State/Country")
    st.write("**Current Location:** City, State")
    
    st.markdown("### 🎓 Education")
    st.write("**High School:** [Your High School Name]")
    st.write("**Expected Graduation:** 202X")
    st.write("**Favorite Classes:** AP Computer Science, [Other Class]")
    
    st.markdown("### 🚀 Interests & Hobbies")
    st.write("- Coding and technology")
    st.write("- [Add your hobby here]")
    st.write("- [Add another hobby here]")

# --- TAB 3: FRIENDS & FAMILY ---
with tab3:
    st.title("❤️ Friends & Family")
    st.write("The people who support me and keep me going!")
    
    # Creating a grid layout for your photos
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            st.image("family.jpg", caption="My Family", use_container_width=True)
        except:
            st.info("🖼️ Add 'family.jpg' to your folder to show your family photo here.")
            
    with col2:
        try:
            st.image("friends.jpg", caption="My Friends", use_container_width=True)
        except:
            st.info("🖼️ Add 'friends.jpg' to your folder to show your friends photo here.")