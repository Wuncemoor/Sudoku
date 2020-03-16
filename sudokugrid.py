import pygame

class SudokuGrid:
    
    def __init__(self, pattern=None):
    
        self.nodes = []
        self.pattern = pattern
        
    def initialize_nodes(self):
        x,y = 1, 1

        for i in range(81):
            
            node = self.get_node()
            self.fill_node(x, y, node)
            self.nodes.append(node)
            if x == 9:
                x = 1
                y += 1
            else:
                x += 1
    def fill_node(self, x, y, node):
    
        cubedict = { 
            (1,1): 1, (2,1): 1, (3,1): 1, (4,1): 2, (5,1): 2, (6,1): 2, (7,1): 3, (8,1): 3, (9,1): 3,
            (1,2): 1, (2,2): 1, (3,2): 1, (4,2): 2, (5,2): 2, (6,2): 2, (7,2): 3, (8,2): 3, (9,2): 3,
            (1,3): 1, (2,3): 1, (3,3): 1, (4,3): 2, (5,3): 2, (6,3): 2, (7,3): 3, (8,3): 3, (9,3): 3,
            (1,4): 4, (2,4): 4, (3,4): 4, (4,4): 5, (5,4): 5, (6,4): 5, (7,4): 6, (8,4): 6, (9,4): 6,
            (1,5): 4, (2,5): 4, (3,5): 4, (4,5): 5, (5,5): 5, (6,5): 5, (7,5): 6, (8,5): 6, (9,5): 6,
            (1,6): 4, (2,6): 4, (3,6): 4, (4,6): 5, (5,6): 5, (6,6): 5, (7,6): 6, (8,6): 6, (9,6): 6,
            (1,7): 7, (2,7): 7, (3,7): 7, (4,7): 8, (5,7): 8, (6,7): 8, (7,7): 9, (8,7): 9, (9,7): 9,
            (1,8): 7, (2,8): 7, (3,8): 7, (4,8): 8, (5,8): 8, (6,8): 8, (7,8): 9, (8,8): 9, (9,8): 9,
            (1,9): 7, (2,9): 7, (3,9): 7, (4,9): 8, (5,9): 8, (6,9): 8, (7,9): 9, (8,9): 9, (9,9): 9,
            }
    

        node.column = x
        node.row = y
        node.cube = cubedict[(x, y)]
        node.startval = self.pattern[(x, y)]
        node.endval = self.pattern[(x, y)]

        
    def get_node(self):  
        return SudokuNode()   

    def draw_pattern(self, screen):

        WHITE = pygame.Color(255,255,255)
        RED = pygame.Color(255,0,0)
        BLACK = pygame.Color(0,0,0)
        
        x,y = 65, 65
        font = pygame.font.Font('freesansbold.ttf', 65)
        
        numbers = []
        
        for i in self.nodes:
            if i.endval is not None:
                if i.startval == i.endval:
                    text = font.render(str(i.endval), True, WHITE, BLACK)
                    textRect = text.get_rect()
                    textRect.center = i.get_center()
                    screen.blit(text, textRect)
                else:
                    text = font.render(str(i.endval), True, RED, BLACK)
                    textRect = text.get_rect()
                    textRect.center = i.get_center()
                    screen.blit(text, textRect)
       
class SudokuNode:
    
    def __init__(self, column=None, row=None, cube=None):
    
        self.column = column
        self.row = row 
        self.cube = cube
        self.startval = None
        self.endval = None
        self.possibilities = [0,1,2,3,4,5,6,7,8,9]
        
    def get_center(self):
    
        
        centerdict = { 
            (1,1):  (47.5, 47.5), (2,1):  (123.5, 47.5), (3,1):  (199.5, 47.5), (4,1):  (284.5, 47.5), (5,1):  (360.5, 47.5), (6,1):  (436.5, 47.5), (7,1):  (521.5, 47.5), (8,1):  (597.5, 47.5), (9,1):  (673.5, 47.5),
            (1,2): (47.5, 123.5), (2,2): (123.5, 123.5), (3,2): (199.5, 123.5), (4,2): (284.5, 123.5), (5,2): (360.5, 123.5), (6,2): (436.5, 123.5), (7,2): (521.5, 123.5), (8,2): (597.5, 123.5), (9,2): (673.5, 123.5),
            (1,3): (47.5, 199.5), (2,3): (123.5, 199.5), (3,3): (199.5, 199.5), (4,3): (284.5, 199.5), (5,3): (360.5, 199.5), (6,3): (436.5, 199.5), (7,3): (521.5, 199.5), (8,3): (597.5, 199.5), (9,3): (673.5, 199.5),
            (1,4): (47.5, 284.5), (2,4): (123.5, 284.5), (3,4): (199.5, 284.5), (4,4): (284.5, 284.5), (5,4): (360.5, 284.5), (6,4): (436.5, 284.5), (7,4): (521.5, 284.5), (8,4): (597.5, 284.5), (9,4): (673.5, 284.5),
            (1,5): (47.5, 360.5), (2,5): (123.5, 360.5), (3,5): (199.5, 360.5), (4,5): (284.5, 360.5), (5,5): (360.5, 360.5), (6,5): (436.5, 360.5), (7,5): (521.5, 360.5), (8,5): (597.5, 360.5), (9,5): (673.5, 360.5),
            (1,6): (47.5, 436.5), (2,6): (123.5, 436.5), (3,6): (199.5, 436.5), (4,6): (284.5, 436.5), (5,6): (360.5, 436.5), (6,6): (436.5, 436.5), (7,6): (521.5, 436.5), (8,6): (597.5, 436.5), (9,6): (673.5, 436.5),
            (1,7): (47.5, 521.5), (2,7): (123.5, 521.5), (3,7): (199.5, 521.5), (4,7): (284.5, 521.5), (5,7): (360.5, 521.5), (6,7): (436.5, 521.5), (7,7): (521.5, 521.5), (8,7): (597.5, 521.5), (9,7): (673.5, 521.5),
            (1,8): (47.5, 597.5), (2,8): (123.5, 597.5), (3,8): (199.5, 597.5), (4,8): (284.5, 597.5), (5,8): (360.5, 597.5), (6,8): (436.5, 597.5), (7,8): (521.5, 597.5), (8,8): (597.5, 597.5), (9,8): (673.5, 597.5),
            (1,9): (47.5, 673.5), (2,9): (123.5, 673.5), (3,9): (199.5, 673.5), (4,9): (284.5, 673.5), (5,9): (360.5, 673.5), (6,9): (436.5, 673.5), (7,9): (521.5, 673.5), (8,9): (597.5, 673.5), (9,9): (673.5, 673.5),
            }
     
        return centerdict[(self.column, self.row)]
        




    
def draw_grid(screen):

    GREY = pygame.Color(100,100,100)
    pygame.draw.rect(screen, GREY, pygame.Rect(0,0,10,721))
    pygame.draw.rect(screen, GREY, pygame.Rect(711,0,10,721))
    pygame.draw.rect(screen, GREY, pygame.Rect(0,0,721,10))
    pygame.draw.rect(screen, GREY, pygame.Rect(0,711,721,10))
    
    pygame.draw.rect(screen, GREY, pygame.Rect(237,0,10,721))
    pygame.draw.rect(screen, GREY, pygame.Rect(474,0,10,721))
    pygame.draw.rect(screen, GREY, pygame.Rect(0,237,721,10))
    pygame.draw.rect(screen, GREY, pygame.Rect(0,474,721,10))
    
    pygame.draw.rect(screen, GREY, pygame.Rect(85,0,1,721))
    pygame.draw.rect(screen, GREY, pygame.Rect(161,0,1,721))
    pygame.draw.rect(screen, GREY, pygame.Rect(322,0,1,721))
    pygame.draw.rect(screen, GREY, pygame.Rect(398,0,1,721))
    pygame.draw.rect(screen, GREY, pygame.Rect(559,0,1,721))
    pygame.draw.rect(screen, GREY, pygame.Rect(635,0,1,721))

    pygame.draw.rect(screen, GREY, pygame.Rect(0,85,721,1))
    pygame.draw.rect(screen, GREY, pygame.Rect(0,161,721,1))
    pygame.draw.rect(screen, GREY, pygame.Rect(0,322,721,1))
    pygame.draw.rect(screen, GREY, pygame.Rect(0,398,721,1))
    pygame.draw.rect(screen, GREY, pygame.Rect(0,559,721,1))
    pygame.draw.rect(screen, GREY, pygame.Rect(0,635,721,1))
    

