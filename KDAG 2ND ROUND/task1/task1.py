
#kdag task 1
# Soham Agarwal 24CH10039

#introduction to the task
# two ants 1 and 2 are present in a pygame and they will now start to move based on the conditions initially provided 

import pygame
import numpy as np
import random
pygame.init()
WHITE, BLACK ,ANT1_COLOR,ANT2_COLOR = (255, 255, 255), (0, 0, 0),(0, 255, 0),(0, 255, 255)
direction = {0:'UP', 1:'RIGHT', 2:'DOWN', 3:'LEFT'}
colors = {0: WHITE , 1: BLACK}
box_size = 30
length = 720
breadth = 1080
rows = length // box_size
cols = breadth // box_size

class Ant():
    def __init__(self,x,y,color,face,pheromone):
        self.x = x
        self.y = y
        self.color = color
        self.face = face
        self.pheromone = pheromone
        
    
    def ant_steps(self):
        if direction[self.face] == "UP":
            self.y += box_size
        elif direction[self.face] == "DOWN":
            self.y -= box_size
        elif direction[self.face] == "LEFT":
            self.x -= box_size
        elif direction[self.face] == "RIGHT":
            self.x += box_size
        
    def turn_left(self):
        self.face = (self.face+1)%4
    
    def turn_right(self):
        self.face = (self.face+3)%4

screen = pygame.display.set_mode((breadth,length))

grid_color = np.zeros((breadth, length))
grid_pheromone = np.zeros((breadth, length,2))



ant1 = Ant(breadth//2+box_size,length//2,ANT1_COLOR,0,1)
ant2 = Ant(breadth//2-box_size,length//2,ANT2_COLOR,0,1)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    for i in range(cols):
        for j in range(rows):
            if grid_color[i][j] == 0:
                color = WHITE
            elif grid_color[i][j] == 1:
                pheromone_level = grid_pheromone[i][j][1]
                shade = int(255 * (pheromone_level / 5)) #( to change the shade with pheromone for visualization)
                color = (0, 0, shade)
            elif grid_color[i][j] == 2:
                pheromone_level = grid_pheromone[i][j][1]
                shade = int(255 * (pheromone_level / 5))
                color = (shade,0, 0)
            
            #setting the grid in the screen
            pygame.draw.rect(screen, color, (i * box_size, j * box_size, box_size, box_size))
            pygame.draw.rect(screen,color,(i*box_size,j*box_size,box_size,box_size))
            pygame.draw.rect(screen,(150,190,190),(i*box_size,j*box_size,box_size,box_size),1)
    
            
    # changing the grid color

    grid_color[ant1.x//box_size][ant1.y//box_size] = 1-grid_color[ant1.x//box_size][ant1.y//box_size]
    grid_color[ant2.x//box_size][ant2.y//box_size] = 2-grid_color[ant2.x//box_size][ant2.y//box_size]
    
    
    # there can be three cases like no pheromone is there 
    #ant1 pheromone can be there 
    #ant2 pheromone can be there
    
    
    if(grid_pheromone[ant1.x//box_size][ant1.y//box_size][0]==0):
        if grid_color[ant1.x//box_size][ant1.y//box_size] == 0:
            ant1.turn_right()
        else:
            ant1.turn_left()
    
    if(grid_pheromone[ant1.x//box_size][ant1.y// box_size][0]==1):
        if random.random()>0.8*grid_pheromone[i][j][1]/5:
            if grid_color[ant1.x//box_size][ant1.y//box_size] == 0:
                ant1.turn_right()
            else:
                ant1.turn_left()
    
    if(grid_pheromone[ant1.x//box_size][ant1.y// box_size][0]==2): 
        if random.random()>1-0.8*grid_pheromone[i][j][1]/5:
            if grid_color[ant1.x//box_size][ant1.y//box_size] == 0:
                ant1.turn_right()
            else:
                ant1.turn_left()

    # same for ant 2

    if(grid_pheromone[ant2.x//box_size][ant2.y//box_size][0]==0):
        if grid_color[ant2.x//box_size][ant2.y//box_size] == 0:
            ant2.turn_right()
        else:
            ant2.turn_left()
    
    if(grid_pheromone[ant2.x//box_size][ant2.y// box_size][0]==2):
        a = random.random()> 0.8*grid_pheromone[i][j][1]/5
        if a:
            if grid_color[ant2.x//box_size][ant2.y//box_size] == 0:
                ant2.turn_right()
            else:
                ant2.turn_left()        
    
    if(grid_pheromone[ant2.x//box_size][ant2.y// box_size][0]==1):
        a = random.random()>1-0.8*grid_pheromone[i][j][1]/5
        if a:
            if grid_color[ant2.x//box_size][ant2.y//box_size] == 0:
                ant2.turn_right()
            else:
                ant2.turn_left()            
                        
    # TO UPDATE THE PHEROMONE COUNT AS IT DECAYS
    for p in range(cols):
        for q in range(rows):
            if (grid_pheromone[p][q][1]>0):
                grid_pheromone[p][q][1] -= 1 
              

    ant1.ant_steps()
    ant2.ant_steps()

    grid_pheromone[ant1.x//box_size][ant1.y//box_size] = [1,5]
    grid_pheromone[ant2.x//box_size][ant2.y//box_size]= [2,5]
       
    pygame.display.flip()
    pygame.time.delay(50)
    


pygame.quit()