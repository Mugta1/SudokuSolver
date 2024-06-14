##sudoku solver
##the code is working as of now 



import numpy as np
#Enter your sudoku in the form of 2d matrix 9x9
sudoku=[]

####FIX INPUT HANDLING, CAN BE MADE BETTER
print("Welcome to sudoku solver.\n  Enter your 9x9 Sudoku as prompted. \n For empty spaces, enter 0. \n Enjoy!")
for i in range(9):
    x=input(f'Enter the {i + 1} row of the Sudoku)
    if len(x)==o and x.isdigit():
        y.append(int(a) for a in x)
    if len(sudoku)==9 and len(sudoku.flatten())==81:
        print("All rows recorded successfuly")
        break
    else:
        sudoku.append(y)
for i in range(9):
    print(sudoku[i])
    print("Verify your Sudoku. In case of faults, restart the program.") #add support to re-enter the sudoku without having to restart the program.
    
sudoku=np.array(sudoku)

nums=[1,2,3,4,5,6,7,8,9]
pvr=[]
#use this to find out the number of times the loop ran before finding the solution  
count=0

#main loop
while True:
    #count+=1
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
    
    #break the loop when the number of empty spaces in the sudoku becomes zero            
    if np.count_nonzero(sudoku==0)==0:
        break
    else:
        continue
    
#prints the final array
for i in range(9):
    print(sudoku[i])
#prints the number of times the loop ran before finding the solution       
#print(f"The number of times the loop ran is {count}")


                        
                                
