import streamlit as st

import streamlit as st

# --- Define Pages ---
home_page = st.Page("views/Home.py", title="Home", icon="", default=True)
culture_page = st.Page("views/Culture.py", title="Culture", icon="")
tourism_page = st.Page("views/tourism.py", title="Tourism", icon="")
art_page = st.Page("views/plan.py", title="Art", icon="")
heritage_page = st.Page("views/heritage.py", title="Heritage", icon="")

# --- Navigation Setup ---
pg = st.navigation({
    "Explore India": [home_page, culture_page, tourism_page, art_page, heritage_page]
})



# --- Shared Header / Sidebar ---
st.set_page_config(page_title="Incredible India", layout="wide")
st.logo("assets/taj.jpeg")  # Optional: You can use an Indian tourism logo
st.sidebar.markdown("Made with ❤️ for the Hackathon by **Gururagavendra**")

# --- Run the App ---
pg.run()