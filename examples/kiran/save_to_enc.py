#!/usr/bin/env python
# -*- coding: utf-8 -*-

import face_recognition
import pickle
import os

all_face_encodings = {}

known_folder = r'C:\Users\kraminen\Documents\images\known'
encode_folder = r'C:\Users\kraminen\Documents\images\enc'

for root, dirs, files in os.walk(known_folder):
    # print(root, dirs, files)
    images = (x for x in files if os.path.splitext(x)[-1] in ('.jpg|.JPG|.png|.PNG'))
    for x in images:
        img = face_recognition.load_image_file(os.path.join(known_folder, x))
        all_face_encodings[os.path.splitext(x)[0]] = face_recognition.face_encodings(img)[0] 
    print(all_face_encodings.keys())

with open(os.path.join(encode_folder, 'dataset_faces.dat'), 'wb') as f:
    pickle.dump(all_face_encodings, f)
