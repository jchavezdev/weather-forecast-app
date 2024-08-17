import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import time
import random

class MainWindow(QtWidgets.QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MainWindow,self).__init__(*args,**kwargs)


		self.bt1 = QPushButton("prueba 1", self)

		fig = plt.figure()
		ax = fig.add_subplot(1,1,1)
		xs = []
		ys = []

	#Funcion que se llama de manera peri[odica
	def animate(i, xs, ys):

		#Agrega Valores
		temp_c = round(Temperatura(),2)

		#Agrega valores a las listas
		xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
		ys.append(temp_c)

		#Limita las listas
		xs = xs[-20:]
		ys = ys[-20:]

		#Traza las listas
		ax.clear()
		ax.plot(xs,ys)

		#Formato
		plt.xticks(rotation=45, ha='right')
		plt.subplots_adjust(bottom=0.30)
		plt.title('Temperatura tiempo')
		plt.ylabel('Temperatura')

	#Llama a la funcion de manera periodica
	ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys),interval=1000)
	plt.show()
	
	layout0 = QtWidgets.QVBoxLayout()
	
	layout1 = QtWidgets.QVBoxLayout()
	layout1.addWidget(plt)
	
	layout2 = QtWidgets.QVBoxLayout()
	layout2.addWidget(bt1)
	
	widget = QtWidgets.QWidget()
	widget.setLayout(layout0)
	layout0.addLayout(layout1)
	layout0.addLayout(layout2)
	self.setCentralWidget(widget)
	
	
#simulador de temperatura
def Temperatura():
	while(True):
		r=random.random()*100
	#	print(r)
		time.sleep(0.5)
		return r
	
app = QtWidgets.QApplication(sys.argv)
Temperatura()
w = MainWindow()
app.exec_()
