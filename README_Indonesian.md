Berikut adalah dokumentasi :

Dalam project ini, ada 2 jenis aplikasi pengenalan wajah dan 1 jenis pendeteksian wajah.

1. Pengenalan wajah dengan menggunakan webcam.
2. Pengenalan wajah dengan menggunakan foto/gambar.

Sebelum melakukan proses encoding, pastikan anda membuat folder khusus untuk menampung citra wajah yang akan dilakukan proses encoding/training.
Pada kasus saya, nama folder yang saya gunakan adalah wajah1. Anda dapat merubah nama folder sesuai kebutuhan.
berikut susunan folder:

|__wajah1
|  |
|__|
|__|___person_name
|__|
|__|___person_name_01
|__|
|__|___person_name_...

Anda bisa menggunakan susunan folder sesuai dengan folder tree di atas.

Untuk mengakses face_rec_webcam_default.py/face_rec_webcam_tuning.py, anda diharuskan menjalankan
script encoding.npy untuk mendapatkan known_face_encoding.npy dan known_face_names.npy
setelah itu anda bisa menjalankan face_rec_webcam_default.py.

Anda bisa menjalankan program diatas dengan mengakses main.py dan sesuaikan kebutuhan anda ( anda bisa memilih untuk menjalankan face_rec_webcam_default.py/face_rec_webcam_tuning.py dengan merubah kode program "from ... import FaceRecognition pada line 1)

Jika anda sudah mendapatkan file known_face_encoding.npy dan known_face_names.npy, anda langsung bisa 
menjalankan face_rec_picture_default.py/face_rec_picture_tuning.py

Pastikan anda sudah menambahkan foto yang akan digunakan untuk proses pengenalan wajah kedalam folder "test_images".

Anda dapat melakukan proses pendeteksian wajah dengan menggunakan webcam dengan menjalankan detect_face.py