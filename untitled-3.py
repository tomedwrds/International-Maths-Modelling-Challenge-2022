
import random
import matplotlib.pyplot as plt
import numpy
import math

# visualizer things

def intalize_render():

    #Absolute mess of code
    image = []
    for i in range(NUM_SEATS+len(AISLES)):
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
    number_of_runs = range(1,NUM_ROWS)    # use your actual number_of_runs
    ax.set_xticks(number_of_runs, minor=False)
    ax.xaxis.grid(True, which='major')


    ax.set_yticks(numpy.arange(0.5, NUM_SEATS+len(AISLES)+0.5, 1).tolist(), minor=False)
    ax.yaxis.grid(True, which='major')
    ax.set_yticklabels(['Row A','Row B','Row C','Aisle','Row D','Row E','Row F','g','h','i','AISLES','j','k','h','l','m','n','AISLES','q','r','p','s','t','u','AISLES','v','w','x'])
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
            if i not in AISLES:
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








# --------
# stuff to board the plane with (given a boarding queue)
# --------

# calculate time taken to get to seat if someone in the way
def get_past_people(seating_plan, passenger, current_row):

    # number of people blocking seats
    N=0
    time_to_stop_blocking_aisle = 0


    # aisle seat
    for aisle in AISLES:
        if abs(passenger[1] - aisle) == 1:
            time_to_stop_blocking_aisle += TIME_TO_MOVE_PAST_SEAT
    # middle or window seat: people are in the way
    else:

        for aisle in AISLES:

            if passenger[1]-aisle == -3:


                # if aisle seat taken IMPORTANT to check aisle seat first so f is maximised
                if seating_plan[passenger[1]+1][NUM_ROWS-current_row-1] != -1:
                    N+=1
                    f=1
                # if middle seat taken
                if seating_plan[passenger[1]+2][NUM_ROWS-current_row-1] != -1:
                    N+=1
                    f=2

                break

            elif passenger[1]-aisle == -2:

                # if aisle seat taken
                if seating_plan[passenger[1]+1][NUM_ROWS-current_row-1] != -1:
                    N+=1
                    f=1        

            # window seat F
            elif passenger[1]-aisle == 3:
                # if aisle seat taken IMPORTANT to check aisle seat first so f is maximised
                if seating_plan[passenger[1]-2][NUM_ROWS-current_row-1] != -1:
                    N+=1
                    f=1
                # if middle seat taken
                if seating_plan[passenger[1]-1][NUM_ROWS-current_row-1] != -1:
                    N+=1
                    f=2

            # middle seat B
            elif passenger[1] == 2:
                # if aisle seat taken
                if seating_plan[passenger[1]-1][NUM_ROWS-current_row-1] != -1:
                    N+=1
                    f=1      


        if N==0:
            time_to_stop_blocking_aisle = TIME_TO_MOVE_PAST_SEAT
        else:
            time_to_stop_blocking_aisle += TIME_TO_SIT_OR_STAND + TIME_TO_MOVE_PAST_SEAT*(N+f+1)  

    return time_to_stop_blocking_aisle, N
# stow in overhead lockers
def check_locker_space(passenger, current_row, lockers, passengers_loaded_bags, aisle=0):

    # if passenger has no baggage
    if passenger[2] == 0:
        return 0

    # if on right side of aisle

    for aisle in AISLES:

        if abs(passenger[1]-aisle) <= 3:

            correct_aisle = aisle
            break


    if passenger[1] > correct_aisle:    
        if [passenger[0],passenger[1]] not in passengers_loaded_bags:
            nbins = lockers[AISLES.index(correct_aisle)][NUM_ROWS-current_row-1][1]
            lockers[AISLES.index(correct_aisle)][NUM_ROWS-current_row-1][1] += passenger[2]
            passengers_loaded_bags.append([passenger[0],passenger[1]])
        else:
            nbins = lockers[AISLES.index(correct_aisle)][NUM_ROWS-current_row-1][0]-passenger[2]
    else:

        if [passenger[0],passenger[1]] not in passengers_loaded_bags:
            nbins = lockers[AISLES.index(correct_aisle)][NUM_ROWS-current_row-1][0]
            lockers[AISLES.index(correct_aisle)][NUM_ROWS-current_row-1][0] += passenger[2]
            passengers_loaded_bags.append([passenger[0],passenger[1]])
        else:
            nbins = lockers[AISLES.index(correct_aisle)][NUM_ROWS-current_row-1][0]-passenger[2]
    # derivations in writeup


    if passenger[2] == 1:
        t = (4)/(1-(0.8*nbins)/6)    
    if passenger[2] == 2:
        t = (4)/(1-(0.8*nbins)/6) + (2.25)/(1-(nbins+1)/6)
        
    return t

# board the plane
def board_the_plane(boardingQueue, family=False):
    print('boarding the plane')

    # initialize seating plan, top queue (if multiple aisles) and overhead lockers
    seating_plan =  [[-1 for _ in range(NUM_ROWS)] for _ in range(NUM_SEATS + len(AISLES))]
    for aisle in AISLES:
        seating_plan[aisle]=['' for _ in range(NUM_ROWS)]
    top_queue = ['' for _ in range(NUM_SEATS+len(AISLES))]
    lockers = [[[0,0] for i in range(NUM_ROWS)] for j in range(len(AISLES))]
    seated = []
    passengers_loaded_bags = []

    n_passengers = len(boardingQueue)
    
    total_time=0

    # this is false for all scenarios except where families are prioritized
    if family == False:
        time_to_move = TIME_TO_MOVE
    else:
        time_to_move = FAMILY_TIME_TO_MOVE

    while True:
        
        #print(seating_plan)

        # loop through top queue
        for current_column, passenger in enumerate(reversed(top_queue)):
            
            if passenger != '':

                # increase internal clock
                passenger[3] += TIME_STEP

                # check if passenger in right aisle and thus they can seat
                if (NUM_SEATS+len(AISLES)-current_column-1) in AISLES and abs(passenger[1]-(NUM_SEATS+len(AISLES)-current_column-1))<=AISLES[0]+1:  

                    # move into aisle
                    if seating_plan[NUM_SEATS+len(AISLES)-current_column-1][0] == '' and passenger[3] >= time_to_move:
                        #reset internal clock
                        passenger[3]=0
                        seating_plan[NUM_SEATS+len(AISLES)-current_column-1][0] = passenger
                        top_queue[NUM_SEATS+len(AISLES)-current_column-1]=''   

                else:
                    # if passenger in front has moved
                    if top_queue[NUM_SEATS+len(AISLES)-current_column] == '' and passenger[3] >= time_to_move:
                        # move people along
                        top_queue[NUM_SEATS+len(AISLES)-current_column] = passenger
                        top_queue[NUM_SEATS+len(AISLES)-current_column-1] = ''

                        # reset internal clock
                        passenger[3] = 0                 
                
        for aisle in AISLES:

            # loop through aisle from back to front
            for current_row,passenger in enumerate(reversed(seating_plan[aisle])):

                if passenger != '':

                    # increase internal clock
                    #print(seating_plan[aisle])
                    passenger[3] += TIME_STEP

                    # check if passenger in right row and thus they can seat
                    if passenger[0] == NUM_ROWS - current_row:

                        # if passenger has baggage
                        time_to_stow = check_locker_space(passenger, current_row, lockers,passengers_loaded_bags)


                        # time it takes to stop blocking aisle and number of people in the way
                        try:
                            time_to_stop_blocking_aisle=passenger[5]
                        except:
                            time_to_stop_blocking_aisle, N = get_past_people(seating_plan, passenger, current_row)   
                            passenger.append(time_to_stop_blocking_aisle)


                        # make sure there is an empty space       
                        if N==2 and current_row != 0 and seating_plan[aisle][NUM_ROWS-current_row] != '' and current_row != 0:
                            time_to_wait_for_spot_in_aisle += time_to_move - passenger[3]
                        else:
                            time_to_wait_for_spot_in_aisle=0


                        # if time to wait has finished i.e. SIT DOWN BE HUMBLE
                        if passenger[3] >= time_to_stop_blocking_aisle + time_to_stow + time_to_wait_for_spot_in_aisle:

                            seating_plan[passenger[1]][passenger[0]-1] = passenger
                            seated.append(passenger)
                            #print(seated)

                            # set queue place to empty
                            seating_plan[aisle][NUM_ROWS-current_row-1]=''
                            


                    else:
                        # if passenger in front has moved
                        if seating_plan[aisle][NUM_ROWS-current_row] == '' and passenger[3] >= time_to_move:
                            # move people along
                            seating_plan[aisle][NUM_ROWS-current_row] = passenger
                            seating_plan[aisle][NUM_ROWS-current_row-1] = ''

                            # reset internal clock
                            seating_plan[aisle][NUM_ROWS - current_row][3] = 0
            
                if VISUALIZER: update_render(seating_plan)  


        total_time += TIME_STEP    

        if len(seated) == n_passengers:
            print(len(seated))
            return total_time


        if top_queue[0] == '' and len(boardingQueue)!=0:


            # only considered in method where families board first. 
            if family == True and boardingQueue[0] == 'b':
                time_to_move = NON_FAMILY_TIME_TO_MOVE
                boardingQueue.pop(0)

            #Set first place in isle to the first passenger in the seat data seating_plan[3] then remove it from seat data
            top_queue[0] = boardingQueue[0]  
            boardingQueue.pop(0)


# luggage
def assign_luggage():
    return random.choices([0,1,2], weights=BAG_COEFFICIENT, k=1)[0]

# naughty boy
def is_not_a_naughty_boy():
    return random.randrange(100) > NAUGHTY_BOY_COEFFICIENT*100
# create a group size
def group_size(group_weights):

    return random.choices([1,2,3], weights=group_weights, k=1)[0]

# return average of list
def average(x):
    return sum(x)/len(x)







# create order of boarding 
def create_boarding_order_for_section_but_with_groups(boarding_section, other_section1, other_section2, start_row, end_row):
    current_group_member = 0
    current_group_section = 1
    current_group_size = 1
    boarding_section.append([])
    
    for row in range(start_row,end_row+1):
        for seat in range(0,NUM_SEATS+len(AISLES)):

            if seat not in AISLES:
                
                current_group_member += 1
                
                if current_group_section == 1:
                    boarding_section[-1].append([row,seat,assign_luggage(),0])
                elif current_group_section == 2:
                    other_section1[-1].append([row,seat,assign_luggage(),0])
                elif current_group_section == 3:
                    other_section2[-1].append([row,seat,assign_luggage(),0])
                
                
                
                
                if current_group_member == current_group_size: 
                    
                    
                    for aisle in AISLES:
                
                
                        if seat-aisle in [2,3]:
                            if current_group_section == 1:
                                boarding_section[-1].reverse()
                            elif current_group_section == 2:
                                other_section1[-1].reverse()
                            elif current_group_section == 3:
                                other_section2[-1].reverse()       
                
                        if seat-aisle in [-3,-2,1]:
                            current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,THREESOME_COEFFICIENT))
                        elif seat-aisle in [-1,2]:
                            current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,0))
                        elif seat == 6:
                            current_group_size = 1                    
                        
                        current_group_member = 0   
                    
                    
                    if is_not_a_naughty_boy():
                
                        current_group_section = 1
                        boarding_section.append([])              
                
                
                    # else they try board during different sections
                    else:
                        if random.randrange(100) < 50:
                            current_group_section = 2
                            other_section1.append([])  
                        else:
                            current_group_section = 3
                            other_section2.append([])                     




# create order of boarding for doing windows first using groups
def create_boarding_order_for_aisle_but_with_groups(boarding_section, other_section1, other_section2, seats):
    
    
    for seat in seats:
        # window seats
        for row in range(1,NUM_ROWS+1):
            
            
            
            # check if item in group already appended
            if (not any([row,seat] in x for x in boarding_section) 
                and not any([row,seat] in x for x in other_section1)
                and not any([row,seat] in x for x in other_section2)):  
                
                # if passenger is not useless
                if is_not_a_naughty_boy():
                    
                
                    for aisle in AISLES:
                        
                        if aisle-seat == 3:

                            current_group_size = group_size((70,50,20))
                
                            if current_group_size == 3:
                                boarding_section.append([[row, seat],[row, seat+1],[row, seat+2]])
                            elif current_group_size == 2:    
                                boarding_section.append([[row, seat],[row, seat+1]])
                            else:    
                                boarding_section.append([[row, seat]])
                        elif aisle-seat==-3:
                            current_group_size = group_size((70,50,20))
                
                            if current_group_size == 3:
                                boarding_section.append([[row, seat],[row, seat-1],[row, seat-2]])
                            elif current_group_size == 2:    
                                boarding_section.append([[row, seat],[row, seat-1]])
                            else:    
                                boarding_section.append([[row, seat]])            
         
                        elif aisle-seat==2:
                            current_group_size = group_size((80,40,0))
                            if current_group_size == 2:    
                                boarding_section.append([[row, seat],[row, seat+1]])
                            else:    
                                boarding_section.append([[row, seat]])   
                        elif aisle-seat==-2:
                            current_group_size = group_size((80,40,0))
                            if current_group_size == 2:    
                                boarding_section.append([[row, seat],[row, seat-1]])
                            else:    
                                boarding_section.append([[row, seat]])               
                
                
                        else: boarding_section.append([[row, seat]]) 
                        
                        break
    
            # else they try board during different sections    
            else:
                if random.randrange(100) < 50:
                    other_section1.append([[row, seat]])  
                else:
                    other_section2.append([[row, seat]])       


# reduce boarding queue capacity due to Covid
def cull_boarding_queue(boarding_queue):
    target_to_kill = math.floor((1-THANOS_COEFFICIENT)*NUM_SEATS)
    print(target_to_kill)
    for row in range(NUM_ROWS):  
        
        killed = 0
        for index,passenger in enumerate(boarding_queue): 
            if passenger[0] == row:
                killed += 1
                del boarding_queue[index]
            if killed==target_to_kill:
                break
    print(len(boarding_queue))          
    return boarding_queue
                
                    
    
    



# ----------------
# BOARDING METHODS
# ----------------

# boarding in random order
def random_boarding():

    test_cases = []
    for _ in range(N_TEST_CASES):
        boardingQueue = []
        for row in range(1,NUM_ROWS+1):
            for seat in range(NUM_SEATS+len(AISLES)):

                # assign bag based on probability that passenger has bag
                if seat not in AISLES: boardingQueue.append([row,seat,assign_luggage(),0])

        random.shuffle(boardingQueue)

        test_cases.append(board_the_plane(boardingQueue, AISLES))

    print('Random: ', sum(test_cases)/len(test_cases))




def random_boarding_with_groups():

    test_cases = []
    for _ in range(N_TEST_CASES):
        boardingQueue = [[]]

        current_group_member=0
        current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,THREESOME_COEFFICIENT))

        for row in range(1,NUM_ROWS+1):


            for seat in range(0,NUM_SEATS+len(AISLES)):

                if seat not in AISLES: boardingQueue[-1].append([row,seat,assign_luggage(),0])

                current_group_member += 1

                if current_group_member == current_group_size: 

                    for aisle in AISLES:
                        
                        
                        if seat-aisle in [2,3]:
                            boardingQueue[-1].reverse()

                        if seat-aisle in [-3,-2,1]:
                            current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,THREESOME_COEFFICIENT))
                        elif seat-aisle in [-1,2]:
                            current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,0))
                        elif seat == 6:
                            current_group_size = 1

                        current_group_member = 0
                        boardingQueue.append([])    
                        
                        break



        random.shuffle(boardingQueue)

        # flatten groups

        boardingQueue = [j for sub in boardingQueue for j in sub]

        #print(boardingQueue)
        
        boardingQueue = cull_boarding_queue(boardingQueue)

        test_cases.append(board_the_plane(boardingQueue))

    print('Random with groups: ', sum(test_cases)/len(test_cases))


# sectional boarding but with groups
def section_boarding_with_groups():
    
    test_cases = []
    amf, fma = [],[]
    for _ in range(N_TEST_CASES):
        
        aft,middle,front = [],[],[]
        
        # aft section
        create_boarding_order_for_section_but_with_groups(aft,middle,front,A_SEC_START,A_SEC_END)                
        # middle section
        create_boarding_order_for_section_but_with_groups(middle,aft,front,M_SEC_START,M_SEC_END)   
        # front section
        create_boarding_order_for_section_but_with_groups(front,middle,aft,F_SEC_START,F_SEC_END)        
               
        
        random.shuffle(aft)
        random.shuffle(middle)
        random.shuffle(front)
        
        
        #print(boardingQueue)
        
        boardingQueue = aft+middle+front
        boardingQueue = [j for sub in boardingQueue for j in sub]        
        amf.append(board_the_plane(boardingQueue))
        boardingQueue = front+middle+aft
        boardingQueue = [j for sub in boardingQueue for j in sub]        
        fma.append(board_the_plane(boardingQueue))

        
    print('Sectional amf: ', average(amf))
    print('Sectional fma: ', average(fma))



# boarding by seat but allowing groups to board together
def seat_boarding_with_groups():
    
    test_cases = []
    for _ in range(N_TEST_CASES):
        
        window,middle,aisle = [],[],[]

        # window seats
        window_seats = [aisle-3 for aisle in AISLES] + [aisle+3 for aisle in AISLES]
        create_boarding_order_for_aisle_but_with_groups(window,middle,aisle,window_seats)
        # middle seats
        middle_seats = [aisle-2 for aisle in AISLES] + [aisle+2 for aisle in AISLES]
        create_boarding_order_for_aisle_but_with_groups(middle,window,aisle,middle_seats) 
        # aisle seats
        aisle_seats = [aisle-1 for aisle in AISLES] + [aisle+1 for aisle in AISLES]
        create_boarding_order_for_aisle_but_with_groups(aisle,window,middle,aisle_seats)
        
        random.shuffle(window)
        random.shuffle(middle)
        random.shuffle(aisle)
    
        window = [j for sub in window for j in sub]
        middle = [j for sub in middle for j in sub]
        aisle = [j for sub in aisle for j in sub]
    
        boardingQueue = window+middle+aisle
    
        for passenger in boardingQueue:
            passenger.append(assign_luggage())
            passenger.append(0)
    
        print(boardingQueue)
    
        test_cases.append(board_the_plane(boardingQueue))

    print('By seat with groups: ', sum(test_cases)/len(test_cases))    
        



def prioritize_groups_boarding():
    
    test_cases = []
    for _ in range(N_TEST_CASES):
        mainBoardingQueue = [[]]
        priorityQueue=[]
        boardingQueue=[]
        current_group_member=0
        current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,THREESOME_COEFFICIENT))
        current_boarding_section = 2
        for row in range(1,NUM_ROWS+1):


            for seat in range(0,NUM_SEATS+len(AISLES)):

                if seat not in AISLES: 
                    
                    if current_boarding_section == 1:
                        priorityQueue[-1].append([row,seat,assign_luggage(),0])
                    else:
                        mainBoardingQueue[-1].append([row,seat,assign_luggage(),0])
    
                    current_group_member += 1
    
                    if current_group_member == current_group_size: 
    
                        for aisle in AISLES:

                    
                            if seat-aisle in [2,3]:
                                if current_boarding_section == 1:
                                    priorityQueue[-1].reverse()
                                else:
                                    mainBoardingQueue[-1].reverse()
                    
                            if seat-aisle in [-3,-2,1]:
                                current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,THREESOME_COEFFICIENT))
                            elif seat-aisle in [-1,2]:
                                current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,0))
                            elif seat-aisle == 3:
                                current_group_size = 1
                     
                    
                            break

                        current_group_member = 0
                        
                        if current_group_size == 3:
                            if random.randrange(100) > 80:
                                mainBoardingQueue.append([])
                                current_boarding_section = 2
                            else:
                                priorityQueue.append([])
                                current_boarding_section = 1
                        elif current_group_size == 2:
                            if random.randrange(100) > 20:
                                mainBoardingQueue.append([])
                                current_boarding_section = 2
                            else:
                                priorityQueue.append([])
                                current_boarding_section = 1
                        elif current_group_size == 1:   
                            if random.randrange(100) > 5:
                                mainBoardingQueue.append([])
                                current_boarding_section = 2
                            else:
                                priorityQueue.append([])
                                current_boarding_section = 1                        
                            
                                      

        random.shuffle(mainBoardingQueue)
        random.shuffle(priorityQueue)
        # flatten groups
        boardingQueue =  priorityQueue+['b']+mainBoardingQueue
        boardingQueue = [j for sub in boardingQueue for j in sub]
        
        #print(boardingQueue)

        test_cases.append(board_the_plane(boardingQueue, True))
        
    print('Priortizing groups: ', average(test_cases))



















plane = 'two entrance two aisle first class'

if plane == 'narrow body':
    NUM_ROWS = 33
    NUM_SEATS = 6    
    AISLES = [3]
    F_SEC_START = 1
    F_SEC_END = 11
    M_SEC_START = 12
    M_SEC_END = 22
    A_SEC_START = 23
    A_SEC_END = 33
elif plane == 'wide wing':
    NUM_ROWS = 14
    NUM_SEATS = 24  
    AISLES = [3,10,17,24]
    F_SEC_START = 1
    F_SEC_END = 5
    M_SEC_START = 6
    M_SEC_END = 9
    A_SEC_START = 10
    A_SEC_END = 14  
elif plane == 'two entrance two aisle':
    # simulating only the back half of the plane
    NUM_ROWS = 20
    NUM_SEATS = 7
    AISLES = [2,6]
elif plane == 'two entrance two aisle first class':
    NUM_ROWS = 3
    NUM_SEATS = 6
    AISLES = [2,5]    

# CHANGE THESE FOR SENSITIVITY
BAG_COEFFICIENT = (20,80,10)
NAUGHTY_BOY_COEFFICIENT = 0.3
THANOS_COEFFICIENT = 0.3 #0.5 or 0.7

N_TEST_CASES = 1
VISUALIZER = False
TIME_STEP = 0.1

# all measured in standard units (m,s,m/s etc)
AVERAGE_WALKING_SPEED = 0.8
AVERAGE_SEAT_PITCH = 0.78
TIME_TO_MOVE = AVERAGE_SEAT_PITCH / AVERAGE_WALKING_SPEED
FAMILY_TIME_TO_MOVE = 1.3 * TIME_TO_MOVE
NON_FAMILY_TIME_TO_MOVE = TIME_TO_MOVE
TIME_TO_SIT_OR_STAND = 2.5
TIME_TO_MOVE_PAST_SEAT = 2
# proportions of group sizes
SINGLE_PRINGLE_COEFFICIENT = 70
COUPLES_COEFFIENCT = 20
THREESOME_COEFFICIENT = 10


if VISUALIZER: im,fig = intalize_render()


# BOARDING METHODS: comment out if not using

#random_boarding()
#section_boarding()
#seat_boarding()
random_boarding_with_groups()
#section_boarding_with_groups()
#seat_boarding_with_groups()
#prioritize_groups_boarding()

# steffen methods can only be used with narrow body
#steffen_deeznuts()
#steffen_bofa_method()

