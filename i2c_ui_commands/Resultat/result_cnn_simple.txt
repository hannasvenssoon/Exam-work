X shape: (3618, 128, 3)
y shape: (3618,)
Unique labels: [0 1 2]
Label distribution: [ 484  843 2291]
Random split (evaluation)
Train: (2532, 128, 3) (2532,)
Test : (1086, 128, 3) (1086,)
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

 dense_1 (Dense)             (None, 3)                 195

=================================================================
Total params: 13411 (52.39 KB)
Trainable params: 13411 (52.39 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
Class weights: {0: 2.489675516224189, 1: 1.4305084745762713, 2: 0.5265127885215222}
Epoch 1/60
32/32 [==============================] - 1s 17ms/step - loss: 0.8398 - accuracy: 0.6602 - val_loss: 0.7445 - val_accuracy: 0.6095 - lr: 0.0010
Epoch 2/60
32/32 [==============================] - 0s 11ms/step - loss: 0.4466 - accuracy: 0.7116 - val_loss: 0.4919 - val_accuracy: 0.7751 - lr: 0.0010
Epoch 3/60
32/32 [==============================] - 0s 10ms/step - loss: 0.3403 - accuracy: 0.8000 - val_loss: 0.3937 - val_accuracy: 0.8107 - lr: 0.0010
Epoch 4/60
32/32 [==============================] - 0s 10ms/step - loss: 0.2935 - accuracy: 0.8286 - val_loss: 0.4458 - val_accuracy: 0.8126 - lr: 0.0010
Epoch 5/60
32/32 [==============================] - 0s 10ms/step - loss: 0.2742 - accuracy: 0.8405 - val_loss: 0.3567 - val_accuracy: 0.8560 - lr: 0.0010
Epoch 6/60
32/32 [==============================] - 0s 10ms/step - loss: 0.2479 - accuracy: 0.8548 - val_loss: 0.3069 - val_accuracy: 0.8659 - lr: 0.0010
Epoch 7/60
32/32 [==============================] - 0s 10ms/step - loss: 0.2395 - accuracy: 0.8602 - val_loss: 0.3244 - val_accuracy: 0.8718 - lr: 0.0010
Epoch 8/60
32/32 [==============================] - 0s 10ms/step - loss: 0.2323 - accuracy: 0.8672 - val_loss: 0.3676 - val_accuracy: 0.8639 - lr: 0.0010
Epoch 9/60
32/32 [==============================] - 0s 10ms/step - loss: 0.2306 - accuracy: 0.8701 - val_loss: 0.3082 - val_accuracy: 0.8738 - lr: 0.0010
Epoch 10/60
32/32 [==============================] - 0s 10ms/step - loss: 0.2226 - accuracy: 0.8736 - val_loss: 0.3597 - val_accuracy: 0.8580 - lr: 0.0010
Epoch 11/60
32/32 [==============================] - 0s 10ms/step - loss: 0.2048 - accuracy: 0.8800 - val_loss: 0.3282 - val_accuracy: 0.8698 - lr: 0.0010
Epoch 12/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1935 - accuracy: 0.8830 - val_loss: 0.2707 - val_accuracy: 0.8895 - lr: 5.0000e-04
Epoch 13/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1926 - accuracy: 0.8894 - val_loss: 0.3102 - val_accuracy: 0.8836 - lr: 5.0000e-04
Epoch 14/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1874 - accuracy: 0.8859 - val_loss: 0.2962 - val_accuracy: 0.8876 - lr: 5.0000e-04
Epoch 15/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1852 - accuracy: 0.8914 - val_loss: 0.3110 - val_accuracy: 0.8718 - lr: 5.0000e-04
Epoch 16/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1906 - accuracy: 0.8889 - val_loss: 0.2837 - val_accuracy: 0.8817 - lr: 5.0000e-04
Epoch 17/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1832 - accuracy: 0.8948 - val_loss: 0.2695 - val_accuracy: 0.8915 - lr: 5.0000e-04
Epoch 18/60
32/32 [==============================] - 0s 12ms/step - loss: 0.1739 - accuracy: 0.8968 - val_loss: 0.2692 - val_accuracy: 0.8797 - lr: 5.0000e-04
Epoch 19/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1697 - accuracy: 0.8973 - val_loss: 0.2837 - val_accuracy: 0.8856 - lr: 5.0000e-04
Epoch 20/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1713 - accuracy: 0.8928 - val_loss: 0.2654 - val_accuracy: 0.8856 - lr: 5.0000e-04
Epoch 21/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1777 - accuracy: 0.8904 - val_loss: 0.2853 - val_accuracy: 0.8895 - lr: 5.0000e-04
Epoch 22/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1816 - accuracy: 0.8943 - val_loss: 0.2684 - val_accuracy: 0.8856 - lr: 5.0000e-04
Epoch 23/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1809 - accuracy: 0.8923 - val_loss: 0.3012 - val_accuracy: 0.8777 - lr: 5.0000e-04
Epoch 24/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1790 - accuracy: 0.8904 - val_loss: 0.3168 - val_accuracy: 0.8797 - lr: 5.0000e-04
Epoch 25/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1688 - accuracy: 0.9057 - val_loss: 0.2925 - val_accuracy: 0.8895 - lr: 5.0000e-04
Epoch 26/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1639 - accuracy: 0.9027 - val_loss: 0.2585 - val_accuracy: 0.8935 - lr: 2.5000e-04
Epoch 27/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1579 - accuracy: 0.9057 - val_loss: 0.2905 - val_accuracy: 0.8856 - lr: 2.5000e-04
Epoch 28/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1583 - accuracy: 0.9042 - val_loss: 0.2604 - val_accuracy: 0.8856 - lr: 2.5000e-04
Epoch 29/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1524 - accuracy: 0.9062 - val_loss: 0.2572 - val_accuracy: 0.8856 - lr: 2.5000e-04
Epoch 30/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1574 - accuracy: 0.9032 - val_loss: 0.2796 - val_accuracy: 0.8895 - lr: 2.5000e-04
Epoch 31/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1569 - accuracy: 0.9081 - val_loss: 0.2579 - val_accuracy: 0.8895 - lr: 2.5000e-04
Epoch 32/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1559 - accuracy: 0.9052 - val_loss: 0.2638 - val_accuracy: 0.8876 - lr: 2.5000e-04
Epoch 33/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1505 - accuracy: 0.9096 - val_loss: 0.2545 - val_accuracy: 0.8935 - lr: 2.5000e-04
Epoch 34/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1559 - accuracy: 0.9072 - val_loss: 0.2776 - val_accuracy: 0.8817 - lr: 2.5000e-04
Epoch 35/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1533 - accuracy: 0.9081 - val_loss: 0.2494 - val_accuracy: 0.8895 - lr: 2.5000e-04
Epoch 36/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1490 - accuracy: 0.9091 - val_loss: 0.2329 - val_accuracy: 0.8974 - lr: 2.5000e-04
Epoch 37/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1509 - accuracy: 0.9081 - val_loss: 0.2706 - val_accuracy: 0.8915 - lr: 2.5000e-04
Epoch 38/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1533 - accuracy: 0.9081 - val_loss: 0.2373 - val_accuracy: 0.8994 - lr: 2.5000e-04
Epoch 39/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1509 - accuracy: 0.9062 - val_loss: 0.2609 - val_accuracy: 0.8955 - lr: 2.5000e-04
Epoch 40/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1481 - accuracy: 0.9116 - val_loss: 0.2531 - val_accuracy: 0.8915 - lr: 2.5000e-04
Epoch 41/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1555 - accuracy: 0.9081 - val_loss: 0.2531 - val_accuracy: 0.8935 - lr: 2.5000e-04
Epoch 42/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1459 - accuracy: 0.9101 - val_loss: 0.2325 - val_accuracy: 0.8974 - lr: 1.2500e-04
Epoch 43/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1451 - accuracy: 0.9170 - val_loss: 0.2301 - val_accuracy: 0.8974 - lr: 1.2500e-04
Epoch 44/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1438 - accuracy: 0.9116 - val_loss: 0.2443 - val_accuracy: 0.8974 - lr: 1.2500e-04
Epoch 45/60
32/32 [==============================] - 0s 11ms/step - loss: 0.1413 - accuracy: 0.9116 - val_loss: 0.2510 - val_accuracy: 0.8935 - lr: 1.2500e-04
Epoch 46/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1415 - accuracy: 0.9146 - val_loss: 0.2344 - val_accuracy: 0.8955 - lr: 1.2500e-04
Epoch 47/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1418 - accuracy: 0.9126 - val_loss: 0.2331 - val_accuracy: 0.8955 - lr: 1.2500e-04
Epoch 48/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1486 - accuracy: 0.9121 - val_loss: 0.2298 - val_accuracy: 0.8974 - lr: 1.2500e-04
Epoch 49/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1438 - accuracy: 0.9165 - val_loss: 0.2412 - val_accuracy: 0.8915 - lr: 1.2500e-04
Epoch 50/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1425 - accuracy: 0.9111 - val_loss: 0.2545 - val_accuracy: 0.8915 - lr: 1.2500e-04
Epoch 51/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1428 - accuracy: 0.9131 - val_loss: 0.2309 - val_accuracy: 0.8994 - lr: 1.2500e-04
Epoch 52/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1480 - accuracy: 0.9101 - val_loss: 0.2667 - val_accuracy: 0.8935 - lr: 1.2500e-04
Epoch 53/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1426 - accuracy: 0.9126 - val_loss: 0.2515 - val_accuracy: 0.8935 - lr: 1.2500e-04
Epoch 54/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1397 - accuracy: 0.9185 - val_loss: 0.2401 - val_accuracy: 0.8974 - lr: 6.2500e-05
Epoch 55/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1434 - accuracy: 0.9141 - val_loss: 0.2430 - val_accuracy: 0.8915 - lr: 6.2500e-05
Epoch 56/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1394 - accuracy: 0.9141 - val_loss: 0.2326 - val_accuracy: 0.8955 - lr: 6.2500e-05
Epoch 57/60
32/32 [==============================] - 0s 9ms/step - loss: 0.1364 - accuracy: 0.9185 - val_loss: 0.2346 - val_accuracy: 0.8935 - lr: 6.2500e-05
Epoch 58/60
32/32 [==============================] - 0s 10ms/step - loss: 0.1364 - accuracy: 0.9170 - val_loss: 0.2381 - val_accuracy: 0.8974 - lr: 6.2500e-05


Offline inference predicted labels:
['standing', 'standing', 'standing', 'standing', 'moving', 'moving', 'moving', 'moving', 'standing', 'standing', 'moving', 'standing', 'lying', 'standing', 'standing', 'standing', 'standing', 'lying', 'standing', 'moving', 'standing', 'moving', 'standing', 'standing', 'standing', 'standing', 'standing', 'lying', 'standing', 'lying', 'standing', 'standing', 'lying', 'moving', 'standing', 'standing', 'standing', 'standing', 'moving', 'standing']

00: true=standing   pred=standing
01: true=standing   pred=standing
02: true=standing   pred=standing
03: true=standing   pred=standing
04: true=moving     pred=moving
05: true=moving     pred=moving
06: true=moving     pred=moving
07: true=moving     pred=moving
08: true=standing   pred=standing
09: true=standing   pred=standing
10: true=standing   pred=moving
11: true=standing   pred=standing
12: true=lying      pred=lying
13: true=standing   pred=standing
14: true=standing   pred=standing
15: true=standing   pred=standing
16: true=standing   pred=standing
17: true=lying      pred=lying
18: true=standing   pred=standing
19: true=moving     pred=moving
20: true=standing   pred=standing
21: true=standing   pred=moving
22: true=standing   pred=standing
23: true=standing   pred=standing
24: true=standing   pred=standing
25: true=standing   pred=standing
26: true=standing   pred=standing
27: true=standing   pred=lying
28: true=standing   pred=standing
29: true=lying      pred=lying
30: true=standing   pred=standing
31: true=standing   pred=standing
32: true=standing   pred=lying
33: true=moving     pred=moving
34: true=standing   pred=standing
35: true=standing   pred=standing
36: true=standing   pred=standing
37: true=standing   pred=standing
38: true=moving     pred=moving
39: true=standing   pred=standing

Evaluation results CNN
Accuracy        : 0.9227
F1-score (Macro): 0.9134
F1-score (Weighted): 0.9237