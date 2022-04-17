"""
This library uses Prim's Algorithm to generate mazes. It follows the followign tutorial.
https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e
"""
from colorama import init,Fore
from random import random

cell='c'
wall='w'

class Maze():
    """
    Class that handles the maze's execution, generation and sotrage
    """
    init() #Initialices colorama
    maze=[] #We store here the actual state of the maze
    walls=[] #List of walls
    height=0
    width=0
    #initialization of an empty maze at definition of the instance
    def __init__(self,width,height) -> None:
        ######
        #STEP 1 OF PRIM'S ALGORITHM
        # Start with a grid full of walls
        ######
        self.height=height
        self.width=width
        for i in range(0,height):
            line=[]
            for j in range(0,width):
                line.append('u')
            self.maze.append(line)
    
    #Prints the state of the maze on the screen. For debuggin porpouses
    def print_maze(self) -> None:
        for i in range(0,len(self.maze)):
            for j in range(0,len(self.maze[i])):
                if self.maze[i][j]=='u': print(Fore.WHITE,f'{self.maze[i][j]}',end="")
                elif self.maze[i][j]=='c': print(Fore.GREEN,f'{self.maze[i][j]}',end="")
                elif self.maze[i][j]=='w': print(Fore.RED,f'{self.maze[i][j]}',end="")
                else: print(f'ERROR {self.maze[i][j]}',end="")
            print('\n')
    
    def create(self):
        #######
        #STEP 2 OF PRIM'S ALGORITHM:
        #Pick a cell, mark it as part of the maze. Add the walls of the cell to the walls of the list
        #######
        #Select a random block to start with that is not on the edge of the maze
        starting_height=int(random()*self.height)
        starting_width=int(random()*self.width)
        
        if starting_height==0: starting_height+=1
        if starting_height==self.height-1: starting_height-=1

        if starting_width==0: starting_width+=1
        if starting_width==self.width-1: starting_width-=1

        #Mark that block as a cell and include the surrounding blocks in the wall list and in the maze as walls
        self.maze[starting_height][starting_width]=cell
        self.walls.append([starting_height-1,starting_width])
        self.walls.append([starting_height,starting_width-1])
        self.walls.append([starting_height+1,starting_width])
        self.walls.append([starting_height,starting_width+1])

        self.maze[starting_height-1][starting_width]=wall
        self.maze[starting_height][starting_width-1]=wall
        self.maze[starting_height+1][starting_width]=wall
        self.maze[starting_height][starting_width+1]=wall

        #######
        #STEP 3 OF PRIM'S ALGORITHM
        # While there are walls in the list:
        #     1. Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
        #         a) Make the wall a passage and mark the unvisited cell as part of the maze
        #         b) Add the neighboring walls of the cell to the wall list.
        #     2. Remove the wall from the list
        #######

        while self.walls:
            rand_wall=self.walls[int(random()*len(self.walls))-1]
            if rand_wall[1]!=0:#To the left u and to the right c
                if self.maze[rand_wall[0]][rand_wall[1]-1]=='u' and self.maze[rand_wall[0]][rand_wall[1]+1]=='c':
                    if self.sorroundingCells(rand_wall)<2:
                        self.maze[rand_wall[0]][rand_wall[1]]=cell
                        #The wall bellow
                        if rand_wall[0]!=0:
                            if self.maze[rand_wall[0]-1][rand_wall[1]]!=cell:
                                self.maze[rand_wall[0]-1][rand_wall[1]]=wall
                            if [rand_wall[0]-1,rand_wall[1]] not in self.walls:
                                self.walls.append([rand_wall[0]-1,rand_wall[1]])
                        #The wall above
                        if rand_wall[0]!=self.height-1:
                            if self.maze[rand_wall[0]+1][rand_wall[1]]!=cell:
                                self.maze[rand_wall[0]+1][rand_wall[1]]=wall
                            if [rand_wall[0]+1,rand_wall[1]] not in self.walls:
                                self.walls.append([rand_wall[0]+1,rand_wall[1]])
                        #The wall to the left. As it is in the condition it is already checked
                        self.maze[rand_wall[0]][rand_wall[1]-1]=wall
                        if [rand_wall[0],rand_wall[1]-1] not in self.walls:
                            self.walls.append([rand_wall[0],rand_wall[1]+1])
                    self.delete_wall(rand_wall)
                    continue
                continue
            if rand_wall[1]!=self.width-1: #To the right u and to the left c
                if self.maze[rand_wall[0]][rand_wall[1]+1]=='u' and self.maze[rand_wall[0]][rand_wall[1]-1]=='c':
                    if self.sorroundingCells(rand_wall)<2:
                        self.maze[rand_wall[0]][rand_wall[1]]=cell
                        #The wall bellow
                        if rand_wall[0]!=0:
                            if self.maze[rand_wall[0]-1][rand_wall[1]]!=cell:
                                self.maze[rand_wall[0]-1][rand_wall[1]]=wall
                            if [rand_wall[0]-1,rand_wall[1]] not in self.walls:
                                self.walls.append([rand_wall[0]-1,rand_wall[1]])
                        #The wall above
                        if rand_wall[0]!=self.height-1:
                            if self.maze[rand_wall[0]+1][rand_wall[1]]!=cell:
                                self.maze[rand_wall[0]+1][rand_wall[1]]=wall
                            if [rand_wall[0]+1,rand_wall[1]] not in self.walls:
                                self.walls.append([rand_wall[0]+1,rand_wall[1]])
                        #The wall to the right. As it is in the condition it is already checked
                        self.maze[rand_wall[0]][rand_wall[1]+1]=wall
                        if [rand_wall[0],rand_wall[1]+1] not in self.walls:
                            self.walls.append([rand_wall[0],rand_wall[1]+1])
                    self.delete_wall(rand_wall)
                    continue
                continue
            if rand_wall[0]!=0: #Bellow u and above c
                if self.maze[rand_wall[0]-1][rand_wall[1]]=='u' and self.maze[rand_wall[0]+1][rand_wall[1]]=='c':
                    if self.sorroundingCells(rand_wall)<2:
                        self.maze[rand_wall[0]][rand_wall[1]]=cell
                        #The wall to the right
                        if rand_wall[1]!=self.width-1:
                            if self.maze[rand_wall[0]][rand_wall[1]+1]!=cell:
                                self.maze[rand_wall[0]][rand_wall[1]+1]=wall
                            if [rand_wall[0],rand_wall[1]+1] not in self.walls:
                                self.walls.append([rand_wall[0],rand_wall[1]+1])
                        #The wall to the left
                        if rand_wall[1]!=0:
                            if self.maze[rand_wall[0]][rand_wall[1]-1]!=cell:
                                self.maze[rand_wall[0]][rand_wall[1]-1]=wall
                            if [rand_wall[0],rand_wall[1]-1] not in self.walls:
                                self.walls.append([rand_wall[0],rand_wall[1]-1])
                        #The wall bellow
                        self.maze[rand_wall[0]-1][rand_wall[1]]=wall
                        if [rand_wall[0]-1,rand_wall[1]] not in self.walls:
                            self.walls.append([rand_wall[0]-1,rand_wall[1]])
                    self.delete_wall(rand_wall)
                    continue
                continue
            if rand_wall[0]!=self.height-1: #Above u and bellow c
                if self.maze[rand_wall[0]+1][rand_wall[1]]=='u' and self.maze[rand_wall[0]-1][rand_wall[1]]=='c':
                    if self.sorroundingCells(rand_wall)<2:
                        self.maze[rand_wall[0]][rand_wall[1]]=cell
                        #The wall to the right
                        if rand_wall[1]!=self.width-1:
                            if self.maze[rand_wall[0]][rand_wall[1]+1]!=cell:
                                self.maze[rand_wall[0]][rand_wall[1]+1]=wall
                            if [rand_wall[0],rand_wall[1]+1] not in self.walls:
                                self.walls.append([rand_wall[0],rand_wall[1]+1])
                        #The wall to the left
                        if rand_wall[1]!=0:
                            if self.maze[rand_wall[0]][rand_wall[1]-1]!=cell:
                                self.maze[rand_wall[0]][rand_wall[1]-1]=wall
                            if [rand_wall[0],rand_wall[1]-1] not in self.walls:
                                self.walls.append([rand_wall[0],rand_wall[1]-1])
                        #The wall above
                        self.maze[rand_wall[0]+1][rand_wall[1]]=wall
                        if [rand_wall[0]+1,rand_wall[1]] not in self.walls:
                            self.walls.append([rand_wall[0]+1,rand_wall[1]])
                    self.delete_wall(rand_wall)
                    continue
                continue
        self.make_walls()
        self.create_entrance_exit()
    def sorroundingCells(self,rand_wall)->int:
        """Returns how many sorounding blocks are actually cells"""
        s_cells=0
        if(self.maze[rand_wall[0]-1][rand_wall[1]]=='c'):
            s_cells+=1
        if(self.maze[rand_wall[0]+1][rand_wall[1]]=='c'):
            s_cells+=1
        if(self.maze[rand_wall[0]][rand_wall[1]+1]=='c'):
            s_cells+=1
        if(self.maze[rand_wall[0]][rand_wall[1]-1]=='c'):
            s_cells+=1
        
        return s_cells
    
    def delete_wall(self,rand_wall)->None:
        for wall in self.walls:
            if wall[0]==rand_wall[0] and wall[1]==rand_wall[1]:
                self.walls.remove(wall)
    
    def make_walls(self)->None:
        for i in range(0,self.height):
            for j in range(0,self.width):
                if self.maze[i][j]=='u':
                    self.maze[i][j]='w'
    
    def create_entrance_exit(self)->None:
        for i in range(0,self.width):
            if self.maze[1][i]=='c':
                self.maze[0][i]=cell
                break
        for i in range(self.width-1,0,-1):
            if self.maze[self.height-1][i]==cell:
                self.maze[self.height-1][i]=cell
                break