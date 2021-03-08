import pygame 
from random import randrange,shuffle

import time
from time import sleep
import keyboard
# press b for bubble sort and s for selection sort
pygame.init() 
surface = pygame.display.set_mode((700,700)) 
color = (255,255,255) 
arrays=[]
width=int(input('what will be the width of the blocks?'))
gap=int(input('what will be the gap between the blocks?'))
speed=10-int(input('what will be the speed between 1-10?'))
print('press S for selection sort and b for bubble sort')
speed=speed/5000
numbers=[]
lazer=(209,245,7)
for i in range(width+gap,700,(width+gap)):
	numbers.append(i)
shuffle(numbers)
arrays = numbers
x=0
run=True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_b]:
		run=False
		bubble=True
		curr_time=time.time()
	elif keys[pygame.K_s]:
		run=False
		bubble=False
		curr_time=time.time()
run=True
#arrays=sorted(arrays)
events = pygame.event.get()
other_color=(0,255,0)
if_sorted=False
if bubble:
	nummy=len(arrays)
	while (not if_sorted) and run and not keyboard.is_pressed('ctrl'):
		nummy-=1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False
		if_sorted=True
		x=0
		for i in range(len(arrays)-1):
			if i>nummy:
				break
			if i!=len(arrays)-1:
				if arrays[i]>arrays[i+1]:
					c=arrays[i]
					arrays[i]=arrays[i+1]
					arrays[i+1]=c
					if_sorted=False
					color=(255,0,0)
			stuff=arrays[i]
			other_x=x-width-gap
			if i==0:
				other_x=670
				pre_stuff=999
			else:
				pre_stuff=arrays[i-1]
			remove_pos=700-stuff
			pygame.draw.rect(surface, (0,0,0), pygame.Rect(other_x, 0, 1, 700-pre_stuff))
			pygame.draw.rect(surface, (0,0,0), pygame.Rect(x, 0, width, 700-stuff))
			pygame.draw.rect(surface, lazer, pygame.Rect(x, 0, 1, 700-stuff))
			pygame.draw.rect(surface, color, pygame.Rect(x, remove_pos, width, stuff))
			pygame.display.update()
			x+=width+gap
			color=(255,255,255)
			sleep(speed)
		pygame.draw.rect(surface, (0,0,0), pygame.Rect(other_x+width+gap, 0, 1, remove_pos))
		pygame.display.update()
else:
	for i in range(len(arrays)):
		if not run:
			break
		minimum=1000
		min_index=99999
		x=(width+gap)*i
		min_x=999999999
		thingies=[]
		for j in range(i,len(arrays)):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run=False
			if arrays[j]<minimum and j>=i:
				if min_index==i:
					color=(0,0,255)
				else:
					color=(255,255,255)
				pygame.draw.rect(surface, color, pygame.Rect(min_x, 700-minimum, width, minimum))
				minimum=arrays[j]
				min_index=j
				min_x=x
				color=(34,177,76)
			if i==j:
				color=(63,72,204)
			stuff=arrays[j]
			remove_pos=700-stuff
			other_x=x-width-gap
			pre_stuff=arrays[j-1]
			pygame.draw.rect(surface, (0,0,0), pygame.Rect(other_x+width/2, 0, 1, 700-pre_stuff))
			pygame.draw.rect(surface, (0,0,0), pygame.Rect(x, 0, width, 700))
			pygame.draw.rect(surface, lazer, pygame.Rect(x+width/2, 0, 1, 700-stuff))
			pygame.draw.rect(surface, color, pygame.Rect(x, 700-stuff, width, stuff))
			pygame.display.update()
			x+=width+gap
			color=(255,255,255)
			sleep(speed)
		c=arrays[i]
		arrays[i]=minimum
		arrays[min_index]=c
		pygame.draw.rect(surface, (0,0,0), pygame.Rect(min_x, 0, width, 700))
		pygame.draw.rect(surface, (0,0,0), pygame.Rect((width+gap)*i, 0, width, 700))
		pygame.draw.rect(surface, color, pygame.Rect(min_x, 700-c, width, c))
		pygame.draw.rect(surface, color, pygame.Rect((width+gap)*i, 700-minimum, width, minimum))
		pygame.draw.rect(surface, (0,0,0), pygame.Rect((x-width-gap)+width/2, 0, 3, remove_pos))
		pygame.display.update()