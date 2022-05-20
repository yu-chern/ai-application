import numpy as np
from field_var import *

def range_check(chessboard_array,coordinates_range):
    if len(coordinates_range)==0:
        return False# no need to check, so it is not danger
    no_pawn_block = True
    for i,j in coordinates_range:
        if chessboard_array[i][j]=='Q':
            if no_pawn_block:
                return True
            else:
                return False
        elif chessboard_array[i][j]=='P':
            no_pawn_block = False
        elif chessboard_array[i][j]==0:
            continue
        elif chessboard_array[i][j]=='D':
            continue
        else:
            raise ValueError("chessboard_array[field[0]][field[1]] is wrong")
    return False

def check_danger(chessboard_array,field):
    """
    Input:
        chessboard_array:array
        field:pair = (x,y), the position on chessboard_array under check
    Return:
        True: if chessboard_array[x,y] is danger
        False: if chessboard_array[x,y] is free space
    """
    chessboard_size = len(chessboard_array)
    #1.check row
    ## check above[x-1,x-2,...,1,0]
    above = [(i,field[1]) for i in range(field[0]-1,-1,-1)]
    if range_check(chessboard_array,above):
        return True
    else:## check below[x+1,...,N]
        below = [(i,field[1]) for i in range(field[0]+1,chessboard_size,1)]
        if range_check(chessboard_array,below):
            return True
        #else: row is not in danger

    #2.check column
    ##check left[y-1,y-2,...,1,0]
    left = [(field[0],j) for j in range(field[1]-1,-1,-1)]
    if range_check(chessboard_array,left):
        return True
    else:##check right[y+1,y+2,...,N]
        right = [(field[0],j) for j in range(field[1]+1,chessboard_size,1)]
        if range_check(chessboard_array,right):
            return True
        #else: column is not in danger

    #3.check diagonal
    ## check diag_above[(x-1,y-1),(x-2,y-2),...]
    diag_above = [(i,j) for i,j in zip(range(field[0]-1,-1,-1),range(field[1]-1,-1,-1))]
    if range_check(chessboard_array,diag_above):
        return True
    else:## check diag_below[(x+1,y+1),(x+2,y+2),...]
        diag_below = [(i,j) for i,j in zip(range(field[0]+1,chessboard_size,1),range(field[1]+1,chessboard_size,1))]
        if range_check(chessboard_array,diag_below):
            return True
        #else: diagnoal is not in danger
    
    #4.check subdiagonal
    ## check subdiag_above[(x+1,y-1),(x+2,y-2),...]
    subdiag_above = [(i,j) for i,j in zip(range(field[0]+1,chessboard_size,1),range(field[1]-1,-1,-1))]
    if range_check(chessboard_array,subdiag_above):
        return True
    else:## check subdiag_below[(x-1,y+1),(x-2,y+2),...]
        subdiag_below = [(i,j) for i,j in zip(range(field[0]-1,-1,-1),range(field[1]+1,chessboard_size,1))]
        if range_check(chessboard_array,subdiag_below):
            return True
        #else: subdiagnoal is not in danger

    #row, col diag and subdiag are neither in danger
    return False    

def generate_knowledge(chessboard_array):
    """
    Initialize the knowledge base, by adding statements describing
    the initial state of the chessboard, as well as the rules concerning the
    danger fields.
    
    You can use the functions Queen(x,y), Pawn(x,y), and Danger(x,y) to
    produce the statements Qxy, Pxy, and Dxy, if x and y are integers.
    
    Input: np.ndarray 2-D array, where each field
            contains either 'Q', 'P', 'D' or '0'
            
    Output: A list kb of logical sentences that will be added to
             the knowledge base
    """
    
    chessboard_size = len(chessboard_array)
    kb = []
    
    all_fields = [(x,y) for x in range(chessboard_size) for y in range(chessboard_size)]
    
    
    for field in all_fields:
        #print(chessboard_array[field[0]][field[1]])
        if chessboard_array[field[0]][field[1]]=='Q':
            kb.append(Queen(field[0],field[1]))
        elif chessboard_array[field[0]][field[1]]=='P':
            kb.append(Pawn(field[0],field[1]))
        elif chessboard_array[field[0]][field[1]]=='D':
            kb.append(Danger(field[0],field[1]))
        elif chessboard_array[field[0]][field[1]]==0:
            #continue
            ###########################################
            # TODO:
            infer_sentence = inference(chessboard_array,field)
            if infer_sentence:
                kb.append(infer_sentence)
            ###########################################
            
        else:
            raise ValueError("chessboard_array[x,y] is wrong")
    return kb

def subsentence(chessboard_array,field,direction):
    """
    Generate a subsentence that only concerns the coordinates for chessboard_array[field[0]][field[1]]
    Input:
        direction: Int: 0:left, 1:right, 2:up, 3:down, 
                        4:upper_left, 5:lower_right, 6:lower_left, 7:upper_right
    Return:
        sentence: string; for example: sentence = 'row_left_danger(i,j)'
    """
    chessboard_size = len(chessboard_array)
    
    sentence = ''
    if direction == 0:#left
        x_left = [x for x in range(field[0]-1,-1,-1)]
        if len(x_left)==0:
            return ''
        for coord in x_left:
            for idx,x in enumerate(range(coord,field[0],+1)):#Cp,Cp+1,...,field[0]-1
                if idx==0:
                    sentence += Queen(x,field[1])
                else:
                    #s_part = '&(~'+Pawn(x,field[1])+')'
                    s_part = '&((~'+Pawn(x,field[1])+')|('+Danger(x,field[1])+'))'
                    sentence += s_part
            sentence += '|'
                
    elif direction == 1:#right
        x_right = [x for x in range(field[0]+1,chessboard_size,1)]
        if len(x_right)==0:
            return ''
        for coord in x_right:
            for idx,x in enumerate(range(coord,field[0],-1)):
                if idx==0:
                    sentence += Queen(x,field[1])
                else:
                    #s_part = '&(~'+Pawn(x,field[1])+')'
                    s_part = '&((~'+Pawn(x,field[1])+')|('+Danger(x,field[1])+'))'
                    sentence += s_part
            sentence += '|'
    
    elif direction == 2:#up
        y_upper = [y for y in range(field[1]-1,-1,-1)]
        if len(y_upper)==0:
            return ''
        for coord in y_upper:
            for idx,y in enumerate(range(coord,field[1],+1)):
                if idx==0:
                    sentence += Queen(field[0],y)
                else:
                    #s_part = '&(~'+Pawn(field[0],y)+')'
                    s_part = '&((~'+Pawn(field[0],y)+')|('+Danger(field[0],y)+'))'
                    sentence += s_part
            sentence += '|'

    elif direction == 3:#low
        y_lower = [y for y in range(field[1]+1,chessboard_size,+1)]
        if len(y_lower)==0:
            return ''
        for coord in y_lower:
            for idx,y in enumerate(range(coord,field[1],-1)):
                if idx==0:
                    sentence += Queen(field[0],y)
                else:
                    #s_part = '&(~'+Pawn(field[0],y)+')'
                    s_part = '&((~'+Pawn(field[0],y)+')|('+Danger(field[0],y)+'))'
                    sentence += s_part
            sentence += '|'
    
    elif direction == 4:#upper_left
        upper_left = [(x,y) for x,y in zip(range(field[0]-1,-1,-1),range(field[1]-1,-1,-1))]
        if len(upper_left)==0:
            return ''
        for coord in upper_left:
            for idx,xy in enumerate(  zip( range(coord[0],field[0],+1),range(coord[1],field[1],+1) ) ):
                if idx==0:
                    sentence += Queen(xy[0],xy[1])
                else:
                    #s_part = '&(~'+Pawn(xy[0],xy[1])+')'
                    s_part = '&((~'+Pawn(xy[0],xy[1])+')|('+Danger(xy[0],xy[1])+'))'
                    sentence += s_part
            sentence += '|'
    
    elif direction == 5:#lower_right
        lower_right = [(x,y) for x,y in zip(range(field[0]+1,chessboard_size,1),range(field[1]+1,chessboard_size,1))]
        if len(lower_right)==0:
            return ''
        for coord in lower_right:
            for idx,xy in enumerate(  zip( range(coord[0],field[0],-1),range(coord[1],field[1],-1) ) ):
                if idx==0:
                    sentence += Queen(xy[0],xy[1])
                else:
                    #s_part = '&(~'+Pawn(xy[0],xy[1])+')'
                    s_part = '&((~'+Pawn(xy[0],xy[1])+')|('+Danger(xy[0],xy[1])+'))'
                    sentence += s_part
            sentence += '|'

    elif direction == 6:#lower_left
        lower_left = [(x,y) for x,y in zip(range(field[0]-1,-1,-1),range(field[1]+1,chessboard_size,1))]
        if len(lower_left)==0:
            return ''
        for coord in lower_left:
            for idx,xy in enumerate(  zip( range(coord[0],field[0],1),range(coord[1],field[1],-1) ) ):
                if idx==0:
                    sentence += Queen(xy[0],xy[1])
                else:
                    #s_part = '&(~'+Pawn(xy[0],xy[1])+')'
                    s_part = '&((~'+Pawn(xy[0],xy[1])+')|('+Danger(xy[0],xy[1])+'))'
                    sentence += s_part
            sentence += '|'

    elif direction == 7:#upper_right
        upper_right = [(x,y) for x,y in zip(range(field[0]+1,chessboard_size,1),range(field[1]-1,-1,-1))]
        if len(upper_right)==0:
            return ''
        for coord in upper_right:
            for idx,xy in enumerate(  zip( range(coord[0],field[0],-1),range(coord[1],field[1],1) ) ):
                if idx==0:
                    sentence += Queen(xy[0],xy[1])
                else:
                    #s_part = '&(~'+Pawn(xy[0],xy[1])+')'
                    s_part = '&((~'+Pawn(xy[0],xy[1])+')|('+Danger(xy[0],xy[1])+'))'
                    sentence += s_part
            sentence += '|'
    return sentence

def inference(chessboard_array,field):
    """
    If chessboard_array[field[0]][field[1]]==0, write sentences to predict whether D[field[0],filed[1]] hold
    
    Input: 
        chessboard_array[field[0]][field[1]]==0
    Return:
        sentence: string
        A sentence template: 
            'row_danger(i,j) | col_danger(i,j) | diag_danger(i,j) | subdiag_danger(i,j) ==> D(i,j)'
    """
    chessboard_size = len(chessboard_array)
    
    #1.check row
    left = subsentence(chessboard_array,field,0)
    right = subsentence(chessboard_array,field,1)
    row = left+right

    #2.check column
    upper = subsentence(chessboard_array,field,2)
    lower = subsentence(chessboard_array,field,3)
    col = upper+lower
    
    #3.check diagonal
    upper_left = subsentence(chessboard_array,field,4)
    lower_right = subsentence(chessboard_array,field,5)
    diag = upper_left+lower_right
    
    #4.check subdiagonal
    lower_left = subsentence(chessboard_array,field,6)
    upper_right = subsentence(chessboard_array,field,7)
    subdiag = lower_left+upper_right
    # combine all subsentences 
    #sentence = row+'|'+col+'|'+diag+'|'+subdiag+'==>'+Danger(field[0],field[1])
    sentence = row+col+diag+subdiag
    sentence = sentence[:-1]
    sentence += '==>'+Danger(field[0],field[1])
    return sentence