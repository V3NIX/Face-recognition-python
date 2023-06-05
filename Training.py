import cv2
import os
import numpy as np
from sklearn import svm
from joblib import dump, load

# Set the path to the training and testing data
training_data_path = 'att_faces/Training'
testing_data_path = 'att_faces/Testing'

# Define a function to load the images and corresponding labels from a given directory
def load_images_from_folder(folder_path):
    images = []
    labels = []
    for subfolder_name in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder_name)
        if os.path.isdir(subfolder_path):
            label = int(subfolder_name.replace('s', '')) # Extract the label from the folder name
            for filename in os.listdir(subfolder_path):
                img_path = os.path.join(subfolder_path, filename)
                if img_path.endswith('.pgm'):
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) # Load the image in grayscale
                    images.append(img)
                    labels.append(label)
    return images, labels


# Load the training and testing data
training_images, training_labels = load_images_from_folder(training_data_path)
testing_images, testing_labels = load_images_from_folder(testing_data_path)

print('Loaded data')

# Resize the images to a fixed size (128x128) and convert them to numpy arrays
training_images = np.array([cv2.resize(x, (128, 128)) for x in training_images])
testing_images = np.array([cv2.resize(x, (128, 128)) for x in testing_images])

print('Resized images')

# Reshape the data to be 1D arrays
X_train = training_images.reshape((training_images.shape[0], -1))
X_test = testing_images.reshape((testing_images.shape[0], -1))

print('Reshaped data')

# Normalize the pixel values to be between 0 and 1
X_train = X_train / 255.0
X_test = X_test / 255.0
print('Normalized data')

# Train an SVM on the training data
clf = svm.SVC()
clf.fit(X_train, training_labels)
print('Trained SVM')

# Evaluate the model on the testing data
accuracy = clf.score(X_test, testing_labels)
accuracy2 = clf.score(X_train , training_labels)
print("Accuracy_train:", accuracy2*100,'%')
print("Accuracy_test:", accuracy*100,'%')
# save the trained model to a file
dump(clf, 'svm_model.joblib')