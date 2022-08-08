import sys
import numpy as np
import matplotlib.pyplot as plt
import csv
import random
from pandas import read_csv
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.models import load_model


class Model():
    def __init__(self):
        self.net = None

    def build_model(self):
        self.net = Sequential(name='ANN_classifier')
        self.net.add(Dense(150, input_dim=2, activation='tanh'))
        self.net.add(Dense(100, input_dim=2, activation='tanh'))
        self.net.add(Dense(50, input_dim=2, activation='tanh'))
        self.net.add(Dense(1, activation='linear'))
        self.net.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

    def save_model(self, name):
        self.net.save('model/' + name + '.h5')
    
    def load_model(self, name):
        self.net = keras.models.load_model('model/' + name + '.h5')

    def train_model(self, dataset):
        self.net.fit(dataset.dataset, dataset.Label, epochs=1000, batch_size=64)
        self.make_prediction(dataset)

    def make_prediction(self, dataset):
        dataset.predict = self.net.predict(dataset.dataset)
        
        for i in range(len(dataset.predict)):
            if dataset.predict[i] < 1:
                dataset.InsideX.append(dataset.dataset[i][0])
                dataset.InsideY.append(dataset.dataset[i][1])
                dataset.Label = np.append(dataset.Label, dataset.class_label["Inside"])
            else:
                dataset.OutsideX.append(dataset.dataset[i][0])
                dataset.OutsideY.append(dataset.dataset[i][1])
                dataset.Label = np.append(dataset.Label, dataset.class_label["Outside"])
        draw_plot(dataset)
    
    def write_output(self, name, dataset):
        for i in range(len(dataset.dataset)):
            print(dataset.dataset[i], dataset.Label[i])
        with open(name + ".csv", "a", newline="") as csvfile:
            for i in range(len(dataset.dataset)):
                writer = csv.writer(csvfile)
                writer.writerow([str(dataset.dataset[i]) + "; " + str(dataset.Label[i])])

class Dataset:
    def __init__(self):
        self.InsideX = []
        self.InsideY = []
        self.OutsideX = []
        self.OutsideY = []
        self.dataset = np.array([])
        self.Coords = []
        self.Label = np.array([])
        self.predict = None
        self.class_label = {"Inside": 1, "Outside": 0}

    def generate_dataset(self, name, size):
        with open(name + ".csv", "a", newline="") as csvfile:
            for i in range(size):
                x1 = random.uniform(-4, 2)
                x2 = random.uniform(2, 5)   
                writer = csv.writer(csvfile)
                writer.writerow([str(x1) + ";" + str(x2)])

    def read_dataset(self, name):
        with open(name + ".csv", "r", newline="") as csvfile:
            csvReader = csv.reader(csvfile, delimiter=';')
            for row in csvReader:
                self.Coords = np.append(float(row[0].replace(',', ".")), float(row[1].replace(',', ".")))
                self.dataset = np.append(self.dataset, self.Coords)
                self.dataset = np.reshape(self.dataset, (-1, 2))
        
    def make_labels(self):
        for i in range(len(self.dataset)):
            if 0.4444444 * (self.dataset[i][0] + 2)**2 + 2.36686399 * (self.dataset[i][1] - 3)**2 < 1:
                self.Label = np.append(self.Label, self.class_label["Inside"])
            else:
                self.Label = np.append(self.Label, self.class_label["Outside"])

def draw_plot(dataset):
    plt.axis([-4,2,2,5])
    plt.plot(dataset.InsideX, dataset.InsideY, "ro", color = "blue", label="Inside")
    plt.plot(dataset.OutsideX, dataset.OutsideY, "ro", color = "red", label="Outside")
    plt.legend(loc="upper left")
    plt.show()

if __name__ == '__main__':
    action = "build_new_model_and_make_prediction"

    if action == "create_dataset":
        dataset3 = Dataset()
        dataset3.generate_dataset("Data_1", 8000)
    
    if action == "build_new_model_and_make_prediction":
        dataset2 = Dataset()
        dataset2.read_dataset("Data_1")
        dataset2.make_labels()
        ANN2 = Model()
        ANN2.build_model()
        ANN2.save_model("ANN2_classifier")
        ANN2.train_model(dataset2)
        ANN2.make_prediction(dataset2)
        ANN2.write_output("output1", dataset2)

    if action == "load_model_and_make_prediction":
        dataset1 = Dataset()
        dataset1.read_dataset("Data_1")
        dataset1.make_labels()
        ANN1 = Model()
        ANN1.load_model("ANN_classifier")
        ANN1.make_prediction(dataset1)
        ANN1.write_output("output", dataset1)
