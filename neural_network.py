import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

df = pd.read_csv("acc_full_data.csv", sep=';', names=["x","y","z","label"])

X = df[["x","y","z"]].values.astype("float32")
y = df["label"].values


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


le = LabelEncoder()
y_encoded = le.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.3, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(3,)),        
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(len(np.unique(y_encoded)), activation='softmax') 
])


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)


loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test accuracy: {accuracy*100:.2f}%")


new_point = np.array([[-4, 1072, 20]])
new_point_scaled = scaler.transform(new_point)
pred_num = np.argmax(model.predict(new_point_scaled), axis=1)[0]
pred_label = le.inverse_transform([pred_num])[0]
print(f"Predicted position: {pred_label}")


model.save("acc_model.h5")
