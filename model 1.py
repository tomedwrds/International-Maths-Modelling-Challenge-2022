
import random

#General setup shit put all seats in
NUM_ROWS = 33
NUM_SEATS = 6


# all measured in standard units (meters, seconds, etc)
AVERAGE_WALKING_SPEED = 1.3
AVERAGE_SEAT_PITCH = 0.78
TIME_TO_MOVE = AVERAGE_SEAT_PITCH / AVERAGE_WALKING_SPEED
TIME_TO_STOW = 5
TIME_TO_SIT_OR_STAND = 2.5
TIME_TO_MOVE_PAST_SEAT = 2
BAG_COEFFICIENT = 0.85
# percentage of people misbehaving. if 0 then 
NAUGHTY_BOY_COEFFICIENT = 0.05
N_TEST_CASES = 10



# board the plane
def board_the_plane(boardingQueue):
    

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
                    
                    time_to_stop_blocking_aisle = 0
                    
                    # if passenger has baggage
                    if passenger[2] == True:
                        time_to_stow = TIME_TO_STOW
                    else: time_to_stow = 0
                    
                    # number of people blocking seats
                    N=0
                    
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
            
        
        visualizer = []
        for i,column in enumerate(seating_plan):
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
        
     
        
    return total_time




# boarding in random order
def random_boarding():
    
    test_cases = []
    for _ in range(N_TEST_CASES):
        boardingQueue = []
        for row in range(1,NUM_ROWS+1):
            for seat in range(-3,4):
        
                # assign bag based on probability that passenger has bag
                luggage = random.randrange(100) < BAG_COEFFICIENT*100
                if seat != 0: boardingQueue.append([row,seat,luggage,0])
        random.shuffle(boardingQueue)
        
        test_cases.append(board_the_plane(boardingQueue))
        
    print('Random: ', sum(test_cases)/len(test_cases))
    
# boarding in sections
def section_boarding():
    
    test_cases = []
    for _ in range(N_TEST_CASES):
        
        section1 = []
        for row in range(23,34):
            for seat in range(-3,4):
        
                # assign bag based on probability that passenger has bag
                luggage = random.randrange(100) < BAG_COEFFICIENT*100
                if seat != 0: section1.append([row,seat,luggage,0])
        section2 = []
        for row in range(12,23):
            for seat in range(-3,4):
    
                # assign bag based on probability that passenger has bag
                luggage = random.randrange(100) < BAG_COEFFICIENT*100
                if seat != 0: section2.append([row,seat,luggage,0]) 
        section3 = []   
        for row in range(1,12):
            for seat in range(-3,4):
    
                # assign bag based on probability that passenger has bag
                luggage = random.randrange(100) < BAG_COEFFICIENT*100
                if seat != 0: section3.append([row,seat,luggage,0])     
                
        random.shuffle(section1)
        random.shuffle(section2)
        random.shuffle(section3)
        
        test_cases.append(board_the_plane(section1+section2+section3))
        
    print('Sectional: ', sum(test_cases)/len(test_cases))        
        
        
# boarding by seat
def seat_boarding():
    
    test_cases = []
    for _ in range(N_TEST_CASES):
        
        section1,section2,section3 = [],[],[]
        
        # window seats
        for row in range(1,NUM_ROWS+1):
            
            
            luggage = random.randrange(100) < BAG_COEFFICIENT*100
            # if passenger is not useless
            if random.randrange(100) > NAUGHTY_BOY_COEFFICIENT*100:
                section1.append([row,-3,luggage,0]) 
            # else they try board during different sections
            else:
                if random.randrange(100) < 50:
                    section2.append([row,-3,luggage,0])  
                else:
                    section3.append([row,-3,luggage,0])  
            
            luggage = random.randrange(100) < BAG_COEFFICIENT*100
            # if passenger is not useless
            if random.randrange(100) > NAUGHTY_BOY_COEFFICIENT*100:
                section1.append([row,3,luggage,0]) 
            # else they try board during different sections
            else:
                if random.randrange(100) < 50:
                    section2.append([row,3,luggage,0])  
                else:
                    section3.append([row,3,luggage,0])  
            
        # middle seats 
        for row in range(1,NUM_ROWS+1):
            
            
            
            luggage = random.randrange(100) < BAG_COEFFICIENT*100
            # if passenger is not useless
            if random.randrange(100) > NAUGHTY_BOY_COEFFICIENT*100:
                section2.append([row,-2,luggage,0]) 
            # else they try board during different sections
            else:
                if random.randrange(100) < 50:
                    section1.append([row,-2,luggage,0])  
                else:
                    section3.append([row,-2,luggage,0])  
            
            luggage = random.randrange(100) < BAG_COEFFICIENT*100
            # if passenger is not useless
            if random.randrange(100) > NAUGHTY_BOY_COEFFICIENT*100:
                section2.append([row,2,luggage,0]) 
            # else they try board during different sections
            else:
                if random.randrange(100) < 50:
                    section1.append([row,2,luggage,0])  
                else:
                    section3.append([row,2,luggage,0])  
                    
        # aisle seats
        for row in range(1,NUM_ROWS+1):
            
            luggage = random.randrange(100) < BAG_COEFFICIENT*100
            # if passenger is not useless
            if random.randrange(100) > NAUGHTY_BOY_COEFFICIENT*100:
                section3.append([row,-1,luggage,0]) 
            # else they try board during different sections
            else:
                if random.randrange(100) < 50:
                    section1.append([row,-1,luggage,0])  
                else:
                    section2.append([row,-1,luggage,0])  
                    
                    
            luggage = random.randrange(100) < BAG_COEFFICIENT*100
            # if passenger is not useless
            if random.randrange(100) > NAUGHTY_BOY_COEFFICIENT*100:
                section3.append([row,1,luggage,0]) 
            # else they try board during different sections
            else:
                if random.randrange(100) < 50:
                    section1.append([row,1,luggage,0])  
                else:
                    section2.append([row,1,luggage,0])   
                    
                    
        #print([i[1] for i in section1])

        random.shuffle(section1)
        random.shuffle(section2)
        random.shuffle(section3)
        test_cases.append(board_the_plane(section1+section2+section3))

    print('By seat: ', sum(test_cases)/len(test_cases))    
            
    



#random_boarding()
#section_boarding()
seat_boarding()