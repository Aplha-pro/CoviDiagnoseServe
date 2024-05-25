from joblib import load
from tensorflow.keras.preprocessing import image
import numpy as np

path = './manager/docs/img.jpg'
modelP = "./manager/docs/model.pkl"
class_names = {0:"Covid", 1:"Normal", 2: "Viral Pneumonia"}

def preprocess_testing_image(image_path, target_size=(128, 128)):
    img = image.load_img(image_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0 
    return img_array

def setup():
    global model
    model = load(modelP)

def predict():
    preprocessed_img = preprocess_testing_image(path)
    predictions = model.predict(preprocessed_img)
    print(predictions)
    predicted_class = np.argmax(predictions)
    return class_names[predicted_class]

setup()