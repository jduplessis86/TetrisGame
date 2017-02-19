
import time
import threading
import os
import Getch
import sys
import SceanManager
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
        

def do_stuff(c):
    list = []
    index = 0
    t = threading.Thread(target=input_thread, args =(list,))
    t.start()
    while not list:
        index += 1
        index = index % 15
        c.clearScreen()
        c.drawSquar(3,10,index)
        time.sleep(1)


	

if __name__ == "__main__":

	controler = DisplayControllerInterface()
	
	do_stuff(controler)



