import pygame
from sudokugrid import SudokuGrid, SudokuNode, draw_grid
from sudoku_patterns import get_pattern
from sudokusolver import SudokuSolver

def play_sudoku(screen):

    pattern = get_pattern('easy')

    grid = SudokuGrid(pattern)
    grid.initialize_nodes()
    
    solver = SudokuSolver()
    solver.remove_colrowcube(grid.nodes)
    solver.remove_colrowcube(grid.nodes)
    solver.remove_colrowcube(grid.nodes)
    solver.remove_colrowcube(grid.nodes)

    
    grid.draw_pattern(screen)
        


def main():
    
    pygame.init()
    
    pygame.display.set_caption('Sudoku')
    

    screen_width = 721
    screen_height = 721
    screen = pygame.display.set_mode((screen_width,screen_height))
    
    draw_grid(screen)
    play_sudoku(screen)


    pygame.display.flip()
    
    running = True
    
    while running:
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

                

if __name__ == '__main__':
    main()