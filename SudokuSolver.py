##sudoku solver

import numpy as np

sudoku= np.array([[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]])

#checks if the arrays given for sudoku are of correct size.
for i in range(sudoku.shape[0]):
        if len(sudoku[i])!=9:
            print("wrong")
            break
        else:
            print(f'Row{i}, All is well')
    
    
nums=[1,2,3,4,5,6,7,8,9]
pvr=[]

while True:
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
                
                pvm2=[]     
                if i in range(0,3) and j in range(0,3):
                    
                    for x in range(0,3):
                        for y in range(0,3):
                            pvm2.append(sudoku[x][y]) 
                
                if i in range(0,3) and j in range(3,6):
                    
                    for x in range(0,3):
                        for y in range(3,6):
                            pvm2.append(sudoku[x][y]) 
                            
                if i in range(0,3) and j in range(6,9):
                    
                    for x in range(0,3):
                        for y in range(6,9):
                            pvm2.append(sudoku[x][y]) 
                            
                if i in range(3,6) and j in range(0,3):
                   
                    for x in range(3,6):
                        for y in range(0,3):
                            pvm2.append(sudoku[x][y]) 

                if i in range(3,6) and j in range(3,6):
                
                    for x in range(3,6):
                        for y in range(3,6):
                            pvm2.append(sudoku[x][y]) 
                            
                if i in range(3,6) and j in range(6,9):
                   
                    for x in range(3,6):
                        for y in range(6,9):
                            pvm2.append(sudoku[x][y]) 
                
                if i in range(6,9) and j in range(0,3):
                    
                    for x in range(6,9):
                        for y in range(0,3):
                            pvm2.append(sudoku[x][y]) 
                   
                if i in range(6,9) and j in range(3,6):
                    
                    for x in range(6,9):
                        for y in range(3,6):
                            pvm2.append(sudoku[x][y]) 
                         
                if i in range(6,9) and j in range(6,9):
                    
                    for x in range(6,9):
                        for y in range(6,9):
                            pvm2.append(sudoku[x][y]) 
                            
                #Iterates through each element and appends the numbers not present in the array pvm2                   
                pvm=[]
                for z in nums:
                    if z not in pvm2:
                        pvm.append(z)
                
                #Finds the intersection of pvr, pvc and pvm, and appends those in the array "final"
                final=[]
                for x in nums:
                    if x in pvc:
                        if x in pvr:
                                if x in pvm:
                                    final.append(x)
                #If there is only one element in final, replaces the empty value in sudoku with the solution value, and prints it.
                if len(final)==1:
                    sudoku[i][j]=final[0]
                    print(f'solution for position {i,j} are')
                    for x in final:
                        print(x)
                    else:
                        continue
    #break the loop when the number of empty spaces in the sudoku becomes zero            
    if np.count_nonzero(sudoku==0)==0:
        break
    else:
        continue
    
#prints the final array
for i in range(9):
    print('\n')
    for j in range(9):
        print(sudoku[i][j])


                        
                                
