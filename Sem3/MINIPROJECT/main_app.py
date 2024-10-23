import numpy as np
import streamlit as st
import cv2
from keras.models import load_model

# Load the trained model
model = load_model('my_model.h5')

# Name of Classes
CLASS_NAMES = ['Scottish Deerhound', 'Maltese Dog', 'Bernese Mountain Dog']

# Fun facts about breeds
BREED_FACTS = {
    'Scottish Deerhound': [
        "Did you know? Scottish Deerhounds can reach up to 32 inches in height!",
        "These dogs were once used as royal hunting dogs in Scotland.",
        "They are known for their gentle and friendly demeanor."
    ],
    'Maltese Dog': [
        "Maltese dogs were favored by royalty in ancient times!",
        "They can live up to 15 years or more with proper care.",
        "These dogs are known for their playful and affectionate nature."
    ],
    'Bernese Mountain Dog': [
        "Bernese Mountain Dogs are great family pets due to their calm temperament.",
        "They were originally bred for farm work in the Swiss Alps.",
        "Their thick fur keeps them warm in cold weather."
    ]
}

# Custom CSS for enhancing the style
st.markdown(
    """
    <style>
    .stApp {
        background-color: #d4edda; /* Soft green background color */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    }
    .stButton>button {
        color: white;
        background-color: #FF4500; /* Bright orange button */
        border: none;
        border-radius: 12px;
        padding: 10px 24px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FF6347; /* Darker orange on hover */
    }
    h1 {
        font-family: 'Pacifico', cursive; /* Custom playful font */
        font-size: 4em; 
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5); /* Shadow effect for the title */
    }
    h3 {
        color: #4682b4; /* Steel blue for subtitles */
        text-align: center;
    }
    .stImage {
        border: 2px solid #4682b4; /* Border around uploaded images */
        border-radius: 15px;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Setting Title of App
st.title("🐕🐕 Dog Breed Prediction App 🐕🐕")
st.markdown("Upload an image of your dog to identify its breed!")

# Uploading the dog image
dog_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
submit = st.button('Predict')

# Confidence threshold for prediction
CONFIDENCE_THRESHOLD = 0.5  # Adjust this value based on your testing

# On predict button click
if submit:
    if dog_image is not None:
        # Convert the file to an OpenCV image
        file_bytes = np.asarray(bytearray(dog_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        # Displaying the image
        st.image(opencv_image, channels="BGR", caption="Uploaded Image", use_column_width=True)

        # Preprocessing the image
        opencv_image = cv2.resize(opencv_image, (224, 224))
        opencv_image = opencv_image / 255.0  # Normalize the image
        opencv_image.shape = (1, 224, 224, 3)  # Convert image to 4D tensor

        # Make Prediction
        Y_pred = model.predict(opencv_image)

        predicted_class_index = np.argmax(Y_pred)
        confidence = np.max(Y_pred)

        # Check if image is valid (above confidence threshold)
        if confidence >= 0.91:  # Confidence is above 91%
            st.warning("**Prediction:** Unidentified - The image does not match any known breed.")
        elif confidence >= CONFIDENCE_THRESHOLD:
            breed_name = CLASS_NAMES[predicted_class_index]
            st.success(f"**Prediction:** {breed_name}")

            # Play bark sound using the markdown approach
            audio_file_path = "C:\\Users\\megha\\Downloads\\app\\Dog Breed Prediction Streamlit App\\mixkit-happy-puppy-barks-741.wav" # Ensure this path is correct
            st.markdown(f'<audio controls src="{audio_file_path}"></audio>', unsafe_allow_html=True)

            # Display multiple fun facts
            st.markdown("### Fun Facts:")
            facts = BREED_FACTS[breed_name]
            for fact in facts:
                st.markdown(f"- {fact}")
        else:
            st.error("Prediction: **Invalid - The image does not match any known breed.**")
    else:
        st.error("Please upload an image to classify.")
