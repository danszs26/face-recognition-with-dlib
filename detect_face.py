import cv2
import face_recognition

# Initialize some variables
face_locations = []

# Get a reference to webcam 
video_capture = cv2.VideoCapture(0)

while True:
    # Capture a frame
    ret, frame = video_capture.read()

    # Convert the frame from BGR color to RGB color for face_recognition library
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)

    # Draw a rectangle around the face
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
video_capture.release()

# Close all windows
cv2.destroyAllWindows()
