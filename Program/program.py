#!/usr/bin/env python
# coding: utf-8

# In[10]:


#import machine learning
import numpy as np
import pandas as pd
import sklearn
from sklearn import metrics
from sklearn.model_selection import train_test_split
from neupy import algorithms
from IPython.display import display
from sklearn.neural_network import MLPClassifier
from neupy.layers import *

#import tkinter
from tkinter import *
from tkinter import messagebox

#Random seed set
from numpy.random import seed
seed(777)
from tensorflow import set_random_seed
set_random_seed(777)

#prep and Train Neural Network begin
df = pd.read_csv("data tugas akhir crossed.csv")

#membuat variabel 'dataset' menjadi data tanpa label
dataset = df.values
#membuat variabel 'x' menjadi array data simptom tanpa label
x = dataset[:,:11]
#membuat variabel 'y' menjadi array tipe penyakit tanpa label
y = dataset [:,11]

#merubah dataset menjadi set training dan testing, dengan stratify dataset y
x_train, x_test, y_train, y_test = train_test_split(
x, y, test_size=0.1, random_state=777, shuffle=True, stratify=y)


#membuat Jaringan Saraf Tiruan metode backpropagation dengan jumlah HIDDEN LAYER 2, dan NEURON pada HIDDEN LAYER 7
network = join(Input(11),Sigmoid(7),Sigmoid(7), Sigmoid(1))
#metode Backpropagation dengan LEARNING RATE 0.1
optimizer = algorithms.Momentum(network,step=0.1)
#training metode backpropagation 
optimizer.train(x_train, y_train, x_test, y_test, epochs=200)

#tkinter window
if __name__ == '__main__':
    root = Tk()
    root.title("Aplikasi Identifikasi COVID-19")
    root.geometry("500x500")

#nampilin menampilkan prediksi covid atau negatif
def show_result():
    #memasukkan variabel dari user untuk diprediksi oleh sistem
    pred = np.array((var1.get(), var7.get(), var2.get(), var8.get(), var3.get(), var9.get(), var4.get(), var10.get(), var5.get(), var11.get(), var6.get()))
    #memprediksi hasil user dan memasukkanya ke variabel "p" dengan bentuk float
    p=optimizer.predict(pred)
    #actual adalah hasil prediksi yang di sederhanakan
    actual=0
    #jika hasil prediksi lebih dari samadengan 0.5 maka hasil akan menjadi positif
    if (p >= 0.5):
        actual=1
    #jika hasil prediksi kurang dari samadengan 0.5 maka hasil menjadi negatif
    else:
        actual=0

    #jika hasil 1, atau positif, maka mengeluarkan message box dengan prediksi positif
    if (actual == 1):
        print('sistem memprediksi anda POSITIF dengan nilai prediksi: ',p)
        messagebox.showinfo('Sistem Memprediksi','POSITIF',icon='error')
    #jika hasil 0 atau NEGATIF, maka mengeluarkan message box dengan prediksi negatif
    elif(actual == 0):
        print('sistem memprediksi anda NEGATIF dengan nilai prediksi: ',p)
        messagebox.showinfo('Sistem Memprediksi','NEGATIF' )
    else:
        print('error')
        messagebox.showinfo('Sistem mengalami Error','sistem mengalami error')

#text gejala yang dialami di tengah
Label(root, text="Gejala yang dialami:").grid(row=0,column=4, sticky=W)

#Checkboxes variable gejala-gejala yang dialami
var1 = IntVar()
Checkbutton(root, text="Batuk-Batuk", variable=var1).grid(row=1,column=3, sticky=W)
var2 = IntVar()
Checkbutton(root, text="Sesak Nafas", variable=var2).grid(row=2,column=3, sticky=W)
var3 = IntVar()
Checkbutton(root, text="Sakit Tenggorokan", variable=var3).grid(row=3,column=3, sticky=W)
var4 = IntVar()
Checkbutton(root, text="Mual-Mual", variable=var4).grid(row=4,column=3, sticky=W)
var5 = IntVar()
Checkbutton(root, text="Menggigil", variable=var5).grid(row=5,column=3, sticky=W)
var6 = IntVar()
Checkbutton(root, text="Diare", variable=var6).grid(row=6,column=3, sticky=W)
var7 = IntVar()
Checkbutton(root, text="Demam", variable=var7).grid(row=1,column=5, sticky=W)
var8 = IntVar()
Checkbutton(root, text="Rasa Lelah", variable=var8).grid(row=2,column=5, sticky=W)
var9 = IntVar()
Checkbutton(root, text="Sakit Kepala", variable=var9).grid(row=3,column=5, sticky=W)
var10 = IntVar()
Checkbutton(root, text="Otot Keram", variable=var10).grid(row=4,column=5, sticky=W)
var11 = IntVar()
Checkbutton(root, text="Pilek", variable=var11).grid(row=5,column=5, sticky=W)

#tombol untuk keluar
Button(root, text='Keluar', command=root.quit).grid(row=12,column=4, sticky=W, pady=4)
#tombol tombol submit
Button(root, text='Submit', command=show_result).grid(row=12,column=5, sticky=W, pady=4)

mainloop()


# In[ ]:




