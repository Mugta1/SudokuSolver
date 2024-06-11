##sudoku solver

import numpy as np

sudoku= np.array([[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]])

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
                pvr=[]
                for x in nums:
                    if x not in sudoku[i]:
                        pvr.append(x)
                
                col=[]
                for x in range(sudoku.shape[0]):
                    col.append(sudoku[x][j])
                pvc=[]
                for x in nums:
                    if x not in col:
                        pvc.append(x)       
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
                   
                pvm=[]
                for z in nums:
                    if z not in pvm2:
                        pvm.append(z)
                final=[]
                for x in nums:
                    if x in pvc:
                        if x in pvr:
                            final.append(x)

                if len(final)==1:
                    sudoku[i][j]=final[0]
                    print(f'solution for position {i,j} are')
                    for x in final:
                        print(x)
                    else:
                        continue
                else: 
                    pvr=[]
                    for x in nums:
                        if x not in sudoku[i]:
                            pvr.append(x)
                    
                    
                    col=[]
                    for x in range(sudoku.shape[0]):
                        col.append(sudoku[x][j])
                    pvc=[]
                    for x in nums:
                        if x not in col:
                            pvc.append(x)           
                    final=[]
                    if x in pvc:
                        if x in pvr:
                            final.append(x)
                   

                    if len(final)==1:
                        sudoku[i][j]=final[0]
                        print(f'solution for position {i,j} are')
                        for x in final:
                            print(x)
    if np.count_nonzero(sudoku==0)==0:
        break
    else:
        continue
for i in range(9):
    for j in range(9):
        print(sudoku[i][j])


                        
                                