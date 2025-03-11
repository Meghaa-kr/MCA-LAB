import streamlit as st
from helper import summarize_text, summarize_pdf, summarize_webpage

# Set page config with a dark theme-like appearance
st.set_page_config(page_title="Text Summarizer", page_icon="📝", layout="wide")

# Custom CSS for a modern, attractive color theme with proper visibility
st.markdown(
    """
    <style>
    body {
        background-color: #0F0F1E;
        color: #FFFFFF;
    }
    .stApp {
        background: linear-gradient(135deg, #1E1E2F, #2E2E3F);
    }
    .css-1d391kg, .css-1dbjc4n, .css-18e3th9 {
        background-color: #2E2E3F !important;
        color: #FF6F61 !important;
    }
    .stTextInput, .stTextArea, .stFileUploader, .stButton>button {
        background-color: #3E3E4F !important;
        color: #FFFFFF !important;  /* Changed to white for better visibility */
        border-radius: 15px;
        border: 2px solid #FF6F61;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #FF6F61 !important;
        color: #FFFFFF !important;
    }
    .stSidebar {
        background-color: #1E1E2F;
    }
    .stSidebar .sidebar-content {
        background-color: #1E1E2F !important;
        color: #FFFFFF !important;  /* Ensure sidebar text is visible */
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #FF6F61;
    }
    .stMarkdown p {
        color: #FFFFFF;  /* Ensure paragraph text is visible */
    }
    .stSpinner div {
        color: #FF6F61 !important;
    }
    .stDownloadButton>button {
        background-color: #FF6F61 !important;
        color: #FFFFFF !important;
        border-radius: 15px;
        border: 2px solid #FF6F61;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stDownloadButton>button:hover {
        background-color: #FF3B2F !important;
        border-color: #FF3B2F;
    }
    /* Ensure input labels and text are visible */
    .stTextInput label, .stTextArea label, .stFileUploader label {
        color: #FFFFFF !important;
    }
    /* Ensure radio button text is visible */
    .stRadio label {
        color: #FFFFFF !important;
    }
    /* Ensure warning messages are visible */
    .stWarning {
        color: #FF6F61 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📄 AI-Powered Text Summarizer")
st.markdown("<p style='color:#FF6F61; font-size:18px;'>Summarize <b>Text, PDFs, and Webpages</b> effortlessly using AI!</p>", unsafe_allow_html=True)

# Sidebar for options
st.sidebar.header("⚙️ Choose Input Type")
option = st.sidebar.radio("Select an option:", ["Text", "PDF", "URL"])
summary = ""

if option == "Text":
    user_text = st.text_area("✍️ Enter text to summarize:", height=200)
    
    if st.button("🔍 Summarize Text"):
        if user_text.strip():
            with st.spinner("🔄 Summarizing... Please wait."):
                summary = summarize_text(user_text)
            st.subheader("📌 Summary")
            st.write(summary)
        else:
            st.warning("⚠️ Please enter some text.")

elif option == "PDF":
    uploaded_pdf = st.file_uploader("📂 Upload a PDF file", type=["pdf"])
    
    if uploaded_pdf and st.button("🔍 Summarize PDF"):
        with st.spinner("🔄 Extracting and Summarizing... Please wait."):
            summary = summarize_pdf(uploaded_pdf)
        st.subheader("📌 Summary")
        st.write(summary)

elif option == "URL":
    url = st.text_input("🌐 Enter webpage URL:")
    
    if st.button("🔍 Summarize Webpage"):
        if url.strip():
            with st.spinner("🔄 Fetching and Summarizing... Please wait."):
                summary = summarize_webpage(url)
            st.subheader("📌 Summary")
            st.write(summary)
        else:
            st.warning("⚠️ Please enter a valid URL.")

# Allow users to download the summary as a text file
if summary:
    st.download_button(label="📥 Download Summary", data=summary, file_name="summary.txt", mime="text/plain")