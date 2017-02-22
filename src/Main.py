
import time
import threading
import os
import Getch
import sys
from SceneManager import SceneManager
from DisplayController import DisplayControllerInterface 


def input_thread(list):
	while True:
		time.sleep(0.5)
		try:
			char = Getch.getch()
		except Exception as e:
			char = 'q'
			raise
		if char == 'q':
			list.append(None)
			return
        

def do_stuff(c,SM):
    list = []
    index = 0
    t = threading.Thread(target=input_thread, args =(list,))
    t.start()
    while not list:
        index += 1
        index = index % 15
        c.clearScreen()
        c.drawSquar(3,10,index)
        #SM.drawScene()
        time.sleep(0.5)

def get_random_number():
	return 4 #guaranteed to be random

if __name__ == "__main__":

	controler = DisplayControllerInterface()
	SM = SceneManager(20,40)
	do_stuff(controler,SM)



