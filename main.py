import pygame
import sys
from block import *
from food import *
from testthread import *
import threading

pygame.init()
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((640,480))
# None = default font
font = pygame.font.Font(None, 24)
pygame.display.set_caption("Snake: By Matias Grioni")

# Variables specfic for the snake
# Head of the snake at predetermined position
snake = [Block(310, 0, 0, 10)]
foodBlock = Food()
score = 0
running = True

while running:
    window.fill((0, 0, 0))
    
    # Draw each block and also update their position
    for i in range(len(snake)-1, -1, -1):
        pygame.draw.rect(window, (100, 155, 234), snake[i].getRect())
        # if this is the head simply move it forward
        if i == 0:
            # if the snake hits the wall then exit the game
            running = snake[0].advance()

            # if the snake hits itself exit the game
            for i in range(1, len(snake)):
                if snake[0].getRect().colliderect(snake[i].getRect()):
                    running = False
            
            # If the head of the snake and the food collide then...
            # increase the snake length by 1
            if snake[0].getRect().colliderect(foodBlock.getRect()):
                # Add a block to the end of the snake
                snake.append(snake[-1].blockBehind())
                # also create a new food block
                foodBlock = Food()
                score += 1
        # Otherwise move the block to the block in front
        else:
            snake[i].copy(snake[i-1])

    pygame.draw.rect(window, (70, 171, 105), foodBlock.getRect())
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(text, (10, 10))
            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake[0].turnLeft()
            elif event.key == pygame.K_RIGHT:
                snake[0].turnRight()
            elif event.key == pygame.K_DOWN:
                snake[0].moveDown()
            elif event.key == pygame.K_UP:
                snake[0].moveUp()
                 

    pygame.display.update()
    fpsClock.tick(30)

# Finish it off
pygame.quit()
sys.exit()
