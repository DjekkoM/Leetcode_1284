import numpy as np
import pygame


def flip(i,j):
    M[i][j] = np.logical_not(M[i][j])
    return(M[i][j])
def Flip(i,j):
    flip(i,j)
    if i == n-1:
        if j == 0:
            flip(i-1, j)
            flip(i, j+1)
        else:
            if j == m-1:
                flip(i-1, j)
                flip(i, j-1)
            else:
                flip(i,j-1)
                flip(i,j+1)
                flip(i-1,j)
          
    else:
        if i == 0:
            if j == 0:
                flip(i+1, j)
                flip(i, j+1)
            else:
                if j==m-1:
                    flip(i+1, j)
                    flip(i, j-1)
                else:
                    flip(i,j-1)
                    flip(i,j+1)
                    flip(i+1,j)            
        else:
            if j == 0:
                flip(i-1,j)
                flip(i+1,j)
                flip(i,j+1)
            
            else:
                if j == m-1:
                    flip(i-1,j)
                    flip(i+1,j)
                    flip(i,j-1)
                else:    
                    flip(i+1, j)
                    flip(i-1, j)
                    flip(i, j-1)
                    flip(i, j+1)
    return(M)


print("This game is designed to help in visualizing the leetcode task #1284. The red squares represent values of 1 in the matrix, while white squares represent 0. The user applies the defined transformation from the task by clicking on the square he wishes to act upon.")
print('The input is a binary matrix of size mxn with the user inputing the values of m and n. (m, n are integers where m > 0 and n < 4)')
print('Please enter the value for m:')
m = int(input())
print('Please enter the value for n')
n = int(input())
if n > 3:
    print("Input values not allowed")
else:   
    print('Do you want the matrix to be randomized? Y/N')
    x = str(input())
    if x == 'Y' or x == 'y':
        M = np.random.choice(a = [True,False], size =(n,m))
    else:
        print("Enter the entries rowwise:")
        matrix = []
        for k in range(n):          
            a =[]
            for l in range(m):
                y = int(input())
                if y == 1:
                    z = True
                else:
                    z = False
                print(z)
                a.append(z)
            matrix.append(a)
        M = np.array(matrix)

    print(np.array(M,dtype=int))
    
    
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    WIDTH = 100
    HEIGHT = 100
    MARGIN = 1
    pygame.init()
    window_size = [m*WIDTH+1, n*HEIGHT+1]
    scr = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Matrix flip")
    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                np.array(Flip(row,column), dtype = int)
                # print("Click ", pos, "Grid coordinates: ", row, column)
        scr.fill(black)
        for row in range(n):
            for column in range(m):
                color = white
                if M[row][column] == 1:
                    color = red
                pygame.draw.rect(scr,color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        clock.tick(50)
        pygame.display.flip()
    pygame.quit()