import pygame
import sys
pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("КликерX")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

background = pygame.image.load("Zhdun.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

font = pygame.font.SysFont('Arial', 50)


clicks = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1
    screen.blit(background, (0, 0))
    

    text = font.render(f"Кликов: {clicks}", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH//2, 50))
    

    text_bg = pygame.Surface((text_rect.width + 20, text_rect.height + 10))
    text_bg.set_alpha(180) 
    text_bg.fill(WHITE)
    screen.blit(text_bg, (text_rect.x - 10, text_rect.y - 5))
    
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()