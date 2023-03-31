以下是文件说明：

在该项目中，有2种面部识别应用程序和1种面部检测应用程序。

使用网络摄像头进行面部识别。
使用照片/图像进行面部识别。
在进行编码处理之前，请确保创建一个专门用于容纳将进行编码/训练处理的面部图像的文件夹。
在我的情况下，我使用的文件夹名称是wajah1。 您可以根据需要更改文件夹名称。
下面是文件夹结构：

|__wajah1
|  |
|__|
|__|___person_name
|__|
|__|___person_name_01
|__|
|__|___person_name_...

您可以按照上面的文件树使用文件夹结构。

要访问face_rec_webcam_default.py / face_rec_webcam_tuning.py，您必须运行编码脚本.npy以获取known_face_encoding.npy和known_face_names.npy，然后才能运行face_rec_webcam_default.py。

您可以通过访问main.py并根据需要进行调整（您可以选择通过更改代码“from ... import FaceRecognition on line 1”来运行face_rec_webcam_default.py / face_rec_webcam_tuning.py）来运行上述程序。

如果您已经获取了known_face_encoding.npy和known_face_names.npy文件，则可以直接运行face_rec_picture_default.py / face_rec_picture_tuning.py

请确保将要用于面部识别过程的照片添加到“test_images”文件夹中。

您可以通过运行detect_face.py使用网络摄像头进行面部检测。