import random
from string import ascii_letters


#Comment out if not using
import matplotlib.pyplot as plt
import numpy

# General setup shit put all seats in
NUM_ROWS = 33
NUM_SEATS = 6


def intalize_render():
    

    #Absolute mess of code
    image = []
    for i in range(NUM_SEATS+1):
        subimage = []
        for k in range(NUM_ROWS):
            if k % 2 == 0:
                subimage.append(-1) 
            else:
                subimage.append(0)
            
        image.append(subimage)
            

    fig,ax = plt.subplots(1,1)
    plt.set_cmap('OrRd')
    
    image = numpy.array(image)

    im = ax.imshow(image)
    
    ax.set_yticks(numpy.arange(0.5, NUM_SEATS+1.5, 1).tolist(), minor=False)
    ax.yaxis.grid(True, which='major')
    ax.set_yticklabels(['Row A','Row B','Row C','Aisle','Row D','Row E','Row F'])
    ax.set_ylim(top=-0.5)


    ax.set_xticks(numpy.arange(0.5, NUM_ROWS+.5, 1).tolist(), minor=False)
    ax.xaxis.grid(True, which='major')

    xticklist = []
    #Create list of numbers between 
    for i in range(NUM_ROWS):
        if ((i+1) % 5 == 0) and (i != 0):
            xticklist.append(str(i+1))
        else:
            xticklist.append('')
        
    ax.set_xticklabels(xticklist)
    ax.set_xlim(left=-0.5)
    
    return im,fig
def update_render(seat_plan):
    
    visualizer = []
   
    for i,column in enumerate(seat_plan):
        visualizer.append([])
        for seats in column:
            if seats[0] != -1 :
                visualizer[i].append(0)
            else: visualizer[i].append(-1)
        
                    
                    
   
    im.set_data(visualizer)
    fig.canvas.draw_idle()
    plt.pause(1) 
    
    
im,fig = intalize_render()


# initialize seating plan
seating_plan = [[ [0,0] for _ in range(NUM_ROWS)] for _ in range(NUM_SEATS + 1)]
seating_plan[3]=[[-1,0]  for _ in range(NUM_ROWS)]


seated = []


TIME_STEP = 0.1
move_time = 0.4
total_time=0

#print(seating_plan)


def move_up():
    
            
    if aisles-1 > 0:
        
        if seating_plan[aisles-1][seat][0] == -1:
            seating_plan[aisles-1][seat] = seating_plan[aisles][seat]
            seating_plan[aisles-1][seat][1] = 0
            seating_plan[aisles][seat] = [-1,0]
                
def move_down():
    
    if aisles+1 < NUM_SEATS :
        
        if seating_plan[aisles+1][seat][0] == -1:
            seating_plan[aisles+1][seat] = seating_plan[aisles][seat]
            seating_plan[aisles+1][seat][1] = 0
            seating_plan[aisles][seat] = [-1,0]
            
            
            
def move_left():
    #You can only move left the plane if in the aisle
    if aisles == 3:
        if seat-1 >= 0:
            if seating_plan[aisles][seat-1][0] == -1:
                seating_plan[aisles][seat-1] = seating_plan[aisles][seat]
                seating_plan[aisles][seat-1][1] = 0
                seating_plan[aisles][seat] = [-1,0]
                
                

while True:
    
    #Exit square
    
    for aisles in (reversed(range(len(seating_plan)))):
        print(aisles)
        for seat in (range(len(seating_plan[aisles]))):
            if seating_plan[aisles][seat][1] >= 0.4 and seating_plan[aisles][seat][0] == 0:
                #Move the p
                move_up()
                
                #Move all blocks left
                move_left()
                
            #Remove player if in sqare
            if (aisles == 3) and (seat == 0):
                seating_plan[aisles][seat] = [-1,0]
                
            #Incrasese internal clock
            seating_plan[aisles][seat][1] += 0.1
                
                
             
            
            
            
           
            
            
            
    
    
        
        
        
        
        
        
        
                    
            
            
        
        
        
        
    
    #seating_plan[3][NUM_ROWS - current_row-1][3] += TIME_STEP
        
                    
    total_time += TIME_STEP
    '''           
    if len(seated) == NUM_ROWS * NUM_SEATS:
        break
        '''    
    
        
    '''if seating_plan[3][0] == '' and len(boardingQueue)!=0:
        #Set first place in isle to the first passenger in the seat data seating_plan[3] then remove it from seat data
        seating_plan[3][0] = boardingQueue[0]  
        boardingQueue.pop(0)'''
        
       
    #Update render comment out if not using
    update_render(seating_plan)