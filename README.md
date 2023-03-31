# face-recognition-with-dlib
face recognition with dlib (face_recognition) including face confidence and available to detect face in sub-directory

## Here is the documentation:

In this project, there are 2 types of face recognition applications and 1 type of face detection.

### 1. Face recognition using webcam.
### 2. Face recognition using a photo/image.

Before performing the encoding process, make sure you create a special folder to store the facial images that will undergo the encoding/training process. In my case, the folder name I used was ###"wajah1"###. You can change the folder name as needed. Here is the folder structure:

![image.png]( https://github.com/danszs26/face-recognition-with-dlib/blob/main/assets/folder_tree.png )

You can use the folder structure according to the above folder tree.

To access ###face_rec_webcam_default.py/face_rec_webcam_tuning.py###, you need to run the ###encoding.npy### script to obtain ###known_face_encoding.npy### and ###known_face_names.npy###, and then you can run ###face_rec_webcam_default.py.###

You can run the above program by accessing main.py and adjusting it to your needs (you can choose to run face_rec_webcam_default.py/face_rec_webcam_tuning.py by changing the program code "from ... import FaceRecognition" on line 1).

If you have obtained the known_face_encoding.npy and known_face_names.npy files, you can directly run face_rec_picture_default.py/face_rec_picture_tuning.py.

Make sure you have added the photo that will be used for face recognition process into the "test_images" folder.

You can perform face detection using a webcam by running detect_face.py.
