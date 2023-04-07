
import random
import matplotlib.pyplot as plt
import numpy

# General setup shit put all seats in
NUM_ROWS = 33
NUM_SEATS = 6
# all measured in standard units (m,s,m/s etc)
AVERAGE_WALKING_SPEED = 0.8
AVERAGE_SEAT_PITCH = 0.78
TIME_TO_MOVE = AVERAGE_SEAT_PITCH / AVERAGE_WALKING_SPEED
TIME_TO_STOW = 5
TIME_TO_SIT_OR_STAND = 2.5
TIME_TO_MOVE_PAST_SEAT = 2
BAG_COEFFICIENT = 0.85
NAUGHTY_BOY_COEFFICIENT = 0.05
N_TEST_CASES = 10
# proportions of group sizes
SINGLE_PRINGLE_COEFFICIENT = 70
COUPLES_COEFFIENCT = 20
THREESOME_COEFFICIENT = 10


# render stuff that I don't understand
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
    print(image)
    image = numpy.array(image)

    im = ax.imshow(image)
    #number_of_runs = range(1,NUM_ROWS)    # use your actual number_of_runs
    #ax.set_xticks(number_of_runs, minor=False)
    #ax.xaxis.grid(True, which='major')


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
        for seat in column:
            if i!=3:
                if seat != -1:
                    visualizer[i].append(0)
                else: visualizer[i].append(-1)
            else:
                if seat != '':
                    visualizer[i].append(0)
                else: visualizer[i].append(-1)
                    
                    
        
    im.set_data(visualizer)
    fig.canvas.draw_idle()
    plt.pause(0.01) 

# calculate time taken to get to seat if someone in the way
def get_past_people(seating_plan, passenger, current_row):
    
    # number of people blocking seats
    N=0
    time_to_stop_blocking_aisle = 0


    # aisle seat
    if abs(passenger[1]) == 1:
        time_to_stop_blocking_aisle += TIME_TO_SIT_OR_STAND
    # middle or window seat: people are in the way
    else:
        # window seat A
        if passenger[1] == -3:
            # if aisle seat taken IMPORTANT to check aisle seat first so f is maximised
            if seating_plan[2][NUM_ROWS-current_row-1] != -1:
                N+=1
                f=1
            # if middle seat taken
            if seating_plan[1][NUM_ROWS-current_row-1] != -1:
                N+=1
                f=2

        # middle seat B
        elif passenger[1] == -2:
            # if aisle seat taken
            if seating_plan[2][NUM_ROWS-current_row-1] != -1:
                N+=1
                f=1        

        # window seat F
        elif passenger[1] == 3:
            # if aisle seat taken IMPORTANT to check aisle seat first so f is maximised
            if seating_plan[4][NUM_ROWS-current_row-1] != -1:
                N+=1
                f=1
            # if middle seat taken
            if seating_plan[5][NUM_ROWS-current_row-1] != -1:
                N+=1
                f=2

        # middle seat B
        elif passenger[1] == 2:
            # if aisle seat taken
            if seating_plan[4][NUM_ROWS-current_row-1] != -1:
                N+=1
                f=1      


        if N==0:
            time_to_stop_blocking_aisle = TIME_TO_MOVE_PAST_SEAT
        else:
            time_to_stop_blocking_aisle += TIME_TO_SIT_OR_STAND + TIME_TO_MOVE_PAST_SEAT*(N+f+1)  
            
    return time_to_stop_blocking_aisle, N

# board the plane
def board_the_plane(boardingQueue):
    
    # initialize seating plan
    seating_plan = [[-1 for _ in range(NUM_ROWS)] for _ in range(NUM_SEATS + 1)]
    seating_plan[3]=['' for _ in range(NUM_ROWS)]
    seated = []
    
    
    TIME_STEP = 0.1
    
    total_time=0
    
    while True:
        
        # loop through aisle from back to front
        for current_row,passenger in enumerate(reversed(seating_plan[3])):
            
            if passenger != '':
                
                # increase internal clock
                seating_plan[3][NUM_ROWS - current_row-1][3] += TIME_STEP
                
                # check if passenger in right row and thus they can seat
                if passenger[0] == NUM_ROWS - current_row:
                    
                    # if passenger has baggage
                    if passenger[2] == True:
                        time_to_stow = TIME_TO_STOW
                    else: time_to_stow = 0
                    
                    # time it takes to stop blocking aisle and number of people in the way
                    try:
                        time_to_stop_blocking_aisle[5]
                    except:
                        time_to_stop_blocking_aisle, N = get_past_people(seating_plan, passenger, current_row)   
                        seating_plan[3][NUM_ROWS-current_row-1].append(time_to_stop_blocking_aisle)
                    
                    
                    # make sure there is an empty space       
                    if N==2 and current_row != 0 and seating_plan[3][NUM_ROWS-current_row] != '' and current_row != 0:
                        time_to_wait_for_spot_in_aisle += TIME_TO_MOVE - seating_plan[3][NUM_ROWS-current_row][3]
                    else:
                        time_to_wait_for_spot_in_aisle=0
                            
    
                    # if time to wait has finished
                    if seating_plan[3][NUM_ROWS - current_row-1][3] >= time_to_stop_blocking_aisle + time_to_stow + time_to_wait_for_spot_in_aisle:
    
                        seating_plan[passenger[1]+3][passenger[0]-1] = passenger
                        seated.append(passenger)
                        # set queue place to empty
                        seating_plan[3][NUM_ROWS-current_row-1]=''
                    
                    
                else:
                    # if passenger in front has moved
                    if seating_plan[3][NUM_ROWS-current_row ] == '' and seating_plan[3][NUM_ROWS - current_row-1][3] >= TIME_TO_MOVE:
                        # move people along
                        seating_plan[3][NUM_ROWS-current_row] = passenger
                        seating_plan[3][NUM_ROWS-current_row-1] = ''
                        
                        # reset internal clock
                        seating_plan[3][NUM_ROWS - current_row][3] = 0
                        
        total_time += TIME_STEP
                        
        if len(seated) == NUM_ROWS * NUM_SEATS:
            break
        
            
        if seating_plan[3][0] == '' and len(boardingQueue)!=0:
            #Set first place in isle to the first passenger in the seat data seating_plan[3] then remove it from seat data
            seating_plan[3][0] = boardingQueue[0]  
            boardingQueue.pop(0)
            
            
            
        #Update render comment out if not using
        #update_render(seating_plan)                   
        
        

        
    return total_time




# luggage
def assign_luggage():
    return random.randrange(100) < BAG_COEFFICIENT*100

# naughty boy
def naughty_boy():
    return random.randrange(100) > NAUGHTY_BOY_COEFFICIENT*100
# create a group size
def group_size(group_weights):
    
    return random.choices([1,2,3], weights=group_weights, k=1)[0]


# create order of boarding for section
def create_boarding_order_for_section(boarding_section, other_section1,other_section2, start_row, end_row):
    
    for row in range(start_row,end_row+1):
        for seat in range(-3,4):

            if seat != 0:
                if naughty_boy():
                    boarding_section.append([row,seat,assign_luggage(),0]) 
                # else they try board during different sections
                else:
                    if random.randrange(100) < 50:
                        other_section1.append([row,seat,assign_luggage(),0])  
                    else:
                        other_section2.append([row,seat,assign_luggage(),0])               


# create order of boarding for section when using groups
def create_boarding_order_for_section_but_with_groups(boarding_section, other_section1, other_section2, start_row, end_row):

    for row in range(start_row,end_row+1):
        for seat in range(-3,4):

            if seat != 0:
                if not naughty_boy():
                    boarding_section.append([row,seat,assign_luggage(),0]) 
                    
                    
                    current_group_member += 1
                        
                    if current_group_member == current_group_size: 
                    
                        if  seat in [2,3]:
                            boardingQueue[-1].reverse()
                            
                        if seat in [-3,-2,1]:
                            current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,THREESOME_COEFFICIENT))
                        elif seat in [-1,2]:
                            current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,0))
                        elif seat == 3:
                            current_group_size = 1
                            
                        current_group_member = 0
                        boardingQueue.append([])                    
                                        
                    
                    
                # else they try board during different sections
                else:
                    if random.randrange(100) < 50:
                        other_section1.append([row,seat,assign_luggage(),0])  
                    else:
                        other_section2.append([row,seat,assign_luggage(),0]) 
                        
                        
                        


# boarding in random order
def random_boarding():
    
    test_cases = []
    for _ in range(N_TEST_CASES):
        boardingQueue = []
        for row in range(1,NUM_ROWS+1):
            for seat in range(-3,4):
        
                # assign bag based on probability that passenger has bag
                if seat != 0: boardingQueue.append([row,seat,assign_luggage(),0])
                
        random.shuffle(boardingQueue)
        
        test_cases.append(board_the_plane(boardingQueue))
        
    print('Random: ', sum(test_cases)/len(test_cases))
    
# boarding in sections
def section_boarding():
    
    test_cases = []
    for _ in range(N_TEST_CASES):
        
        aft,middle,front = [],[],[]
        
        # aft section
        create_boarding_order_for_section(aft,middle,front,23,33)                
        # middle section
        create_boarding_order_for_section(middle,aft,front,12,22)   
        # front section
        create_boarding_order_for_section(front,middle,aft,1,11)        
               
        
        random.shuffle(aft)
        random.shuffle(middle)
        random.shuffle(front)
        
        test_cases.append(board_the_plane(aft+middle+front))
        
    print('Sectional: ', sum(test_cases)/len(test_cases))        
        
        
# boarding by seat
def seat_boarding():
    
    test_cases = []
    for _ in range(N_TEST_CASES):
        
        section1,section2,section3 = [],[],[]
        
        # window seats
        for row in range(1,NUM_ROWS+1):
            
            # if passenger is not useless
            if naughty_boy():
                section1.append([row,-3,assign_luggage(),0]) 
            # else they try board during different sections
            else:
                if random.randrange(100) < 50:
                    section2.append([row,-3,assign_luggage(),0])  
                else:
                    section3.append([row,-3,assign_luggage(),0])  
            
            # if passenger is not useless
            if naughty_boy():
                section1.append([row,3,assign_luggage(),0]) 
            # else they try board during different sections
            else:
                if random.randrange(100) < 50:
                    section2.append([row,3,assign_luggage(),0])  
                else:
                    section3.append([row,3,assign_luggage(),0])  
            
        # middle seats 
        for row in range(1,NUM_ROWS+1):
            
            
            # if passenger is not useless
            if naughty_boy():
                section2.append([row,-2,assign_luggage(),0]) 
            # else they try board during different sections
            else:
                if random.randrange(100) < 50:
                    section1.append([row,-2,assign_luggage(),0])  
                else:
                    section3.append([row,-2,assign_luggage(),0])  

            if naughty_boy:
                section2.append([row,2,assign_luggage(),0]) 
            else:
                if random.randrange(100) < 50:
                    section1.append([row,2,assign_luggage(),0])  
                else:
                    section3.append([row,2,assign_luggage(),0])  
                    
        # aisle seats
        for row in range(1,NUM_ROWS+1):
            
            # if passenger is not useless
            if naughty_boy():
                section3.append([row,-1,assign_luggage(),0]) 
            # else they try board during different sections
            else:
                if random.randrange(100) < 50:
                    section1.append([row,-1,assign_luggage(),0])  
                else:
                    section2.append([row,-1,assign_luggage(),0])  
                    
                    
            # if passenger is not useless
            if naughty_boy:
                section3.append([row,1,assign_luggage(),0]) 
            # else they try board during different sections
            else:
                if random.randrange(100) < 50:
                    section1.append([row,1,assign_luggage(),0])  
                else:
                    section2.append([row,1,assign_luggage(),0])   
                    
                    
        #print([i[1] for i in section1])

        random.shuffle(section1)
        random.shuffle(section2)
        random.shuffle(section3)
        test_cases.append(board_the_plane(section1+section2+section3))

    print('By seat: ', sum(test_cases)/len(test_cases))    
            
    




# random boarding but with groups
def random_boarding_with_groups():
    
    test_cases = []
    for _ in range(N_TEST_CASES):
        boardingQueue = [[]]
        
        current_group_member=0
        current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,THREESOME_COEFFICIENT))

        for row in range(1,NUM_ROWS+1):
            
            
            for seat in range(-3,4):
                
                if seat != 0: boardingQueue[-1].append([row,seat,assign_luggage(),0])
                
                current_group_member += 1
                    
                if current_group_member == current_group_size: 
                
                    if  seat in [2,3]:
                        boardingQueue[-1].reverse()
                        
                    if seat in [-3,-2,1]:
                        current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,THREESOME_COEFFICIENT))
                    elif seat in [-1,2]:
                        current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,0))
                    elif seat == 3:
                        current_group_size = 1
                        
                    current_group_member = 0
                    boardingQueue.append([])                    
                    
              
                
        random.shuffle(boardingQueue)
        
        # flatten groups
        
        boardingQueue = [j for sub in boardingQueue for j in sub]
        
        print(boardingQueue)
        
        test_cases.append(board_the_plane(boardingQueue))
        
    print('Random with groups: ', sum(test_cases)/len(test_cases))


# sectional boarding but with groups
def section_boarding_with_groups():
    
    test_cases = []
    for _ in range(N_TEST_CASES):
        
        aft,middle,front = [],[],[]
        
        # aft section
        create_boarding_order_for_section(aft,middle,front,23,33)                
        # middle section
        create_boarding_order_for_section(middle,aft,front,12,22)   
        # front section
        create_boarding_order_for_section(front,middle,aft,1,11)        
               
        
        random.shuffle(aft)
        random.shuffle(middle)
        random.shuffle(front)
        
        test_cases.append(board_the_plane(aft+middle+front))
               

    print('Sectional: ', sum(test_cases)/len(test_cases))        

#im,fig = intalize_render()
random_boarding_with_groups()
random_boarding()
section_boarding()
seat_boarding()