import streamlit as st

# Page Config
st.set_page_config(
    page_title="Making Machines See",
    page_icon="👁️",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("👁️ Making Machines See")
st.caption("CBSE AI Notes • Interactive • Quick Revision")

# ---------------- CHIPS ----------------
st.markdown("""
<style>
.chip{
display:inline-block;
padding:8px 14px;
margin:4px;
border-radius:20px;
background-color:#262730;
color:white;
font-size:14px;
font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="chip">Computer Vision</div>
<div class="chip">Pixels</div>
<div class="chip">Grayscale</div>
<div class="chip">Image Processing</div>
<div class="chip">AI</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📘 Overview",
    "🧠 Concepts",
    "⚙️ Process",
    "🌍 Applications",
    "🎯 Quiz"
])

# ---------------- OVERVIEW ----------------
with tab1:
    st.header("📘 What is Making Machines See?")
    
    st.write("""
Computer Vision is a branch of AI that helps machines understand images and videos.

### 📌 Real-life Examples
- Face Unlock 📱
- Self-driving Cars 🚗
- CCTV Surveillance 📹
- Medical Scanning 🏥
""")

# ---------------- CONCEPTS ----------------
with tab2:
    st.header("🧠 Key Concepts")

    st.subheader("🟦 Pixel")
    st.write("""
- Smallest unit of an image
- Images are made of thousands of pixels
- Pixel values range from 0 to 255
""")

    st.subheader("⚫ Grayscale")
    st.write("""
Why convert images to grayscale?
- Reduces complexity
- Faster processing
- Focuses on structure instead of color
""")

    st.info("0 = Black ⚫ | 255 = White ⚪")

# ---------------- PROCESS ----------------
with tab3:
    st.header("⚙️ Image Processing Steps")

    st.write("""
### 1️⃣ Input Image
Machine receives image

### 2️⃣ Preprocessing
Resize / Grayscale / Noise Removal

### 3️⃣ Feature Extraction
Detect shapes, edges, patterns

### 4️⃣ Classification
Machine identifies object
""")

# ---------------- APPLICATIONS ----------------
with tab4:
    st.header("🌍 Applications")

    col1, col2 = st.columns(2)

    with col1:
        st.success("📱 Face Recognition")
        st.success("🚗 Autonomous Vehicles")
        st.success("🛒 Smart Shopping")

    with col2:
        st.success("🏥 Medical Imaging")
        st.success("📷 Camera Filters")
        st.success("🔒 Security Systems")

# ---------------- QUIZ ----------------
with tab5:
    st.header("🎯 Quick Quiz")

    q1 = st.radio(
        "1. What is the smallest unit of an image?",
        ["Bit", "Pixel", "Byte"]
    )

    if q1 == "Pixel":
        st.success("Correct 🎉")
    elif q1:
        st.error("Incorrect 😅")

    q2 = st.radio(
        "2. Why do we use grayscale images?",
        [
            "To simplify processing",
            "To increase colors",
            "To make images bigger"
        ]
    )

    if q2 == "To simplify processing":
        st.success("Correct 👍")
    elif q2:
        st.error("Try again 🤔")

    q3 = st.radio(
        "3. Which field helps machines understand images?",
        ["Cyber Security", "Computer Vision", "Networking"]
    )

    if q3 == "Computer Vision":
        st.success("Nice Work 🚀")
    elif q3:
        st.error("Oops!")

# ---------------- FOOTER ----------------
st.divider()
st.caption("🔥 CBSE AI Notes App • Making Machines See")
