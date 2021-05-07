import numpy as np
import PIL.Image as Image
import tensorflow as tf
import tensorflow_hub as hub
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":2,"print_urls":True}
paths = response.download(arguments)
print(paths)


# https://i.pinimg.com/originals/38/d7/5b/38d75b985d9d08ce0959201f8198f405.jpg
class Classifier:
    def __init__(self):
        classifier_model = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
        self.IMAGE_SHAPE = (224, 224)
        self.classifier = tf.keras.Sequential([
            hub.KerasLayer(classifier_model)
        ])
        labels_path = tf.keras.utils.get_file('ImageNetLabels.txt',
                                              'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
        self.imagenet_labels = np.array(open(labels_path).read().splitlines())

    def predict_labels(self, url):
        img = tf.keras.utils.get_file('image6.jpg', url)
        grace_hopper = Image.open(img).resize(self.IMAGE_SHAPE)
        grace_hopper = np.array(grace_hopper) / 255.0
        result = self.classifier.predict(grace_hopper[np.newaxis, ...])
        # predicted_class = np.argmax(result[0], axis=-1)
        top_classes = result[0].argsort()[-10:][::-1]
        top_class_names = []
        for i in list(top_classes):
            top_class_names.append(self.imagenet_labels[i])
        return top_class_names


clf = Classifier()
labels = clf.predict_labels('https://i.pinimg.com/originals/38/d7/5b/38d75b985d9d08ce0959201f8198f405.jpg')
print(labels)
