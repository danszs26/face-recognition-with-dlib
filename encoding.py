import face_recognition
import os
import numpy as np
import math

# Helper
def face_confidence(face_distance, face_match_threshold=0.5):
    range = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'

class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True

    def __init__(self):
        self.encode_faces()

    def encode_faces(self):
        # Create an empty list to hold the face encodings
        known_face_encodings = []

        # Create an empty list to hold the names of the people you want to recognize
        known_face_names = []

        # Loop through the subdirectories in the main directory
        path = 'wajah1/'
        
        for subdir in os.listdir(path):

            # Get the name of the person from the subdirectory name
            name = subdir.split('/')[-1]
            print('Processing images for:', name)

            # Loop through the images in the subdirectory
            for filename in os.listdir(os.path.join(path, subdir)):
                # Load the image
                image = face_recognition.load_image_file(os.path.join(path, subdir, filename))

                # Get the face encoding for the image
                face_encoding = face_recognition.face_encodings(image)[0]

                # Add the face encoding to the list of known face encodings
                known_face_encodings.append(face_encoding)

                # Add the name of the person to the list of known face names
                known_face_names.append(name)

        # Save known_face_encodings and known_face_names to npy files
        np.save('known_face_encodings.npy', known_face_encodings)
        np.save('known_face_names.npy', known_face_names)

# Run the encoding function
if __name__ == '__main__':
    fr = FaceRecognition()
