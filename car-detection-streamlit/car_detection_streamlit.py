import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

def object_detection(image, confidence):
    # Detect objects in the image with the specified confidence level using Faster R-CNN
    bbox, label, conf = cv.detect_common_objects(image, model='faster_rcnn', confidence=confidence)

    # Create a copy of the original image to draw rectangles and apply effect of highlight
    highlighted_image = np.copy(image)

    # Draw rectangles around the detected objects using draw_bbox() function
    output = draw_bbox(highlighted_image, bbox, label, conf)

    return output, label.count('car')

def main():
    st.title("Détection de voitures")

    # Upload image file
    uploaded_file = st.file_uploader("Choisir une image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read uploaded image
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Check if the image contains cars
        bbox, label, conf = cv.detect_common_objects(image, model='yolov3')
        if 'car' not in label:
            st.error("L'image ne contient pas de voiture.")
            return

        # Display original image
        st.subheader("Image originale")
        st.image(image, channels="BGR")

        # Confidence level slider
        confidence = st.slider("Niveau de confiance", 0.0, 1.0, 0.5, 0.05)

        if st.button("Détecter les voitures"):
            # Perform object detection
            output, car_count = object_detection(image, confidence)

            # Display image with detected objects
            st.subheader(f"Voitures détectées ({car_count} voitures)")
            st.image(output, channels="BGR")

if __name__ == "__main__":
    main()
