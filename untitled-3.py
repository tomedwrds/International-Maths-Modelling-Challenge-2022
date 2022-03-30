
import random
import matplotlib.pyplot as plt
import numpy

#Data csv
#import csv
#fields = []
#rows = []
#index = []
#Add the indexing
#for i in range(10):
    #   index.append(i)

#rows.append(index)


# General setup shit put all seats in
NUM_ROWS = 14
NUM_SEATS = 24
# all measured in standard units (m,s,m/s etc)
AVERAGE_WALKING_SPEED = 0.8
AVERAGE_SEAT_PITCH = 0.78
TIME_TO_MOVE = AVERAGE_SEAT_PITCH / AVERAGE_WALKING_SPEED
FAMILY_TIME_TO_MOVE = 1.3 * TIME_TO_MOVE
NON_FAMILY_TIME_TO_MOVE = TIME_TO_MOVE
TIME_TO_STOW = 5
TIME_TO_SIT_OR_STAND = 2.5
TIME_TO_MOVE_PAST_SEAT = 2
BAG_COEFFICIENT = (20,80,10)
NAUGHTY_BOY_COEFFICIENT = 0.1
N_TEST_CASES = 1
# proportions of group sizes
SINGLE_PRINGLE_COEFFICIENT = 70
COUPLES_COEFFIENCT = 20
THREESOME_COEFFICIENT = 10
VISUALIZER = False
TIME_STEP = 1
AISLE = [3,10,17,24]



p=1


def intalize_render():


    #Absolute mess of code
    image = []
    for i in range(NUM_SEATS+len(AISLE)):
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


    ax.set_yticks(numpy.arange(0.5, NUM_SEATS+len(AISLE)+0.5, 1).tolist(), minor=False)
    ax.yaxis.grid(True, which='major')
    ax.set_yticklabels(['Row A','Row B','Row C','Aisle','Row D','Row E','Row F','g','h','i','AISLE','j','k','h','l','m','n','AISLE','q','r','p','s','t','u','AISLE','v','w','x'])
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
            if i not in AISLE:
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
    for aisle in AISLE:
        if abs(passenger[1] - aisle) == 1:
            time_to_stop_blocking_aisle += TIME_TO_MOVE_PAST_SEAT
    # middle or window seat: people are in the way
    else:

        for aisle in AISLE:

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

    for aisle in AISLE:

        if abs(passenger[1]-aisle) <= 3:

            correct_aisle = aisle
            break


    if passenger[1] > correct_aisle:    
        if [passenger[0],passenger[1]] not in passengers_loaded_bags:
            nbins = lockers[AISLE.index(correct_aisle)][NUM_ROWS-current_row-1][1]
            lockers[AISLE.index(correct_aisle)][NUM_ROWS-current_row-1][1] += passenger[2]
            passengers_loaded_bags.append([passenger[0],passenger[1]])
        else:
            nbins = lockers[AISLE.index(correct_aisle)][NUM_ROWS-current_row-1][0]-passenger[2]
    else:

        if [passenger[0],passenger[1]] not in passengers_loaded_bags:
            nbins = lockers[AISLE.index(correct_aisle)][NUM_ROWS-current_row-1][0]
            lockers[AISLE.index(correct_aisle)][NUM_ROWS-current_row-1][0] += passenger[2]
            passengers_loaded_bags.append([passenger[0],passenger[1]])
        else:
            nbins = lockers[AISLE.index(correct_aisle)][NUM_ROWS-current_row-1][0]-passenger[2]
    # derivations in writeup


    if passenger[2] == 1:
        t = (4)/(1-(0.8*nbins)/6)    
    if passenger[2] == 2:
        t = (4)/(1-(0.8*nbins)/6) + (2.25)/(1-(nbins+1)/6)
        
    return t

# board the plane
def board_the_plane(boardingQueue, aisles, family=False):

    # initialize seating plan
    seating_plan =  [[-1 for _ in range(NUM_ROWS)] for _ in range(NUM_SEATS + len(aisles))]
    for aisle in AISLE:
        seating_plan[aisle]=['' for _ in range(NUM_ROWS)]
    seated = []
    top_queue = ['' for _ in range(NUM_SEATS+len(AISLE))]
    #print(top_queue)

    lockers = [[[0,0] for i in range(NUM_ROWS)] for j in range(len(aisles))]
    passengers_loaded_bags = []

    #print(seating_plan)
    p=1
    total_time=0

    # this is false for all scenarios except where families are prioritized
    if family == False:
        time_to_move = TIME_TO_MOVE
    else:
        time_to_move = FAMILY_TIME_TO_MOVE

    while True:

        #print('new time')
        #print(top_queue)
        #print(seating_plan

        # loop through top queue
        for current_column, passenger in enumerate(reversed(top_queue)):
            #print(current_column)

            if passenger != '':

                # increase internal clock
                passenger[3] += TIME_STEP

                # check if passenger in right aisle and thus they can seat

                if (NUM_SEATS+len(AISLE)-current_column-1) in AISLE and abs(passenger[1]-(NUM_SEATS+len(AISLE)-current_column-1))<=3:  

                    # move into aisle
                    if seating_plan[NUM_SEATS+len(AISLE)-current_column-1][0] == '' and passenger[3] >= time_to_move:
                        p+=1
                        #reset internal clock
                        passenger[3]=0
                        seating_plan[NUM_SEATS+len(AISLE)-current_column-1][0] = passenger
                        top_queue[NUM_SEATS+len(AISLE)-current_column-1]=''   
       

                else:

                    # if passenger in front has moved
                    if top_queue[NUM_SEATS+len(AISLE)-current_column] == '' and passenger[3] >= time_to_move:
                        # move people along
                        top_queue[NUM_SEATS+len(AISLE)-current_column] = passenger
                        top_queue[NUM_SEATS+len(AISLE)-current_column-1] = ''

                        # reset internal clock
                        passenger[3] = 0                 



        for aisle in aisles:

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
                            time_to_stop_blocking_aisle[5]
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

        if len(seated) == NUM_ROWS * NUM_SEATS:
            return total_time


        if top_queue[0] == '' and len(boardingQueue)!=0:


            # only considered in method where families board first. 
            if family == True and boardingQueue[0] == 'b':
                time_to_move = NON_FAMILY_TIME_TO_MOVE
                boardingQueue.pop(0)

            #Set first place in isle to the first passenger in the seat data seating_plan[3] then remove it from seat data
            top_queue[0] = boardingQueue[0]  
            boardingQueue.pop(0)

        #print(len(seated))
        #for row in seating_plan:
            #print(row)
        #Update render comment out if not using
                         









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







def create_boarding_order_for_section_but_with_groups(boarding_section, other_section1, other_section2, start_row, end_row):
    current_group_member = 0
    current_group_section = 1
    current_group_size = 1
    boarding_section.append([])
    
    for row in range(start_row,end_row+1):
        for seat in range(0,NUM_SEATS+len(AISLE)):

            if seat not in AISLE:
                
                current_group_member += 1
                
                if current_group_section == 1:
                    boarding_section[-1].append([row,seat,assign_luggage(),0])
                elif current_group_section == 2:
                    other_section1[-1].append([row,seat,assign_luggage(),0])
                elif current_group_section == 3:
                    other_section2[-1].append([row,seat,assign_luggage(),0])
                
                
                
                
                if current_group_member == current_group_size: 
                    
                    
                    for aisle in AISLE:
                
                
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



# ----------------
# BOARDING METHODS
# ----------------

# boarding in random order
def random_boarding():

    test_cases = []
    for _ in range(N_TEST_CASES):
        boardingQueue = []
        for row in range(1,NUM_ROWS+1):
            for seat in range(NUM_SEATS+len(AISLE)):

                # assign bag based on probability that passenger has bag
                if seat not in AISLE: boardingQueue.append([row,seat,assign_luggage(),0])

        random.shuffle(boardingQueue)

        test_cases.append(board_the_plane(boardingQueue, AISLE))

    print('Random: ', sum(test_cases)/len(test_cases))




def random_boarding_with_groups():

    test_cases = []
    for _ in range(N_TEST_CASES):
        boardingQueue = [[]]

        current_group_member=0
        current_group_size = group_size((SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,THREESOME_COEFFICIENT))

        for row in range(1,NUM_ROWS+1):


            for seat in range(0,NUM_SEATS+len(AISLE)):

                if seat not in AISLE: boardingQueue[-1].append([row,seat,assign_luggage(),0])

                current_group_member += 1

                if current_group_member == current_group_size: 

                    for aisle in AISLE:
                        
                        
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

        test_cases.append(board_the_plane(boardingQueue, AISLE))

    print('Random with groups: ', sum(test_cases)/len(test_cases))


# sectional boarding but with groups
def section_boarding_with_groups():
    
    test_cases = []
    amf, fma = [],[]
    for _ in range(N_TEST_CASES):
        
        aft,middle,front = [],[],[]
        
        # aft section
        create_boarding_order_for_section_but_with_groups(aft,middle,front,10,14)                
        # middle section
        create_boarding_order_for_section_but_with_groups(middle,aft,front,6,9)   
        # front section
        create_boarding_order_for_section_but_with_groups(front,middle,aft,1,5)        
               
        
        random.shuffle(aft)
        random.shuffle(middle)
        random.shuffle(front)
        
        
        #print(boardingQueue)
        
        boardingQueue = aft+middle+front
        boardingQueue = [j for sub in boardingQueue for j in sub]        
        amf.append(board_the_plane(boardingQueue,AISLE))
        boardingQueue = front+middle+aft
        boardingQueue = [j for sub in boardingQueue for j in sub]        
        fma.append(board_the_plane(boardingQueue,AISLE))

        
    print('Sectional amf: ', average(amf))
    print('Sectional fma: ', average(fma))
     




# field names add whatever field names that you are creating data for 
fields = ['Index','Random','amf','afm','maf','mfa','fma','fam'] 

if VISUALIZER: im,fig = intalize_render()

#random_boarding()
#section_boarding()
#seat_boarding()
#random_boarding_with_groups()
section_boarding_with_groups()
#prioritize_groups_boarding()
#steffen_deeznuts()
#steffen_bofa_method()


#Makes the shit into colums honestly magic
#rows = zip(*rows)
#Create the rows
#with open('sectionsdata.csv', 'w', newline='') as f:

    # using csv.writer method from CSV package
    #write = csv.writer(f)

    #write.writerow(fields)

    #write.writerows(rows)


