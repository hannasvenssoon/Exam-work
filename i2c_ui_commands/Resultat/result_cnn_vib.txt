X shape: (1429, 128, 3)
y shape: (1429,)
Unique labels: [0 1]
Label distribution: [759 670]
Random split (evaluation)
Train: (1000, 128, 3) (1000,)
Test : (429, 128, 3) (429,)
Model: "model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input_1 (InputLayer)        [(None, 128, 3)]          0

 conv1d (Conv1D)             (None, 128, 16)           256

 max_pooling1d (MaxPooling1  (None, 64, 16)            0
 D)

 conv1d_1 (Conv1D)           (None, 64, 32)            2592

 max_pooling1d_1 (MaxPoolin  (None, 32, 32)            0
 g1D)

 conv1d_2 (Conv1D)           (None, 32, 64)            6208

 global_average_pooling1d (  (None, 64)                0
 GlobalAveragePooling1D)

 dense (Dense)               (None, 64)                4160

 dropout (Dropout)           (None, 64)                0

 dense_1 (Dense)             (None, 2)                 130

=================================================================
Total params: 13346 (52.13 KB)
Trainable params: 13346 (52.13 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
Class weights: {0: 0.9416195856873822, 1: 1.0660980810234542}
Epoch 1/60
13/13 [==============================] - 1s 29ms/step - loss: 0.6711 - accuracy: 0.6662 - val_loss: 0.6358 - val_accuracy: 0.8350 - lr: 0.0010
Epoch 2/60
13/13 [==============================] - 0s 13ms/step - loss: 0.5828 - accuracy: 0.8275 - val_loss: 0.5041 - val_accuracy: 0.8650 - lr: 0.0010
Epoch 3/60
13/13 [==============================] - 0s 14ms/step - loss: 0.4212 - accuracy: 0.8888 - val_loss: 0.3401 - val_accuracy: 0.8900 - lr: 0.0010
Epoch 4/60
13/13 [==============================] - 0s 12ms/step - loss: 0.2732 - accuracy: 0.9250 - val_loss: 0.2741 - val_accuracy: 0.8950 - lr: 0.0010
Epoch 5/60
13/13 [==============================] - 0s 11ms/step - loss: 0.2028 - accuracy: 0.9350 - val_loss: 0.2457 - val_accuracy: 0.9050 - lr: 0.0010
Epoch 6/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1877 - accuracy: 0.9413 - val_loss: 0.2074 - val_accuracy: 0.9200 - lr: 0.0010
Epoch 7/60
13/13 [==============================] - 0s 11ms/step - loss: 0.1665 - accuracy: 0.9488 - val_loss: 0.2024 - val_accuracy: 0.9300 - lr: 0.0010
Epoch 8/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1654 - accuracy: 0.9475 - val_loss: 0.2172 - val_accuracy: 0.9300 - lr: 0.0010
Epoch 9/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1526 - accuracy: 0.9463 - val_loss: 0.1966 - val_accuracy: 0.9350 - lr: 0.0010
Epoch 10/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1504 - accuracy: 0.9450 - val_loss: 0.2084 - val_accuracy: 0.9300 - lr: 0.0010
Epoch 11/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1520 - accuracy: 0.9513 - val_loss: 0.2056 - val_accuracy: 0.9300 - lr: 0.0010
Epoch 12/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1415 - accuracy: 0.9500 - val_loss: 0.1986 - val_accuracy: 0.9200 - lr: 0.0010
Epoch 13/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1418 - accuracy: 0.9525 - val_loss: 0.2013 - val_accuracy: 0.9350 - lr: 0.0010
Epoch 14/60
13/13 [==============================] - 0s 13ms/step - loss: 0.1337 - accuracy: 0.9500 - val_loss: 0.2312 - val_accuracy: 0.9200 - lr: 0.0010
Epoch 15/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1468 - accuracy: 0.9438 - val_loss: 0.1931 - val_accuracy: 0.9350 - lr: 5.0000e-04
Epoch 16/60
13/13 [==============================] - 0s 11ms/step - loss: 0.1351 - accuracy: 0.9500 - val_loss: 0.2034 - val_accuracy: 0.9350 - lr: 5.0000e-04
Epoch 17/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1306 - accuracy: 0.9588 - val_loss: 0.1929 - val_accuracy: 0.9300 - lr: 5.0000e-04
Epoch 18/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1265 - accuracy: 0.9588 - val_loss: 0.1983 - val_accuracy: 0.9250 - lr: 5.0000e-04
Epoch 19/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1322 - accuracy: 0.9500 - val_loss: 0.1971 - val_accuracy: 0.9250 - lr: 5.0000e-04
Epoch 20/60
13/13 [==============================] - 0s 11ms/step - loss: 0.1292 - accuracy: 0.9538 - val_loss: 0.2025 - val_accuracy: 0.9200 - lr: 5.0000e-04
Epoch 21/60
13/13 [==============================] - 0s 11ms/step - loss: 0.1329 - accuracy: 0.9525 - val_loss: 0.2007 - val_accuracy: 0.9250 - lr: 5.0000e-04
Epoch 22/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1300 - accuracy: 0.9588 - val_loss: 0.1996 - val_accuracy: 0.9300 - lr: 5.0000e-04
Epoch 23/60
13/13 [==============================] - 0s 11ms/step - loss: 0.1184 - accuracy: 0.9613 - val_loss: 0.1955 - val_accuracy: 0.9300 - lr: 2.5000e-04
Epoch 24/60
13/13 [==============================] - 0s 11ms/step - loss: 0.1281 - accuracy: 0.9600 - val_loss: 0.1914 - val_accuracy: 0.9350 - lr: 2.5000e-04
Epoch 25/60
13/13 [==============================] - 0s 11ms/step - loss: 0.1194 - accuracy: 0.9613 - val_loss: 0.1929 - val_accuracy: 0.9300 - lr: 2.5000e-04
Epoch 26/60
13/13 [==============================] - 0s 11ms/step - loss: 0.1175 - accuracy: 0.9588 - val_loss: 0.1920 - val_accuracy: 0.9300 - lr: 2.5000e-04
Epoch 27/60
13/13 [==============================] - 0s 11ms/step - loss: 0.1218 - accuracy: 0.9588 - val_loss: 0.1950 - val_accuracy: 0.9300 - lr: 2.5000e-04
Epoch 28/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1206 - accuracy: 0.9588 - val_loss: 0.1926 - val_accuracy: 0.9300 - lr: 2.5000e-04
Epoch 29/60
13/13 [==============================] - 0s 11ms/step - loss: 0.1151 - accuracy: 0.9588 - val_loss: 0.1925 - val_accuracy: 0.9300 - lr: 2.5000e-04
Epoch 30/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1135 - accuracy: 0.9600 - val_loss: 0.1928 - val_accuracy: 0.9350 - lr: 1.2500e-04
Epoch 31/60
13/13 [==============================] - 0s 11ms/step - loss: 0.1172 - accuracy: 0.9625 - val_loss: 0.1927 - val_accuracy: 0.9300 - lr: 1.2500e-04
Epoch 32/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1145 - accuracy: 0.9650 - val_loss: 0.1929 - val_accuracy: 0.9350 - lr: 1.2500e-04
Epoch 33/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1143 - accuracy: 0.9638 - val_loss: 0.1938 - val_accuracy: 0.9350 - lr: 1.2500e-04
Epoch 34/60
13/13 [==============================] - 0s 12ms/step - loss: 0.1228 - accuracy: 0.9525 - val_loss: 0.1932 - val_accuracy: 0.9350 - lr: 1.2500e-04

Offline inference predicted labels:
['normal', 'normal', 'normal', 'abnormal', 'abnormal', 'abnormal', 'normal', 'normal', 'normal', 'abnormal', 'abnormal', 'normal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'normal', 'abnormal', 'normal', 'normal', 'normal', 'normal', 'abnormal', 'abnormal', 'normal', 'abnormal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'abnormal', 'normal', 'normal', 'abnormal', 'normal', 'abnormal', 'abnormal']

00: true=normal     pred=normal
01: true=normal     pred=normal
02: true=normal     pred=normal
03: true=abnormal   pred=abnormal
04: true=abnormal   pred=abnormal
05: true=abnormal   pred=abnormal
06: true=normal     pred=normal
07: true=normal     pred=normal
08: true=normal     pred=normal
09: true=abnormal   pred=abnormal
10: true=abnormal   pred=abnormal
11: true=normal     pred=normal
12: true=abnormal   pred=abnormal
13: true=abnormal   pred=abnormal
14: true=abnormal   pred=abnormal
15: true=abnormal   pred=abnormal
16: true=normal     pred=abnormal
17: true=normal     pred=normal
18: true=abnormal   pred=abnormal
19: true=normal     pred=normal
20: true=normal     pred=normal
21: true=normal     pred=normal
22: true=normal     pred=normal
23: true=abnormal   pred=abnormal
24: true=abnormal   pred=abnormal
25: true=normal     pred=normal
26: true=abnormal   pred=abnormal
27: true=normal     pred=normal
28: true=normal     pred=normal
29: true=normal     pred=normal
30: true=normal     pred=normal
31: true=normal     pred=normal
32: true=normal     pred=normal
33: true=abnormal   pred=abnormal
34: true=normal     pred=normal
35: true=normal     pred=normal
36: true=abnormal   pred=abnormal
37: true=normal     pred=normal
38: true=abnormal   pred=abnormal
39: true=abnormal   pred=abnormal

Evaluation results CNN vibration table
Accuracy        : 0.9394
F1-score (Macro): 0.9388
F1-score (Weighted): 0.9392