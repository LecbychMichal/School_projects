import pygame
from random import randrange



pygame.init()
screen_size = 800
cell_size = 20
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Pathfinding")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
rows = screen_size // cell_size
columns = screen_size // cell_size



class Node:
    def __init__(self, row, column, cell_size):
        self.color = white
        self.visited = False
        self.row = row
        self.column = column
        self.neighbours = []
        self.f = 0
        self.g = 0
        self.h = 0
    
    def Make_barrier(self):
        self.color = black
        self.visited = True
    
    def Make_visited(self):
        self.color = green
        self.visited = True

    def Draw_nodes(self, row, column):
        pygame.draw.rect(screen, self.color, (self.row * cell_size, self.column * cell_size, cell_size, cell_size))

    def Draw_path(self, row, column):
        pygame.draw.rect(screen, self.color, (self.row * cell_size + 2, self.column * cell_size + 2, cell_size - 2, cell_size - 2))

    def Set_Neighbours(self, NodeList, rows, columns):
        if self.column < columns-1 and NodeList[self.row][self.column + 1].visited == False:
            self.neighbours.append(NodeList[self.row][self.column + 1])
        if self.column > 0 and NodeList[self.row][self.column - 1].visited == False:
            self.neighbours.append(NodeList[self.row][self.column - 1])
        if self.row > 0 and NodeList[self.row - 1][self.column].visited == False:
            self.neighbours.append(NodeList[self.row - 1][self.column])
        if self.row < rows-1 and NodeList[self.row + 1][self.column].visited == False:
            self.neighbours.append(NodeList[self.row + 1][self.column])

def Init_background():
    NodeList = []
    for row in range(rows):
        NodeList.append([])
        for column in range(columns):
            node = Node(row, column, cell_size)
            NodeList[row].append(node)
    Draw_background(NodeList, node)

    return NodeList, row, column

def Draw_background(NodeList, node):
    Set_barriers(NodeList)
    Set_start_end(NodeList)
    

    for row in range(rows):
        for column in range(columns):  
            NodeList[row][column].Draw_nodes(row, column)
            #NodeList[row][column].Set_Neighbours(NodeList, rows, columns)
            Draw_grid(row, column)

def Draw_grid(row, column):
        pygame.draw.line(screen, black, (row * cell_size, column * cell_size), (row * cell_size + cell_size, column * cell_size), 2)
        pygame.draw.line(screen, black, (row * cell_size, column * cell_size), (row * cell_size, column * cell_size + cell_size), 2)

def Set_barriers(NodeList):
    for i in range(5, 13):
        for j in range(5, 15):
            NodeList[i][j].Make_barrier()
    for i in range(28, 33):
        for j in range(0, 8):
            NodeList[i][j].Make_barrier()

    for i in range(33, 37):
        for j in range(35, 40):
            NodeList[i][j].Make_barrier()
    
    for i in range(30, 37):
        for j in range(21, 31):
            NodeList[i][j].Make_barrier()

    for i in range(21, 26):
        for j in range(9, 17):
            NodeList[i][j].Make_barrier()

    for i in range(5, 15):
        for j in range(22, 37):
            NodeList[i][j].Make_barrier()
 
def Set_start_end(NodeList):
    NodeList[0][0].visited = 1
    NodeList[0][0].color = green
    NodeList[rows-1][columns-1].color = red
   
def BreadthFirstSearch(NodeList, row, column):
    Stack = []
    start = NodeList[0][0]
    end = NodeList[rows-1][columns-1]
    current = start
    Stack.append(start)
    i = 0
    while Stack:
        current.Set_Neighbours(NodeList, rows, columns)
        i += 1
        if len(Stack) > 0 and current != end:
            for node in current.neighbours:
                Stack.append(node)
                node.Make_visited()
            Stack.pop(0)
            current = Stack[0]
            current.Draw_path(row, column)
            pygame.display.update()
        else:
            print("cíl nalezen")
            return
        

def DepthFirstSearch(NodeList, row, column):
    Queue = []
    start = NodeList[0][0]
    end = NodeList[rows-1][columns-1]
    current = start
    Queue.append(start)
    i = 0
    while Queue:
        current.Set_Neighbours(NodeList, rows, columns)
        i += 1
        if len(Queue) > 0 and current != end:
            for node in current.neighbours:
                Queue.append(node)
                node.Make_visited()
            current = Queue.pop()
            current.Draw_path(row, column)
            pygame.display.update()
        else:
            print("cíl nalezen")
            return


def main():
    run = True
    NodeList, row, column = Init_background()
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                BreadthFirstSearch(NodeList, row, column)
                # DepthFirstSearch(NodeList, row, column)
    pygame.quit()


if __name__ == "__main__":
    main()