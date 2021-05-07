from django.shortcuts import render
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings
import base64
from io import BytesIO
from tensorflow.python.keras.backend import set_session
#
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
# from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt
import numpy as np
# from keras.applications import vgg16
import datetime
import traceback


import PIL.Image as Image
import tensorflow as tf


def index(request):
    if request.method == "POST":
        f = request.FILES['sentFile']  # here you get the files needed
        response = {}
        file_name = "pic.jpg"
        file_name_2 = default_storage.save(file_name, f)
        file_url = default_storage.url(file_name_2)
        print('skjdfhasldkjfhasdkjfhaslkjfhalkjfhasdkljfhadkljfhasdkljfhadskjfhafkhdkf')
        print('skjdfhasldkjfhasdkjfhaslkjfhalkjfhasdkljfhadkljfhasdkljfhadskjfhafkhdkf')
        print('skjdfhasldkjfhasdkjfhaslkjfhalkjfhasdkljfhadkljfhasdkljfhadskjfhafkhdkf')
        print('skjdfhasldkjfhasdkjfhaslkjfhalkjfhasdkljfhadkljfhasdkljfhadskjfhafkhdkf')
        print('skjdfhasldkjfhasdkjfhaslkjfhalkjfhasdkljfhadkljfhasdkljfhadskjfhafkhdkf')
        print('skjdfhasldkjfhasdkjfhaslkjfhalkjfhasdkljfhadkljfhasdkljfhadskjfhafkhdkf')
        print('skjdfhasldkjfhasdkjfhaslkjfhalkjfhasdkljfhadkljfhasdkljfhadskjfhafkhdkf')
        print('skjdfhasldkjfhasdkjfhaslkjfhalkjfhasdkljfhadkljfhasdkljfhadskjfhafkhdkf')
        print('skjdfhasldkjfhasdkjfhaslkjfhalkjfhasdkljfhadkljfhasdkljfhadskjfhafkhdkf')
        print('skjdfhasldkjfhasdkjfhaslkjfhalkjfhasdkljfhadkljfhasdkljfhadskjfhafkhdkf')
        print('skjdfhasldkjfhasdkjfhaslkjfhalkjfhasdkljfhadkljfhasdkljfhadskjfhafkhdkf')
        print('skjdfhasldkjfhasdkjfhaslkjfhalkjfhasdkljfhadkljfhasdkljfhadskjfhafkhdkf')
        print(file_url)
        print(settings.BASE_DIR)
        print(f)
        # Predicting labels
        img = Image.open('{}{}'.format(settings.BASE_DIR, file_url)).resize((224, 224))

        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())


        img = np.array(img) / 255.0
        result = settings.CLASSIFIER.predict(img[np.newaxis, ...])
        top_classes = result[0].argsort()[-10:][::-1]
        top_class_names = []
        for i in list(top_classes):
            top_class_names.append(settings.IMAGENET_LABELS[i])
        response['name'] = top_class_names  #', '.join(top_class_names)
        response['image'] = "data:image/png;base64," + str(img_str)[2: -1]
        paths = settings.GOOGLE_RESPONSE.download({
            "keywords": ", ".join(top_class_names[:1]),
            "limit": 4,
            "print_urls": True
        })
        print(paths)
        paths = [p.split('server_clf\\')[1] for p in paths[0][top_class_names[0]]]
        response['urls'] = paths
        print(paths)
        return render(request, 'homepage.html', response)
    else:
        return render(request, 'homepage.html')