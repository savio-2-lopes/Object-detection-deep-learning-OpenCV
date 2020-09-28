# -*- coding: utf-8 -*-

import numpy as np
import argparse 
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "path to input image")
ap.add_argument("-p", "--prototxt", required = True,
                help = "path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required = True, 
                help = "path to Caffe pre trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
                help = "minimum probability to filter weak detection")
args = vars(ap.parse_args())

CLASSES = ["background", "aviao", "bicicleta", "passaro", "navio", 
           "garrafa", "onibus", "carro", "gato", "vaca", "pessoa",
           "cachorro", "cavalo", "moto", "ovelha", 
           "sofá", "trem", "monitor"]

COLORS = np.random.uniform(0, 255, size = (len(CLASSES), 3))

print("[INFO] carregando modelo...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])


image = cv2.imread(args["image"])
(h,w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300,300)), 0.007843,
                             (300,300),127.5)

]print("[INFO] object detections...")
net.setInput(blob)
detections = net.forward()

for i in np.arange(0, detections.shape[2]):

    confidence = detections[0,0,i,2] 

    if confidence > args["confidence"]:

        idx = int(detections[0,0,i,1])
        box = detections[0,0,i,3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY)=box.astype("int")
        
        label = "{}:{:.2f}%".format(CLASSES[idx], confidence * 100)
        print("[INFO] {}".format(label))
        cv2.rectangle(image, (startX,startY), (endX, endY),
                      COLORS[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(image, label, (startX, y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
                
        cv2.imshow("Output", image)
        cv2.waitKey(0)
        
