import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
screen.fill('Light Blue')
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('src/assets/font/font.ttf', 30)

sky_surface = pygame.image.load('src/assets/img/background.png').convert()
ground_surface = pygame.image.load('src/assets/img/ground.png').convert_alpha()
text_surface = test_font.render('My game', False, 'Black')

slime_surface = pygame.image.load('src/assets/img/slime.png').convert_alpha()
slime_x_pos = 600

player_surf = pygame.image.load('src/assets/img/character2.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))      
    screen.blit(ground_surface, (0, 320))
    screen.blit(text_surface, (300, 50))
    
    screen.blit(slime_surface, (slime_x_pos, 290))
    slime_x_pos -= 3
    if slime_x_pos < -100:
        slime_x_pos = 800
        
    screen.blit(player_surf, (89, 200))
            
    pygame.display.update()
    clock.tick(60)