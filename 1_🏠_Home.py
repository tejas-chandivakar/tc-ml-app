import streamlit as st
import pathlib

st.set_page_config(
    page_title="TC Website",
    page_icon="🌺",
    layout="wide"
)


st.title("Main Page")
st.divider()
st.sidebar.success("Select a page above.")

st.button("Click Me!", key="green")
st.button("Click", key="blue")

pc_Made = ['HP', 'DELL', 'ASUS', 'LENOVO', 'MSI', 'MAC']

# Dropdown menu
selected_pc = st.selectbox("Choose your PC brand:", pc_Made, help="Select your computer brand from the list")

# Display selected value
st.write(f"✅ You selected: **{selected_pc}**")

st.title("🎚️ Slider Demo with Help Icon")
# Slider with help text
age = st.slider(
    "Select your age:",
    min_value=10,
    max_value=80,
    value=25,
    step=1,
    help="Use this slider to choose your age (between 10 and 80)."
)

st.write(f"🧑 Your selected age is: **{age}** years old.")








# Function to Load CSS from the 'assets' folder
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

# Load the external CSS
css_path = pathlib.Path("assets/styles.css")
load_css(css_path)
