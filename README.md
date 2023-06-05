# Face-recognition-python
This project involves the development of a face recognition system using the Support Vector Machine (SVM) algorithm. The system was built using the Python programming language, with a Graphical User Interface (GUI) created using Tkinter. The system was trained on the AT&T dataset, consisting of 400 images of 40 individuals, with 10 images per person. The dataset was split into training and testing data, with the images resized to 128x128 and converted to grayscale. The SVM was trained on the training data, achieving an accuracy of 100%, and was evaluated on the testing data, achieving an accuracy of 95%. The main packages used in the development of the system were cv2, numpy, sklearn-svm, and joblib. The final model was saved using the joblib package. In conclusion, this project demonstrates the effectiveness of the SVM algorithm in face recognition tasks and provides a basis for further improvements in accuracy and scalability.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
![image](https://github.com/V3NIX/Face-recognition-python/assets/117733151/508668e7-df8d-43ee-93a4-778d0a4049c4)
![image](https://github.com/V3NIX/Face-recognition-python/assets/117733151/174274aa-c3d3-4b1b-9f08-af420b5f2d75)

---FaceApp---
*Overview:
This app is a face recognition system that can operate in two modes: real-time or image-based. It uses machine learning algorithms to recognize faces from a dataset of known individuals, stored in the "persons" folder. The app is launched by running the GUI.py file, which opens a graphical user interface that allows the user to select the mode and operate the app.
![image](https://github.com/V3NIX/Face-recognition-python/assets/117733151/83b65f71-1102-4f23-ba1d-2c31d255ba61)

*Installation:
To run this app, you need to have Python 3 installed on your machine, as well as several Python libraries: OpenCV, numpy, PIL, and scikit-learn. These can be installed using pip, by running the following command:

pip install opencv-python numpy Pillow scikit-learn

Once you have installed the necessary libraries, you can launch the app by running the GUI.py file.

*Usage:
To use the app, follow these steps:
(!!LAUNCH 'Training.py' FOR 1ST TIME USAGE , TO CREATE THE 'svm_model.joblib' FILE!!)
-Launch the app by running the GUI.py file.
-Select the mode you want to use: real-time or image-based.
-If you selected real-time mode, the app will use your computer's webcam to capture video and perform face recognition on each frame. If you selected image-based mode, you can select an image file from your computer to be processed.
-The app will compare the faces in the input (either a live video stream or an image file) with the faces in the "persons" folder. If a match is found, the app will display the name of the recognized person on the screen.

*Files:
This folder contains the following files:

-GUI.py: This file launches the graphical user interface for the app.
-training.py: This file contains the machine learning algorithms for training and testing the face recognition model.
-real_time.py: This file contains the code for real-time face recognition.
-image_rec.py: This file contains the code for image-based face recognition.
-persons/: This folder contains images and names of the allowed people in the system.
-svm_model.joblib: This file contains the trained Support Vector Machine model used for face recognition.
-haarcascade_frontalface_default.xml: This file contains the pre-trained Haar Cascade classifier used for face detection.

*Conclusion:
Thank you for trying out my face recognition app! I hope you find it useful and informative. If you have any questions or comments, please feel free to reach out to me.
