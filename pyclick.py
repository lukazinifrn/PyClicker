import pygame
from sys import exit

# Geral Configs
pygame.init()
window_width = 1080
window_height = 540
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("PyClicker")
clock = pygame.time.Clock()

# Fonts 
font = pygame.font.Font("font/Pixeltype.ttf", 30)

# Python
python_click = pygame.image.load("sprites\pythonlogo.png")
python_click = pygame.transform.scale_by(python_click, 1.4)
python_click_rect = python_click.get_rect(center = (156, window_height/2))

# Title
gametitle = font.render("PyClicker!", False, (185, 209, 0))
gametitle = pygame.transform.scale_by(gametitle, (2 + 1/3))
gametitle_rect = gametitle.get_rect(topleft = (32, 16))

# Click Uptade
pyclick_uptade = pygame.image.load("sprites/pyclick-uptade.png")
pyclick_uptade = pygame.transform.scale_by(pyclick_uptade, 0.4)
pyclick_uptade_rect = pyclick_uptade.get_rect(topleft = (780, 72))

# Game States
game_running = True

# Functional variables
pycoin = 0
pycoin_click = 1
pycoin_click_coust = 1
pycoin_click_coust_total = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_running:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if python_click_rect.collidepoint(event.pos):
                    pycoin += pycoin_click
                
                if pyclick_uptade_rect.collidepoint(event.pos) and pycoin >= 10 * pycoin_click_coust:
                    pycoin_click += 1
                    pycoin -= 10 * pycoin_click_coust
                    pycoin_click_coust += 1
                    pycoin_click_coust_total = 10 * pycoin_click_coust
                    
    # PyCoins display
    show_coins = font.render(f"{pycoin} PyCoins", False, (185, 209, 0))
    show_coins = pygame.transform.scale_by(show_coins, (1 + 2/3))
    show_coins_rect = show_coins.get_rect(topright = (window_width - 64, 32))
    
    # PyClick coust
    pyclick_text = font.render(f"Custo: {pycoin_click_coust_total}", False, "black")
    pyclick_text_rect = pyclick_text.get_rect(center = (920, pyclick_uptade_rect.centery))
    
    if game_running:
        screen.fill((0, 94, 255))
        screen.blit(python_click, python_click_rect)
        screen.blit(show_coins, show_coins_rect)
        screen.blit(gametitle, gametitle_rect)
        screen.blit(pyclick_uptade, pyclick_uptade_rect)
        screen.blit(pyclick_text, pyclick_text_rect)
        
        
    pygame.display.update()
    clock.tick(60)