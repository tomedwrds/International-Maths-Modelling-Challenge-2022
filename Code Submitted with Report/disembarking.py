from audioop import reverse 

import graphlib 

from lib2to3.pgen2.token import NUMBER 

import random 

from string import ascii_letters 

import math 

 

#Comment out if not using 

import matplotlib.pyplot as plt 

import numpy 

import matplotlib.colors as colors 

import matplotlib as mpl 

from matplotlib.colors import Colormap, LinearSegmentedColormap, ListedColormap 

#Constants for refrences 

PRIORITY = 0 

INTERNAL_COCK = 1 

HAS_LUGGAGE = 2 

 

# all measured in standard units (m,s,m/s etc) 

AVERAGE_WALKING_SPEED = 0.8 

AVERAGE_SEAT_PITCH = 0.78 

TIME_TO_MOVE = AVERAGE_SEAT_PITCH / AVERAGE_WALKING_SPEED 

TIME_TO_MOVE_PAST_SEAT = 2 

 

#Priority system 

priority_weightings = [] 

highest_priority_assigned = 0 

#Things to change  

BAG_COEFFICIENT = (20,80,10) 

NAUGHTY_BOY_COEFFICIENT = 0.3 

THANOS_SNAP_COEFFICENT = 0.5 

# proportions of group sizes 

SINGLE_PRINGLE_COEFFICIENT = 70 

COUPLES_COEFFIENCT = 20 

THREESOME_COEFFICIENT = 10 

 

 

 

# General setup shotput all seats in 

NUM_ROWS = 33 

NUM_SEATS = 6 

AISLE_INDEX = 3 

#Wide body shot 

WIDE_WING_SEATS = 28 

WIDE_WING_ROWS = 15 

TWO_SEATS = 9 

TWO_ROWS = 42 

TWO_A_ROWS= 18 

TWO_B_ROWS = 21 

GAP_SIZE = 3 

 

 

 

 

#Normal render  

def intalize_render(): 

     

    global highest_priority_assigned 

    #Absolute mess of code 

    image = [] 

    for i in range(NUM_SEATS+1): 

        subimage = [] 

        for k in range(NUM_ROWS): 

            if k % 2 == 0: 

                subimage.append(0.5)  

            else: 

                subimage.append(1.5) 

             

        image.append(subimage) 

             

     

    fig,ax = plt.subplots(1,1) 

     

    cmap = mpl.cm.OrRd 

    norm = mpl.colors.Normalize(vmin=-1, vmax=highest_priority_assigned) 

     

     

     

    image = numpy.array(image) 

    im = ax.imshow(image, cmap=cmap, norm = norm) 

     

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

             

            visualizer[i].append(seats[PRIORITY]) 

             

     

                     

                     

    

    im.set_data(visualizer) 

    fig.canvas.draw_idle() 

    plt.pause(1)  

def intalize_render_two_thing(): 

     

    global highest_priority_assigned 

     

    #Absolute mess of code 

    image = [] 

    for i in range(TWO_SEATS): 

        subimage = [] 

        for k in range(TWO_ROWS): 

            if k % 2 == 0: 

                subimage.append(0.5)  

            else: 

                subimage.append(1.5) 

             

        image.append(subimage) 

         

     

    fig,ax = plt.subplots(1,1) 

     

    cmap = mpl.cm.OrRd 

    norm = mpl.colors.Normalize(vmin=-1, vmax=highest_priority_assigned) 

     

     

     

    image = numpy.array(image) 

    im = ax.imshow(image, cmap=cmap, norm = norm) 

     

    ax.set_yticks(numpy.arange(0.5, TWO_SEATS+0.5, 1).tolist(), minor=False) 

    ax.yaxis.grid(True, which='major') 

    ax.set_yticklabels(['Row A','Row B','Aisle','Row C','Row D','Row E','Aisle','Row F','Row G']) 

    ax.set_ylim(top=-0.5) 

    ax.set_title('Two Doors Two Aisles Disembarking Model') 

    ax.set_xticks(numpy.arange(0.5, TWO_ROWS+.5, 1).tolist(), minor=False) 

    ax.xaxis.grid(True, which='major') 

    xticklist = [] 

    #Create list of numbers between  

    for i in range(TWO_ROWS): 

        if ((i+1) % 5 == 0) and (i != 0): 

            xticklist.append(str(i+1)) 

        else: 

            xticklist.append('') 

         

    ax.set_xticklabels(xticklist) 

    ax.set_xlim(left=-0.5) 

     

    return im,fig 

def  intalize_render_widebody(): 

     

    global highest_priority_assigned 

     

    #Absolute mess of code 

    image = [] 

    for i in range(WIDE_WING_SEATS): 

        subimage = [] 

        for k in range(WIDE_WING_ROWS): 

            if k % 2 == 0: 

                subimage.append(0.5)  

            else: 

                subimage.append(1.5) 

             

        image.append(subimage) 

         

     

    fig,ax = plt.subplots(1,1) 

     

    cmap = mpl.cm.OrRd 

    norm = mpl.colors.Normalize(vmin=-1, vmax=highest_priority_assigned) 

     

     

     

    image = numpy.array(image) 

    im = ax.imshow(image, cmap=cmap, norm = norm) 

     

    ax.set_yticks(numpy.arange(0.5, WIDE_WING_SEATS+0.5, 1).tolist(), minor=False) 

    ax.yaxis.grid(True, which='major') 

    ax.set_yticklabels(['Row A','Row B','Row C','Aisle','Row D','Row E','Row F','Row G','Row H','Row I','Aisle','Row J','Row K','Row L','Row M','Row N','Row O','Aisle','Row P','Row Q','Row R','Row S','Row T','Row U','Aisle','Row V','Row W','Row X']) 

    ax.set_ylim(top=-0.5) 

    ax.set_title('Widebody Di sembarking Model') 

    ax.set_xticks(numpy.arange(0.5, WIDE_WING_ROWS+.5, 1).tolist(), minor=False) 

    ax.xaxis.grid(True, which='major') 

    xticklist = [] 

    #Create list of numbers between  

    for i in range(WIDE_WING_ROWS): 

        if ((i+1) % 5 == 0) and (i != 0): 

            xticklist.append(str(i+1)) 

        else: 

            xticklist.append('') 

         

    ax.set_xticklabels(xticklist) 

    ax.set_xlim(left=-0.5) 

     

    return im,fig 

    

#General shot to setup 

def generate_priorties(highest_priority_assigned): 

     

     

    weights = list(range(1, highest_priority_assigned+1)) 

     

    return(weights) 

def group_size(): 

    return random.choices([1,2,3], weights=(SINGLE_PRINGLE_COEFFICIENT,COUPLES_COEFFIENCT,THREESOME_COEFFICIENT), k=1)[0]     

def assign_luggage(): 

    return random.choices([0,1,2], weights=BAG_COEFFICIENT, k=1)[0] 

def bag_shit(): 

    global seating_plan 

    #Intalize bag amounts  

    lockers = [[0,0] for i in range(NUM_ROWS)] 

    for row in range(NUM_ROWS): 

        for seat in range(NUM_SEATS+1): 

         

            if seat < 3: 

                lockers[row][0] += seating_plan[seat][row][HAS_LUGGAGE] 

             

            elif seat > 3: 

                lockers[row][1] += seating_plan[seat][row][HAS_LUGGAGE] 

    return lockers 

#Widebody 

def bag_shit_wide(): 

    global seating_plan 

    #Intalize bag amounts  

     

    lockers = [[ [0,0] for _ in range(WIDE_WING_ROWS-1)] for _ in range(4)] 

     

     

    for row in range(1,WIDE_WING_ROWS): 

         

        for seat in range(1,WIDE_WING_SEATS): 

            sublocker = math.floor((seat)/7) 

            if seating_plan[seat][row][PRIORITY] != -1: 

                if seat % 7 < 3: 

                    lockers[sublocker][row-1][0] += seating_plan[seat][row][HAS_LUGGAGE] 

                 

                elif seat % 7 > 3: 

                    lockers[sublocker][row-1][1] += seating_plan[seat][row][HAS_LUGGAGE] 

                 

             

                 

                     

         

         

    return lockers 

#Modifitying shot 

def group_shit(): 

        for row in range(NUM_ROWS): 

            #Resets var  

            current_group_size = 0 

            current_group_priorty = [] 

            current_group_people_added = 0 

            for seat in range(NUM_SEATS+1): 

                #make sure we not in aisles 

                if seat != AISLE_INDEX: 

                    #If not currently generating create a new group 

                    if current_group_people_added == 0: 

                        current_group_size = current_group_people_added = group_size() 

                        if current_group_people_added == 1:  

                            current_group_people_added = 0  

                        else: 

                            current_group_priorty.append(seating_plan[seat][row][PRIORITY]) 

                            current_group_people_added -=1 

                         

                         

                    else: # Currently generating a group 

                        current_group_priorty.append(seating_plan[seat][row][PRIORITY]) 

                        current_group_people_added -=1 

                         

                        #If all people added to group 

                        if current_group_people_added == 0: 

                            #Loop back through people and send priority to average 

                             

                             

                            gone_through_aisles = 0 

                            for i in range(current_group_size): 

                                #Go back through and adjust priority 

                                 

                                #If gone through aisles add another  

                                if (seat - i) == AISLE_INDEX: 

                                    gone_through_aisles = 1 

                                     

                                seating_plan[seat-(i+gone_through_aisles)][row][PRIORITY] = round(sum(current_group_priorty) / len(current_group_priorty))        

def naughty_people(): 

            

        #Generate total amount of naughty boys 

        naughty_bois = math.ceil(NUM_ROWS*NUM_SEATS*NAUGHTY_BOY_COEFFICIENT) 

         

        for i in range(naughty_bois): 

            numbers = list(range(0, NUM_SEATS+1)) 

             

            numbers.remove(3) 

            

            seat = random.choice(numbers) 

            row = random.randrange(NUM_ROWS) 

             

            seating_plan[seat][row][PRIORITY] = random.randrange(1,highest_priority_assigned+1) 

def thanos_snap(): 

    for seat in range(NUM_SEATS+1): 

        for row in range(NUM_ROWS): 

            if THANOS_SNAP_COEFFICENT > random.random(): 

                seating_plan[seat][row] = [-1,0] 

#Narrow body boarding                      

def reverse_wilma(): 

    global seating_plan 

    global highest_priority_assigned 

      

    highest_priority_assigned = 3 

     

    seating_plan = [[ [3,0,assign_luggage()] for _ in range(NUM_ROWS)] for _ in range(NUM_SEATS + 1)] 

    seating_plan[0]= [[1,0,assign_luggage()]  for _ in range(NUM_ROWS)] 

    seating_plan[6]= [[1,0,assign_luggage()]  for _ in range(NUM_ROWS)] 

    seating_plan[1]= [[2,0,assign_luggage()]  for _ in range(NUM_ROWS)] 

    seating_plan[5]= [[2,0,assign_luggage()]  for _ in range(NUM_ROWS)] 

    seating_plan[AISLE_INDEX]= [[-1,0]  for _ in range(NUM_ROWS)] 

       

    naughty_people() 

    group_shit()            

def random_deboard(): 

    global seating_plan 

    global highest_priority_assigned 

      

    highest_priority_assigned = 10 

     

    seating_plan = [[ [random.randrange(1,10),0,assign_luggage()] for _ in range(NUM_ROWS)] for _ in range(NUM_SEATS + 1)] 

    seating_plan[AISLE_INDEX]= [[-1,0]  for _ in range(NUM_ROWS)] 

     

    group_shit() 

def sections(): 

     

    global seating_plan 

     

    global highest_priority_assigned 

      

    highest_priority_assigned = 3 

    fjuk = [] 

    for i in range(NUM_SEATS+1): 

        aisles = [] 

        for k in range(0,11): 

            aisles.append([3,0,assign_luggage()]) 

        for k in range(11,22): 

            aisles.append([2,0,assign_luggage()]) 

        for k in range(22,NUM_ROWS): 

            aisles.append([1,0,assign_luggage()]) 

        fjuk.append(aisles) 

    seating_plan = fjuk 

    seating_plan[AISLE_INDEX]= [[-1,0]  for _ in range(NUM_ROWS)] 

    naughty_people() 

    group_shit() 

def back_to_front(): 

    global seating_plan 

    global highest_priority_assigned 

      

      

    #Create empty seating plan 

    seating_plan = [[ [-1,0,assign_luggage()] for _ in range(NUM_ROWS)] for _ in range(NUM_SEATS + 1)] 

     

    highest_priority_assigned = 0 

     

    for row in range(NUM_ROWS): 

        for seat in range(NUM_SEATS+1): 

            #Increment priority 

             

             

            if seat == 0 or seat == 3: 

                highest_priority_assigned += 1 

            seating_plan[seat][row] = ([highest_priority_assigned,0,assign_luggage()]) 

             

    seating_plan[AISLE_INDEX]= [[-1,0]  for _ in range(NUM_ROWS)] 

    #naughty_people() 

    #group_shit()    

def generate_front_to_back(): 

    global seating_plan 

    global highest_priority_assigned 

      

      

    #Create empty seating plan 

    seating_plan = [[ [-1,0,assign_luggage()] for _ in range(NUM_ROWS)] for _ in range(NUM_SEATS + 1)] 

     

    highest_priority_assigned = 0 

     

    for row in reversed(range(NUM_ROWS)): 

        for seat in range(NUM_SEATS+1): 

            #Increment priority 

             

             

            if seat == 0 or seat == 3: 

                highest_priority_assigned += 1 

            seating_plan[seat][row] = ([highest_priority_assigned,0,assign_luggage()]) 

             

    seating_plan[AISLE_INDEX]= [[-1,0]  for _ in range(NUM_ROWS)] 

     

     

    naughty_people() 

    group_shit() 

     

def group_shit_two(): 

    for row in range(4,TWO_ROWS): 

        #Resets var  

        current_group_size = 0 

        current_group_priorty = [] 

        current_group_people_added = 0 

         

         

         

        for seat in range(0,9): 

             

            #make sure we not in aisles 

            if (seat != 2 or seat !=4) and seating_plan[seat][row][PRIORITY] != -1: 

                #If not currently generating create a new group 

                if current_group_people_added == 0: 

                    current_group_size = current_group_people_added = group_size() 

                    if current_group_people_added == 1:  

                        current_group_people_added = 0  

                    else: 

                        current_group_priorty.append(seating_plan[seat][row][PRIORITY]) 

                        current_group_people_added -=1 

                     

                     

                else: # Currently generating a group 

                    current_group_priorty.append(seating_plan[seat][row][PRIORITY]) 

                    current_group_people_added -=1 

                     

                    #If all people added to group 

                    if current_group_people_added == 0: 

                        #Loop back through people and send priority to average 

                         

                         

                        gone_through_aisles = 0 

                        for i in range(current_group_size): 

                            #Go back through and adjust priority 

                             

                            #If gone through aisles add another  

                            if (seat - i) == 2 or (seat - i) == 6: 

                                gone_through_aisles = 1 

                                 

                            seating_plan[(seat-(i+gone_through_aisles))][row][PRIORITY] = round(sum(current_group_priorty) / len(current_group_priorty))                                                

#Wide body boarding 

def clear_aisles_widebody(): 

    global seating_plan 

     

     

    #Clear aisles 

    for i in range(WIDE_WING_SEATS): 

        if i % 7 == 3 and i != WIDE_WING_SEATS: 

            seating_plan[i]= [[-1,0]  for _ in range(WIDE_WING_ROWS)] 

    #Clear front aisles 

    for k in range(WIDE_WING_SEATS): 

        seating_plan[k][0] = [-1,0]  

         

    #Clear extra 9 on both sides 

    for k in range(1, 4): 

        for j in range(0,3): 

           seating_plan[j][k] = [-1,0] 

            

    #Clear extra 9 on both sides 

    for k in range(1, 4): 

        for j in range(WIDE_WING_SEATS-3,WIDE_WING_SEATS): 

           seating_plan[j][k] = [-1,0] 

def naughty_people_wide(): 

            

        #Generate total amount of naughty boys 

        naughty_bois = math.ceil(((WIDE_WING_ROWS-1)*(WIDE_WING_SEATS-4)-18)*NAUGHTY_BOY_COEFFICIENT) 

         

        for i in range(naughty_bois): 

             

            while True: 

                seat = random.randrange(WIDE_WING_SEATS) 

                row = random.randrange(WIDE_WING_ROWS) 

                 

                if seating_plan[seat][row][PRIORITY] != -1: 

                    seating_plan[seat][row][PRIORITY] = random.randrange(1,highest_priority_assigned+1) 

                    break 

def group_shit_wide(): 

        for row in range(WIDE_WING_ROWS): 

            #Resets var  

            current_group_size = 0 

            current_group_priorty = [] 

            current_group_people_added = 0 

             

             

            for current_aisle in range(0, WIDE_WING_SEATS,7): 

                for seat in range(0,7): 

                     

                    #make sure we not in aisles 

                    if seat != 3 and seating_plan[current_aisle+seat][row][PRIORITY] != -1: 

                        #If not currently generating create a new group 

                        if current_group_people_added == 0: 

                            current_group_size = current_group_people_added = group_size() 

                            if current_group_people_added == 1:  

                                current_group_people_added = 0  

                            else: 

                                current_group_priorty.append(seating_plan[current_aisle+seat][row][PRIORITY]) 

                                current_group_people_added -=1 

                             

                             

                        else: # Currently generating a group 

                            current_group_priorty.append(seating_plan[current_aisle+seat][row][PRIORITY]) 

                            current_group_people_added -=1 

                             

                            #If all people added to group 

                            if current_group_people_added == 0: 

                                #Loop back through people and send priority to average 

                                 

                                 

                                gone_through_aisles = 0 

                                for i in range(current_group_size): 

                                    #Go back through and adjust priority 

                                     

                                    #If gone through aisles add another  

                                    if (seat - i) == 3: 

                                        gone_through_aisles = 1 

                                         

                                    seating_plan[(seat-(i+gone_through_aisles))+current_aisle][row][PRIORITY] = round(sum(current_group_priorty) / len(current_group_priorty))                                                

def reverse_wilma_widebody(): 

    global seating_plan 

    global highest_priority_assigned 

      

    highest_priority_assigned = 3 

     

    #Make an empty 

    seating_plan = [[ [-1,0,0] for _ in range(WIDE_WING_ROWS)] for _ in range(WIDE_WING_SEATS)] 

     

    for i in range(WIDE_WING_SEATS): 

        if i in [2,4,9,11,16,18,23,25]: 

            seating_plan[i]= [[3,0,assign_luggage()]  for _ in range(WIDE_WING_ROWS)] 

        elif i in [1,5,8,12,15,19,22,26]: 

            seating_plan[i]= [[2,0,assign_luggage()]  for _ in range(WIDE_WING_ROWS)] 

        elif i in [0,6,7,13,14,20,21,27]: 

            seating_plan[i]= [[1,0,assign_luggage()]  for _ in range(WIDE_WING_ROWS)] 

         

     

    clear_aisles_widebody() 

    naughty_people_wide() 

    group_shit_wide()                

def random_deboard_widebody(): 

    global seating_plan 

    global highest_priority_assigned 

      

    highest_priority_assigned = 10 

     

    seating_plan = [[ [ random.randrange(1,10),0,assign_luggage()] for _ in range(WIDE_WING_ROWS)] for _ in range(WIDE_WING_SEATS)] 

     

    clear_aisles_widebody() 

    group_shit_wide()    

def sections_widebody(): 

     

    global seating_plan 

     

    global highest_priority_assigned 

      

    highest_priority_assigned = 3 

    fjuk = [] 

    for i in range(WIDE_WING_SEATS): 

        aisles = [] 

        for k in range(1,8): 

            aisles.append([3,0,assign_luggage()]) 

        for k in range(8,12): 

            aisles.append([2,0,assign_luggage()]) 

        for k in range(12,WIDE_WING_ROWS+1): 

            aisles.append([1,0,assign_luggage()]) 

        fjuk.append(aisles) 

    seating_plan = fjuk 

     

     

     

    clear_aisles_widebody() 

     

    naughty_people_wide() 

    group_shit_wide()     

def back_to_front_widebody(): 

    global seating_plan 

    global highest_priority_assigned 

      

      

    #Create empty seating plan 

    seating_plan = [[ [k+j,0,assign_luggage()] for k in range(WIDE_WING_ROWS)] for j in range(WIDE_WING_SEATS)] 

     

    highest_priority_assigned = WIDE_WING_SEATS+WIDE_WING_ROWS 

     

    clear_aisles_widebody() 

     

    naughty_people_wide() 

    group_shit_wide() 

def across_widebody(): 

    global seating_plan 

    global highest_priority_assigned 

      

      

    #Create empty seating plan 

    seating_plan = [[ [k,0,assign_luggage()] for k in range(WIDE_WING_ROWS)] for j in range(WIDE_WING_SEATS)] 

     

    highest_priority_assigned = WIDE_WING_ROWS 

     

    clear_aisles_widebody() 

     

    naughty_people_wide() 

    group_shit_wide() 

def naughty_people_two (): 

         

        global seating_plan 

        global highest_priority_assigned 

     

        #Generate total amount of naughty boys 

        naughty_bois = math.ceil(((TWO_SEATS-2)*(TWO_A_ROWS+TWO_B_ROWS)+18)*NAUGHTY_BOY_COEFFICIENT) 

         

        for i in range(naughty_bois): 

             

            while True: 

                seat = random.randrange(TWO_SEATS) 

                row = random.randrange(TWO_ROWS) 

                 

                if seating_plan[seat][row][PRIORITY] != -1: 

                    seating_plan[seat][row][PRIORITY] = random.randrange(1,highest_priority_assigned) 

                    break 

def generate_front_to_back_widebody (): 

    global seating_plan 

    global highest_priority_assigned 

      

    highest_priority_assigned = WIDE_WING_SEATS+WIDE_WING_ROWS 

    #Create empty seating plan 

    seating_plan = [[ [highest_priority_assigned-(k+j),0,assign_luggage()] for k in range(WIDE_WING_ROWS)] for j in range(WIDE_WING_SEATS)] 

     

     

     

    clear_aisles_widebody() 

     

    naughty_people_wide() 

    group_shit_wide() 

  

  

def bag_shit_Two(): 

    global seating_plan 

    #Intalize bag amounts  

    lockers = [[[0,0] for _ in range(TWO_A_ROWS)],[[0,0] for _ in range(TWO_B_ROWS)]] 

     

    #A first 

    for row in range(TWO_A_ROWS): 

         

        for seat in range(TWO_SEATS): 

             

            if seating_plan[seat][row][PRIORITY] != -1: 

                if seat <=3: 

                    lockers[0][row][0] += seating_plan[seat][row][HAS_LUGGAGE] 

                 

                elif seat > 3: 

                    lockers[0][row][1] += seating_plan[seat][row][HAS_LUGGAGE] 

    #B second 

    for row in range(TWO_B_ROWS): 

         

        for seat in range(TWO_SEATS): 

             

            if seating_plan[seat][row+GAP_SIZE+TWO_A_ROWS][PRIORITY] != -1: 

                if seat <=3: 

                    lockers[1][row][0] += seating_plan[seat][row+GAP_SIZE+TWO_A_ROWS][HAS_LUGGAGE] 

                 

                elif seat > 3: 

                    lockers[1][row][1] += seating_plan[seat][row+GAP_SIZE+TWO_A_ROWS][HAS_LUGGAGE] 

                 

             

                 

                     

         

         

    return lockers 

def two_first_class(): 

    global seating_plan 

    global highest_priority_assigned 

     

    #Generate first class  

    seating_plan[0][0][0] = highest_priority_assigned 

    seating_plan[0][1][0] = highest_priority_assigned 

    seating_plan[0][2][0] = highest_priority_assigned 

    seating_plan[1][0][0] = highest_priority_assigned 

    seating_plan[1][1][0] = highest_priority_assigned 

    seating_plan[1][2][0] = highest_priority_assigned 

    seating_plan[3][0][0] = highest_priority_assigned 

    seating_plan[3][1][0] = highest_priority_assigned 

    seating_plan[3][2][0] = highest_priority_assigned 

    seating_plan[5][0][0] = highest_priority_assigned 

    seating_plan[5][1][0] = highest_priority_assigned 

    seating_plan[5][2][0] = highest_priority_assigned 

    seating_plan[7][0][0] = highest_priority_assigned 

    seating_plan[7][1][0] = highest_priority_assigned 

    seating_plan[7][2][0] = highest_priority_assigned 

    seating_plan[8][0][0] = highest_priority_assigned 

    seating_plan[8][1][0] = highest_priority_assigned 

    seating_plan[8][2][0] = highest_priority_assigned 

 #Two 

def two_cleanup(): 

    global seating_plan 

    global highest_priority_assigned 

     

     

     

    #Clear aisles 

    seating_plan[2]= [[-1,0]  for _ in range(TWO_ROWS)] 

    seating_plan[6]= [[-1,0]  for _ in range(TWO_ROWS)] 

    #Tidy up first class 

    seating_plan[4][0] = [-1,0] 

    seating_plan[4][1] = [-1,0] 

    seating_plan[4][2] = [-1,0] 

     

 

    #Clear queues out 

    for k in range(TWO_SEATS): 

        for j in range(TWO_ROWS): 

            if j in [3, 18,19,20,42]: 

                seating_plan[k][j] = [-1,0]  

                 

def two_random(): 

    global seating_plan 

    global highest_priority_assigned 

     

    seating_plan = [[ [random.randrange(1,10),0,assign_luggage()] for _ in range(TWO_ROWS)] for _ in range(TWO_SEATS)] 

     

    highest_priority_assigned = 10 

    two_first_class() 

    two_cleanup() 

    naughty_people_two() 

    group_shit_two() 

     

def two_back_to_front(): 

    global seating_plan 

    global highest_priority_assigned 

    highest_priority_assigned = 0 

    #Generate an empty plane 

    seating_plan = [[ [0,0,0] for _ in range(TWO_ROWS)] for _ in range(TWO_SEATS)] 

    for _ in range(TWO_SEATS): 

        for k in range(4,TWO_A_ROWS): 

             

            seating_plan[_][k] = [k,0,assign_luggage()] 

     

    for _ in range(TWO_SEATS): 

        for k in (range(TWO_B_ROWS)): 

             

            seating_plan[_][(TWO_B_ROWS-k)+(TWO_A_ROWS+GAP_SIZE-1)] = [k,0,assign_luggage()] 

     

    highest_priority_assigned = TWO_B_ROWS 

     

    two_first_class() 

    two_cleanup() 

    naughty_people_two() 

    group_shit_two() 

     

def two_front_to_back(): 

    global seating_plan 

    global highest_priority_assigned 

    highest_priority_assigned = 0 

    #Generate an empty plane 

    seating_plan = [[ [0,0,0] for _ in range(TWO_ROWS)] for _ in range(TWO_SEATS)] 

    for _ in range(TWO_SEATS): 

        for k in range(4,TWO_A_ROWS): 

             

            seating_plan[_][TWO_A_ROWS-k] = [k,0,assign_luggage()] 

     

    for _ in range(TWO_SEATS): 

        for k in (range(TWO_B_ROWS)): 

             

            seating_plan[_][(k)+(TWO_A_ROWS+GAP_SIZE)] = [k,0,assign_luggage()] 

     

    highest_priority_assigned = TWO_B_ROWS 

     

    two_first_class() 

    two_cleanup() 

    naughty_people_two() 

    group_shit_two() 

     

def two_reverse_wilma_widebody(): 

    global seating_plan 

    global highest_priority_assigned 

      

    highest_priority_assigned = 2 

     

    #Make an empty 

    seating_plan = [[ [-1,0,0] for _ in range(TWO_ROWS)] for _ in range(TWO_SEATS)] 

     

    for i in range(TWO_SEATS): 

        if i in [1,3,5,7]: 

            seating_plan[i]= [[2,0,assign_luggage()]  for _ in range(TWO_ROWS)] 

        elif i in [0,4,8]: 

            seating_plan[i]= [[1,0,assign_luggage()]  for _ in range(TWO_ROWS)] 

             

    two_first_class() 

    two_cleanup() 

    naughty_people_two() 

    group_shit_two() 

     

     

def two_reverse_sections_360(): 

    global seating_plan 

     

    global highest_priority_assigned 

      

    highest_priority_assigned = 3 

    fjuk = [] 

    for i in range(TWO_SEATS): 

        aisles = [] 

        for k in range(0,8): 

            aisles.append([3,0,assign_luggage()]) 

        for k in range(8,13): 

            aisles.append([2,0,assign_luggage()]) 

        for k in range(13,21): 

            aisles.append([1,0,assign_luggage()]) 

        for k in range(21,28): 

            aisles.append([1,0,assign_luggage()]) 

        for k in range(28,36): 

            aisles.append([2,0,assign_luggage()]) 

        for k in range(36,TWO_ROWS): 

            aisles.append([3,0,assign_luggage()]) 

        fjuk.append(aisles) 

    seating_plan = fjuk 

     

    two_first_class() 

    two_cleanup() 

    naughty_people_two() 

    group_shit_two() 

     

     

     

      

             

     

        

#Logic 

def check_locker_space_wide(luggage_number, current_row, seat, lockers): 

    # if passenger has no baggage 

    if luggage_number == 0: 

        return 0 

     

    sublocker = math.floor((seat)/7) 

    

    if seat % 7 < 3: 

        nbins = lockers[sublocker][current_row-1][0]  

        lockers[sublocker][current_row-1][0]  -= luggage_number 

     

    elif seat % 7 > 3: 

        nbins = lockers[sublocker][current_row-1][1]  

        lockers[sublocker][current_row-1][1]  -= luggage_number 

     

    # derivations in writeup 

    if luggage_number == 1: 

        t = (4)/(1-(0.8*((nbins-2)))/6)     

    if luggage_number == 2: 

        t = (4)/(1-(0.8*((nbins-2)))/6) + (2.25)/(1-((nbins-2))/6) 

     

    return t 

def check_locker_space(luggage_number, current_row, down, lockers): 

    # if passenger has no baggage 

    if luggage_number == 0: 

        return 0 

     

    # if on right side of aisle 

    if down==True: 

         

        nbins = lockers[NUM_ROWS-current_row-1][1] 

        lockers[NUM_ROWS-current_row-1][1] -= luggage_number 

    else: 

         

        nbins = lockers[NUM_ROWS-current_row-1][0] 

        lockers[NUM_ROWS-current_row-1][0] -= luggage_number 

    if luggage_number == 1: 

        t = (4)/(1-(0.8*((nbins-2)))/6)     

    if luggage_number == 2: 

        t = (4)/(1-(0.8*((nbins-2)))/6) + (2.25)/(1-((nbins-2))/6) 

     

    return t 

def check_locker_space_Two(luggage_number, current_row, seat, lockers,sectionA): 

     

    if sectionA: 

        thingy = 0 

    else:  

        thingy = 1 

     

    # if passenger has no baggage 

    if luggage_number == 0: 

        return 0 

     

    # if on right side of aisle 

    if seat > 3: 

         

        nbins = lockers[thingy][current_row][1] 

        lockers[thingy][current_row][1] -= luggage_number 

    else: 

         

        nbins = lockers[thingy][current_row][0] 

        lockers[thingy][current_row][0] -= luggage_number 

    if luggage_number == 1: 

        t = (4)/(1-(0.8*((nbins-2)))/6)     

    if luggage_number == 2: 

        t = (4)/(1-(0.8*((nbins-2)))/6) + (2.25)/(1-((nbins-2))/6) 

     

    return t 

def move_up(seat,row): 

            

    if seating_plan[seat-1][row][0] == -1: 

        seating_plan[seat-1][row] = seating_plan[seat][row] 

        seating_plan[seat-1][row][1] = 0 

        seating_plan[seat][row] = [-1,0]                 

def move_down(seat,row): 

     

     

    if seating_plan[seat+1][row][0] == -1: 

        seating_plan[seat+1][row] = seating_plan[seat][row] 

        seating_plan[seat+1][row][1] = 0 

        seating_plan[seat][row] = [-1,0]           

def aisle_take_above(row,hello,world): 

    #Move person from above into aisle 

    seating_plan[AISLE_INDEX][row] = seating_plan[AISLE_INDEX-1][row] 

    seating_plan[AISLE_INDEX-1][row] = [-1,0]   

     

    #Luggage 

    seating_plan[AISLE_INDEX][row][INTERNAL_COCK] = -locker_shit_type[boarding_type](seating_plan[AISLE_INDEX][row][HAS_LUGGAGE], row, True, lockers)     

def aisle_take_below(row,frick,me): 

    #Move person from below into aisle 

    seating_plan[AISLE_INDEX][row] = seating_plan[AISLE_INDEX+1][row] 

    seating_plan[AISLE_INDEX+1][row] = [-1,0] 

     

      

    seating_plan[AISLE_INDEX][row][INTERNAL_COCK] = -locker_shit_type[boarding_type](seating_plan[AISLE_INDEX][row][HAS_LUGGAGE], row, False, lockers)        

def aisle_take_above_wide(row,current_aisles,uguil): 

    #Move person from above into aisle 

    #Luggage 

    seating_plan[current_aisles-1][row][INTERNAL_COCK] = -locker_shit_type[boarding_type](seating_plan[current_aisles-1][row][HAS_LUGGAGE], row, current_aisles-1, lockers)     

     

    seating_plan[current_aisles][row] = seating_plan[current_aisles-1][row] 

    seating_plan[current_aisles-1][row] = [-1,0]   

def aisle_take_above_Two(row,current_aisles,SectionA): 

    #Move person from above into aisle 

    #Luggage 

    if row != 3: 

        seating_plan[current_aisles-1][row][INTERNAL_COCK] = -locker_shit_type[boarding_type](seating_plan[current_aisles-1][row][HAS_LUGGAGE], row-(GAP_SIZE+TWO_A_ROWS), current_aisles-1, lockers,SectionA)     

     

    seating_plan[current_aisles][row] = seating_plan[current_aisles-1][row] 

    seating_plan[current_aisles-1][row] = [-1,0] 

     

def aisle_take_below_Two(row,current_aisles,sectionA): 

    #Move person from below into aisle 

    if row != 3: 

        seating_plan[current_aisles+1][row][INTERNAL_COCK] = -locker_shit_type[boarding_type](seating_plan[current_aisles+1][row][HAS_LUGGAGE], row-(GAP_SIZE+TWO_A_ROWS), current_aisles+1, lockers,sectionA) 

     

    seating_plan[current_aisles][row] = seating_plan[current_aisles+1][row] 

    seating_plan[current_aisles+1][row] = [-1,0] 

     

def aisle_take_below_wide(row,current_aisles,aszgasdhasdh): 

    #Move person from below into aisle 

    if row != 0: 

        seating_plan[current_aisles+1][row][INTERNAL_COCK] = -locker_shit_type[boarding_type](seating_plan[current_aisles+1][row][HAS_LUGGAGE], row, current_aisles+1, lockers) 

     

    seating_plan[current_aisles][row] = seating_plan[current_aisles+1][row] 

    seating_plan[current_aisles+1][row] = [-1,0] 

     

      

       

 

 

def aisle_take_left(row,current_aisles,whythefucknot): 

     

    #Move person from right into aisle 

    seating_plan[current_aisles][row] = seating_plan[current_aisles][row-1] 

    seating_plan[current_aisles][row-1] = [-1,0] 

    seating_plan[current_aisles][row][INTERNAL_COCK] = 0 

def aisle_take_right(row, idonot, careanymore): 

     

    #Move person from right into aisle 

    seating_plan[AISLE_INDEX][row] = seating_plan[AISLE_INDEX][row+1] 

    seating_plan[AISLE_INDEX][row+1] = [-1,0] 

    seating_plan[AISLE_INDEX][row][INTERNAL_COCK] = 0 

                      

def aisle_take_right_wide(row,current_aisles,whythefucknot): 

     

    #Move person from right into aisle 

    seating_plan[current_aisles][row] = seating_plan[current_aisles][row+1] 

    seating_plan[current_aisles][row+1] = [-1,0] 

    seating_plan[current_aisles][row][INTERNAL_COCK] = 0 

                   

#While loop   

def off_the_plane(generation_method,text): 

    global im,fig 

    #isual shot 

     

    global seating_plan 

    global priority_weightings 

    global lockers 

    test_cases = [] 

     

     

     

     

    for i in range(N_TEST_CASES): 

        generation_method() 

        total_time=0 

        left_plane = 0 

        priority_weightings = generate_priorties(highest_priority_assigned) 

        lockers = bag_shit_type[boarding_type]() 

        if VISUALIZER: 

            im,fig = render_type[boarding_type]() 

         

        while True: 

            if boarding_type == TWO: 

                #Exit square 

                if seating_plan[2][41][PRIORITY] != -1 and seating_plan[2][41][INTERNAL_COCK] >= TIME_TO_MOVE: 

                    #Empty square 

                    seating_plan[2][41] = [-1,0] 

                    left_plane += 1 

                 

                if seating_plan[6][41][PRIORITY] != -1 and seating_plan[6][41][INTERNAL_COCK] >= TIME_TO_MOVE: 

                    #Empty square 

                    seating_plan[6][41] = [-1,0] 

                    left_plane += 1 

                if seating_plan[TWO_SEATS-1][3][PRIORITY] != -1 and seating_plan[TWO_SEATS-1][3][INTERNAL_COCK] >= TIME_TO_MOVE: 

                    #Empty square 

                    seating_plan[TWO_SEATS-1][3] = [-1,0] 

                    left_plane += 1 

                

                 

                #End code shot 

                if left_plane == 249: 

                    test_cases.append(total_time)  

                    break 

                 

                for current_aisle in (range(TWO_SEATS)): 

                    if seating_plan[current_aisle][3][PRIORITY] == -1: 

                             

                            priorities = [0,0,0,0] 

                            possible_moves = [aisle_take_above_Two, aisle_take_below_Two, aisle_take_right_wide,aisle_take_left ] 

                            total_move_possibilites = 0 

                             

                            #Get things to check 

                            is_person_above_moving = seating_plan[current_aisle-1][3][PRIORITY] != -1 and seating_plan[current_aisle-1][3][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT 

                         

                            if is_person_above_moving: 

                                priorities[0] = priority_weightings[seating_plan[current_aisle-1][3][PRIORITY]-1] 

                                total_move_possibilites +=1 

                            if current_aisle != 8: 

                                is_person_below_moving = False #seating_plan[current_aisle+1][3][PRIORITY] != -1 and seating_plan[current_aisle+1][3][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT 

                            else: is_person_below_moving = 0 

                            if is_person_below_moving:  

                                 

                                priorities[1] = 0 #priority_weightings[seating_plan[current_aisle+1][3][PRIORITY]-1] 

                                total_move_possibilites +=1 

                            #Prevent indexing error  

                            if True: #row+1+ec != TWO_ROWS: 

                                is_person_right_moving = seating_plan[current_aisle][3+1][PRIORITY] != -1 and seating_plan[current_aisle][3+1][INTERNAL_COCK] >= TIME_TO_MOVE 

                            else: 

                                is_person_right_moving = 0 

                             

                            if is_person_right_moving and (current_aisle == 2 or current_aisle == 6):  

                                 

                                priorities[2] = priority_weightings[seating_plan[current_aisle][3+1][PRIORITY]-1]  

                                total_move_possibilites +=1 

                        #ewginsdaogvnadsklbvasj nwklsfnwdsf 

                            if True: #row+1+ec != TWO_ROWS: 

                                is_person_left_moving = seating_plan[current_aisle][3-1][PRIORITY] != -1 and seating_plan[current_aisle][3-1][INTERNAL_COCK] >= TIME_TO_MOVE 

                            else: 

                                is_person_right_moving = 0 

                             

                            if is_person_left_moving and (current_aisle == 2 or current_aisle == 6) :  

                                priorities[3] = priority_weightings[seating_plan[current_aisle][3-1][PRIORITY]-1]  

                                total_move_possibilites +=1 

                         

                            #Decide who moves above and below 

                            if total_move_possibilites > 0: 

                                #Reset time 

                                seating_plan[current_aisle][3][INTERNAL_COCK] = 0 

                                 

                                #frick knows what is happening here but it works so it stays 

                                move = numpy.argwhere(priorities == numpy.amax(priorities)) 

                                possible_moves[(random.choice(move))[0]](3,current_aisle,False) 

                                 

                for current_aisle in range(2,TWO_SEATS,4): 

                     

                    for row in reversed(range(0,TWO_B_ROWS)): 

                         

                        #extra constant 

                        ec = GAP_SIZE+TWO_A_ROWS 

                        #Check if aisles place is empty 

                        if seating_plan[current_aisle][row+ec][PRIORITY] == -1: 

                             

                            priorities = [0,0,0] 

                            possible_moves = [aisle_take_above_Two, aisle_take_below_Two, aisle_take_left ] 

                            total_move_possibilites = 0 

                             

                            #Get things to check 

                            is_person_above_moving = seating_plan[current_aisle-1][row+ec][PRIORITY] != -1 and seating_plan[current_aisle-1][row+ec][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT 

                         

                            if is_person_above_moving: 

                                priorities[0] = priority_weightings[seating_plan[current_aisle-1][row+ec][PRIORITY]-1] 

                                total_move_possibilites +=1 

                             

                            is_person_below_moving = seating_plan[current_aisle+1][row+ec][PRIORITY] != -1 and seating_plan[current_aisle+1][row+ec][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT 

                            if is_person_below_moving:  

                                 

                                priorities[1] = priority_weightings[seating_plan[current_aisle+1][row+ec][PRIORITY]-1] 

                                total_move_possibilites +=1 

                            #Prevent indexing error  

                            if True: #row+1+ec != TWO_ROWS: 

                                is_person_right_moving = seating_plan[current_aisle][row-1+ec][PRIORITY] != -1 and seating_plan[current_aisle][row-1+ec][INTERNAL_COCK] >= TIME_TO_MOVE 

                            else: 

                                is_person_right_moving = 0 

                             

                            if is_person_right_moving:  

                                 

                                priorities[2] = priority_weightings[seating_plan[current_aisle][row+ec-1][PRIORITY]-1]  

                                total_move_possibilites +=1 

                         

                            #Decide who moves above and below 

                            if total_move_possibilites > 0: 

                                #Reset time 

                                seating_plan[current_aisle][row+ec][INTERNAL_COCK] = 0 

                                 

                                #frick knows what is happening here but it works so it stays 

                                move = numpy.argwhere(priorities == numpy.amax(priorities)) 

                                possible_moves[(random.choice(move))[0]](row+ec,current_aisle,False) 

                     

                     

                    for row in (range(0,TWO_A_ROWS)): 

                        if row != 3: 

                            #extra constant 

                             

                            #Check if aisles place is empty 

                            if seating_plan[current_aisle][row][PRIORITY] == -1: 

                                 

                                priorities = [0,0,0,0] 

                                possible_moves = [aisle_take_above_Two, aisle_take_below_Two, aisle_take_right_wide,aisle_take_left ] 

                                total_move_possibilites = 0 

                                 

                                #Get things to check 

                                is_person_above_moving = seating_plan[current_aisle-1][row][PRIORITY] != -1 and seating_plan[current_aisle-1][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT 

                             

                                if is_person_above_moving: 

                                    priorities[0] = priority_weightings[seating_plan[current_aisle-1][row][PRIORITY]-1] 

                                    total_move_possibilites +=1 

                                 

                                is_person_below_moving = seating_plan[current_aisle+1][row][PRIORITY] != -1 and seating_plan[current_aisle+1][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT 

                                if is_person_below_moving:  

                                     

                                    priorities[1] = priority_weightings[seating_plan[current_aisle+1][row][PRIORITY]-1] 

                                    total_move_possibilites +=1 

                                #Prevent indexing error  

                                if True: #row+1+ec != TWO_ROWS: 

                                    is_person_right_moving = seating_plan[current_aisle][row+1][PRIORITY] != -1 and seating_plan[current_aisle][row+1][INTERNAL_COCK] >= TIME_TO_MOVE 

                                else: 

                                    is_person_right_moving = 0 

                                 

                                if is_person_right_moving:  

                                     

                                    priorities[2] = priority_weightings[seating_plan[current_aisle][row+1][PRIORITY]-1]  

                                    total_move_possibilites +=1 

                            #ewginsdaogvnadsklbvasj nwklsfnwdsf 

                                if True: #row+1+ec != TWO_ROWS: 

                                    is_person_left_moving = seating_plan[current_aisle][row-1][PRIORITY] != -1 and seating_plan[current_aisle][row-1][INTERNAL_COCK] >= TIME_TO_MOVE 

                                else: 

                                    is_person_right_moving = 0 

                                 

                                if is_person_left_moving and row == 3:  

                                    priorities[3] = priority_weightings[seating_plan[current_aisle][row-1][PRIORITY]-1]  

                                    total_move_possibilites +=1 

                             

                                #Decide who moves above and below 

                                if total_move_possibilites > 0: 

                                    #Reset time 

                                    seating_plan[current_aisle][row][INTERNAL_COCK] = 0 

                                     

                                    #frick knows what is happening here but it works so it stays 

                                    move = numpy.argwhere(priorities == numpy.amax(priorities)) 

                                    possible_moves[(random.choice(move))[0]](row,current_aisle,False) 

 

                    #Move towards aisle  

                    for row in range(TWO_ROWS): 

                        if row!= 3: 

                            if seating_plan[0][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT: 

                                move_down(0,row) 

                            if seating_plan[TWO_SEATS-1][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT and seating_plan[TWO_SEATS-1][row][PRIORITY] != -1: 

                                move_up(TWO_SEATS-1,row) 

                            if seating_plan[4][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT: 

                                if random.randint(0,1) and seating_plan[3][row][PRIORITY] == -1: 

                                    move_up(4,row) 

                                elif seating_plan[5][row][PRIORITY] == -1: 

                                    move_down(4,row) 

                             

                 

                        

                                 

                             

                for i in range(TWO_SEATS): 

                    for k in range(TWO_ROWS): 

                        seating_plan[i][k][INTERNAL_COCK] += TIME_STEP  

                     

                     

                 

                 

                 

                 

                 

                 

            elif boarding_type == WIDEBODY: 

                #Exit square 

                if seating_plan[0][0][PRIORITY] != -1 and seating_plan[0][0][INTERNAL_COCK] >= TIME_TO_MOVE: 

                    #Empty square 

                    seating_plan[0][0] = [-1,0] 

                     

                    #End code shot 

                    left_plane += 1 

                    if left_plane == (WIDE_WING_ROWS-1)*(WIDE_WING_SEATS-4)-18: 

                        test_cases.append(total_time)  

                         

                        break 

                 

                #Down queue do not touch 2am code 

                for seat in range(WIDE_WING_SEATS): 

                     

                    #if can move something in 

                    if seating_plan[seat][0][PRIORITY] == -1: 

                             

                        priorities = [0,0] 

                        possible_moves = [ aisle_take_below_wide, aisle_take_right_wide ] 

                        total_move_possibilites = 0  

                         

                        #Check shot 

                        is_person_below_moving = seating_plan[seat][1][PRIORITY] != -1 and seating_plan[seat][1][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT and seat in [3,10,17,24] 

                        if is_person_below_moving:  

                             

                            priorities[1] = priority_weightings[seating_plan[seat][1][PRIORITY]-1] 

                            total_move_possibilites +=1 

                        #Prevent indexing error  

                        if seat != WIDE_WING_SEATS-1: 

                            is_person_right_moving = seating_plan[seat+1][0][PRIORITY] != -1 and seating_plan[seat+1][0][INTERNAL_COCK] >= TIME_TO_MOVE 

                        else: 

                            is_person_right_moving = 0 

                         

                        if is_person_right_moving:  

                             

                            priorities[0] = priority_weightings[seating_plan[seat+1][0][PRIORITY]-1]  

                            total_move_possibilites +=1 

                     

                        #Decide who moves above and below 

                        if total_move_possibilites > 0: 

                            #Reset time 

                            seating_plan[seat][0][INTERNAL_COCK] = 0  

                             

                            #frick knows what is happening here but it works so it stays 

                            move = numpy.argwhere(priorities == numpy.amax(priorities)) 

                            possible_moves[(random.choice(move))[0]](0,seat,False) 

                             

                             

                 

                for current_aisle in range(3, WIDE_WING_SEATS,7): 

                     

                     

                     

                    for row in range(1,WIDE_WING_ROWS): 

                         

                         

                             

                        #Check if aisles place is empty 

                        if seating_plan[current_aisle][row][PRIORITY] == -1: 

                             

                            priorities = [0,0,0] 

                            possible_moves = [aisle_take_above_wide, aisle_take_below_wide, aisle_take_right_wide ] 

                            total_move_possibilites = 0 

                             

                            #Get things to check 

                            is_person_above_moving = seating_plan[current_aisle-1][row][PRIORITY] != -1 and seating_plan[current_aisle-1][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT 

                         

                            if is_person_above_moving: 

                                priorities[0] = priority_weightings[seating_plan[current_aisle-1][row][PRIORITY]-1] 

                                total_move_possibilites +=1 

                             

                            is_person_below_moving = seating_plan[current_aisle+1][row][PRIORITY] != -1 and seating_plan[current_aisle+1][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT 

                            if is_person_below_moving:  

                                 

                                priorities[1] = priority_weightings[seating_plan[current_aisle+1][row][PRIORITY]-1] 

                                total_move_possibilites +=1 

                            #Prevent indexing error  

                            if row != WIDE_WING_ROWS-1: 

                                is_person_right_moving = seating_plan[current_aisle][row+1][PRIORITY] != -1 and seating_plan[current_aisle][row+1][INTERNAL_COCK] >= TIME_TO_MOVE 

                            else: 

                                is_person_right_moving = 0 

                             

                            if is_person_right_moving:  

                                 

                                priorities[2] = priority_weightings[seating_plan[current_aisle][row+1][PRIORITY]-1]  

                                total_move_possibilites +=1 

                         

                            #Decide who moves above and below 

                            if total_move_possibilites > 0: 

                                #Reset time 

                                seating_plan[current_aisle][row][INTERNAL_COCK] = 0 

                                 

                                #frick knows what is happening here but it works so it stays 

                                move = numpy.argwhere(priorities == numpy.amax(priorities)) 

                                possible_moves[(random.choice(move))[0]](row,current_aisle,False) 

                                 

                                 

                    # I fricking HATE INDENDATION 

                     

                     

                    #Get total amount of move posibilites      

                    #total_move_possibilites = is_person_above_moving  + is_person_below_moving + is_person_right_moving 

                     

                         

                for current_aisle in range(0, WIDE_WING_SEATS,7): 

                 

                 

                    # Move down  

                    for seat in reversed(range(0,2)): 

                        # Loops through all 37 rows 

                         

                        #Move towards aisle  

                        for row in range(0,WIDE_WING_ROWS): 

                            if seating_plan[seat+current_aisle][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT: 

                                move_down(seat+current_aisle,row) 

                                 

                                #Incrasese internal clock 

                             

                             

                    # Move up  

                    for seat in range(5,7): 

                        # Loops through all 37 rows 

                         

                        #Move towards aisle  

                        for row in range(0,WIDE_WING_ROWS): 

                            if seating_plan[seat+current_aisle][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT: 

                                move_up(seat+current_aisle,row) 

                        #Incrasese internal clock 

                for i in range(WIDE_WING_SEATS): 

                    for k in range(WIDE_WING_ROWS): 

                        seating_plan[i][k][INTERNAL_COCK] += TIME_STEP  

             

             

            elif boarding_type == NORMAL: 

                            

                #Exit square 

                if seating_plan[AISLE_INDEX][0][PRIORITY] != -1 and seating_plan[3][0][INTERNAL_COCK] >= TIME_TO_MOVE: 

                    #Empty square 

                    seating_plan[AISLE_INDEX][0] = [-1,0] 

                     

                    #End code shot 

                    left_plane += 1 

                    if left_plane == NUM_ROWS*NUM_SEATS: 

                        test_cases.append(total_time)  

                         

                        break 

                         

                 

                 

                #Aisle handling code 

                for row in range(0,NUM_ROWS): 

                    #Check if aisles place is empty 

                    if seating_plan[AISLE_INDEX][row][PRIORITY] == -1: 

                         

                         

                        priorities = [0,0,0] 

                        possible_moves = [aisle_take_above, aisle_take_below, aisle_take_right ] 

                        total_move_possibilites = 0 

                         

                        #Get things to check 

                        is_person_above_moving = seating_plan[AISLE_INDEX-1][row][PRIORITY] != -1 and seating_plan[AISLE_INDEX-1][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT 

                     

                        if is_person_above_moving: 

                            priorities[0] = priority_weightings[seating_plan[AISLE_INDEX-1][row][PRIORITY]-1] 

                            total_move_possibilites +=1 

                         

                        is_person_below_moving = seating_plan[AISLE_INDEX+1][row][PRIORITY] != -1 and seating_plan[AISLE_INDEX+1][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT 

                        if is_person_below_moving:  

                             

                            priorities[1] = priority_weightings[seating_plan[AISLE_INDEX+1][row][PRIORITY]-1] 

                            total_move_possibilites +=1 

                         

                        #Prevent indexing error  

                        if row != NUM_ROWS-1: 

                            is_person_right_moving = seating_plan[AISLE_INDEX][row+1][PRIORITY] != -1 and seating_plan[AISLE_INDEX][row+1][INTERNAL_COCK] >= TIME_TO_MOVE 

                        else: 

                            is_person_right_moving = 0 

                         

                        if is_person_right_moving:  

                             

                            priorities[2] = priority_weightings[seating_plan[AISLE_INDEX][row+1][PRIORITY]-1]  

                            total_move_possibilites +=1 

                         

                         

                        #Get total amount of move posibilites      

                        #total_move_possibilites = is_person_above_moving  + is_person_below_moving + is_person_right_moving 

                         

                        #Decide who moves above and below 

                        if total_move_possibilites > 0: 

                            #Reset time 

                            seating_plan[AISLE_INDEX][row][INTERNAL_COCK] = 0 

                 

                            #frick            knows what is happening here but it works so it stays 

                            move = numpy.argwhere(priorities == numpy.amax(priorities)) 

                            possible_moves[(random.choice(move))[0]](row,False,False) 

                             

                         

                             

                # Move down  

                for seat in reversed(range(0,2)): 

                    # Loops through all 37 rows 

                     

                    #Move towards aisle  

                    for row in range(0,NUM_ROWS): 

                        if seating_plan[seat][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT: 

                            move_down(seat,row) 

                            #Incrasese internal clock 

                         

                         

                # Move up  

                for seat in range(5,7): 

                    # Loops through all 37 rows 

                     

                    #Move towards aisle  

                    for row in range(0,NUM_ROWS): 

                        if seating_plan[seat][row][INTERNAL_COCK] >= TIME_TO_MOVE_PAST_SEAT: 

                            move_up(seat,row) 

                            #Incrasese internal clock 

                             

                for i in range(NUM_SEATS+1): 

                    for k in range(NUM_ROWS): 

                        seating_plan[i][k][INTERNAL_COCK] += TIME_STEP  

                         

                                 

               

                      

             

            total_time += TIME_STEP 

             

            #Update render comment out if not using 

            if VISUALIZER: update_render(seating_plan) 

    print(text + str(sum(test_cases)/len(test_cases))) 

    rows.append(test_cases) 

    return test_cases 

#Types  

render_type = [intalize_render,intalize_render_widebody,intalize_render_two_thing] 

bag_shit_type = [bag_shit, bag_shit_wide,bag_shit_Two] 

locker_shit_type = [check_locker_space,check_locker_space_wide,check_locker_space_Two]  

#What thing to do  

NORMAL = 0 

WIDEBODY = 1 

TWO = 2 

#Test stuff 

N_TEST_CASES = 50 

VISUALIZER = True 

TIME_STEP = 0 

boarding_type = TWO 

#Data csv 

import csv 

fields = [] 

rows = [] 

index = [] 

#Add the indexing 

for i in range(N_TEST_CASES): 

    index.append(i) 

     

rows.append(index) 

#Vroom     

seating_plan = [] 

 

''' 

#Flat body 

off_the_plane(random_deboard, 'Random: ') 

off_the_plane(sections, 'Sections: ') 

off_the_plane(reverse_wilma, 'Reverse Wilma: ') 

off_the_plane(generate_front_to_back, 'Front to back Row: ') 

off_the_plane(back_to_front, 'Back to Front Row: ')  

# field names add whatever field names that you are creating data for  

fields = ['Index','Random Group Adjusted', 'Front to back - sections', 'Reverse Wilma', 'Front to Back Row', 'Back to Front Row']  

file_name = 'narrow.csv' 

 

 

#Wide body 

off_the_plane(random_deboard_widebody, 'Random: ') 

off_the_plane(sections_widebody, 'Sections: ') 

off_the_plane(reverse_wilma_widebody, 'Reverse Wilma: ') 

off_the_plane(generate_front_to_back_widebody, 'Front seat to back seat: ') 

off_the_plane(back_to_front_widebody, 'Back seat to Front seat: ')  

off_the_plane(across_widebody, 'Across: ')  

# field names add whatever field names that you are creating data for  

fields = ['Index','Random Group Adjusted', 'Front to back - sections', 'Reverse Wilma', 'Front to Back Row', 'Back to Front Row', 'Across']  

file_name='widebody.csv' 

''' 

# field names add whatever field names that you are creating data for  

fields = ['Index','Back to front', 'Sections', 'Random', 'Reverse Wilma', 'Front to back']  

off_the_plane(two_reverse_sections_360, 'back to front') 

#off_the_plane(two_reverse_sections_360, 'Sections') 

# 

#off_the_plane(two_front_to_back, 'front to back') 

#off_the_plane(two_reverse_wilma_widebody, 'reverse wilma') 

#off_the_plane(two_random, 'random') 

file_name='twoaisles.csv' 

 

''' 

nbsensitivity = [] 

     

for i in range(0,41): 

    NAUGHTY_BOY_COEFFICIENT = (i*2.5)/100 

     

    # put method wanted in here 

    nbsensitivity.append(off_the_plane(back_to_front, 'back to front: ')) 

     

    print('for test with NB coefficient {}'.format((i*2.5)/100)) 

''' 

''' 

#Makes the shotinto colums honestly magic 

rows = zip(*rows) 

#Create the rows 

with open(file_name, 'w', newline='') as f: 

       

    # using csv.writer method from CSV package 

    write = csv.writer(f) 

       

    write.writerow(fields) 

     

    write.writerows(rows) 

 

 

''' 