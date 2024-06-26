##sudoku solver
##the code is working as of now 


import time
import numpy as np

#Enter your sudoku in the form of 2d matrix 9x9
#input function, takes inputs in the form of a 9 length array, 9 times, to form and return a 9x9 array(sudoku)
def inputsud():
    sudoku=[] #initializing the sudoku array
    for i in range(9):
        while True:
            x=input(f'Enter the {i + 1} row of the Sudoku: ') #takes an array with 9 integers as an input and appends it into the sudoku array
            if len(x)==9 and x.isdigit():
                y=[int(a) for a in x]
                sudoku.append(y)
                break
            else:
                print("Wrong input. Please try again. ")
    return sudoku  #returns the 2d array [9x9] as an output


#The main solving algorithm     
def sudokusolve(sudoku):
    starttime=time.time()
    sudoku=np.array(sudoku)
    count=0

    nums=[1,2,3,4,5,6,7,8,9]
    pvr=[]
    #main loop
    while True:
        start=sudoku.copy()
        count+=1  
        for i in range(0,9):
            for j in range(0,9):
                if sudoku[i][j]==0:
                    
                    #Iterates through horizontal rows and appends the numbers not present into array pvr
                    pvr=[]
                    for x in nums:
                        if x not in sudoku[i]:
                            pvr.append(x)
                            
                    
                    #Creates an array col of elements in the column
                    col=[]
                    for x in range(sudoku.shape[0]):
                        col.append(sudoku[x][j])
                        
                    #Iterates through vertical columns and appends the numbers not present into array pvc
                    pvc=[]
                    for x in nums:
                        if x not in col:
                            pvc.append(x)    
                            
                            
                    #3x3 local check
                    #Creates an array of all elements in the 3x3 Matrix.
                    #I was using multiple loops before to solve this. the method down below is a much better one to separate out the matrix into 3x3 mini-matrix-s
                    pvm2=[]     
                    start_x= (i//3)*3
                    start_y=(j//3)*3
                    for x in range(start_x, start_x+3):
                        for y in range(start_y, start_y+3):
                            pvm2.append(sudoku[x][y])                    
                                
                    #Iterates through each element and appends the numbers not present in the array pvm2                   
                    pvm=[]
                    for z in nums:
                        if z not in pvm2:
                            pvm.append(z)
                    
                    #Finds the intersection of pvr, pvc and pvm, and appends those in the array "final"
                    subintersect= np.intersect1d(pvc, pvm)
                    final=np.intersect1d(pvr, subintersect)
                    #If there is only one element in final, replaces the empty value in sudoku with the solution value, and prints it.
                    if len(final)==1:
                        sudoku[i][j]=final[0]
                        print(f'solution for position {i,j} are {final[0]}')
                    else: 
                        continue
        #Checks if any changes have been made to the array.
        if np.array_equal(sudoku,start):
            print("The given Sudoku has no solutions. Wrong Sudoku Input TwT")
            break
        #if no changes have been made to the sudoku, it will end the program to avoid an infinite loop
        
        #break the loop when the number of empty spaces in the sudoku becomes zero            
        elif np.count_nonzero(sudoku==0)==0:
            #prints the final array
    
            print(f "{sudoku}")
            break
        else:
            continue
    endtime=time.time()
    print(f'The total time taken in solving this sudoku is {endtime-starttime} seconds')
    print(f'The loop ran {count} times.')
    
        
   
        

# main function
def main():
    print("Welcome to sudoku solver.\n  Enter your 9x9 Sudoku as prompted. \n For empty spaces, enter 0. \n Enjoy! ^-^")
    sudoku=inputsud()
    print(f "{sudoku}")
    print("Verify your Sudoku.")
    #Gives the user an opportunity to check if the sudoku input is correct, if not, they can chose to enter the sudoku again.
    check=input("Is the sudoku correct? \n 1. Yes 2. No \n")
    if check.lower()=="no" or check=='2':
        #Enter the Sudoku again
        inputsud()
    if check.lower()=='yes' or check=='1':
        #Solve the sudoku and print the values.
        sudokusolve(sudoku)

main()
