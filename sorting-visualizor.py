import pygame
import random

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH = 800
HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Display settings
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")
clock = pygame.time.Clock()

# Array of numbers to sort
arr = [random.randint(10, HEIGHT - 10) for _ in range(WIDTH // 2)]

# Bubble Sort
def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_window(array, j)
                pygame.time.delay(1)

# Draw the current state of the array
def draw_window(array, index):
    win.fill(WHITE)

    for i in range(len(array)):
        color = BLUE if i == index or i == index + 1 else BLACK
        pygame.draw.rect(win, color, (2 * i, HEIGHT - array[i], 2, array[i]))

    pygame.display.update()

# Main game loop
def main():
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        bubble_sort(arr)

    pygame.quit()

# Start the program
if __name__ == "__main__":
    main()
