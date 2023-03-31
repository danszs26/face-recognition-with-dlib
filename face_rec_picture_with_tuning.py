import face_recognition
import cv2
import numpy as np

from encoding import face_confidence

class FaceRecognition:
    def __init__(self):
        # Load the known face encodings and names
        self.known_face_encodings = np.load('known_face_encodings.npy')
        self.known_face_names = np.load('known_face_names.npy')

    def run_recognition(self, image_path, result_path):
        # Load the image
        image = cv2.imread('test_images/rizqi_03.jpg')

        # Resize the image for faster face recognition processing
        small_image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_image = small_image[:, :, ::-1]

        # Find all the faces and face encodings in the current image
        face_locations = face_recognition.face_locations(rgb_small_image, number_of_times_to_upsample=2)
        face_encodings = face_recognition.face_encodings(rgb_small_image, face_locations, num_jitters=5)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=0.4)
            name = "Unknown"
            confidence = '???'

            # Calculate the shortest distance to face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)

            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
                confidence = face_confidence(face_distances[best_match_index])

            face_names.append(f'{name} ({confidence})')

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Create the frame with the name
            cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            cv2.putText(image, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

        # Save the resulting image
        cv2.imwrite(result_path, image)

if __name__ == '__main__':
    fr = FaceRecognition()
    fr.run_recognition('test.jpg', 'skenario02_rizqi_03.jpg')
