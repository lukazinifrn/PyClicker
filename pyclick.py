import pygame
from sys import exit

# Geral Configs
pygame.init()
window_width = 1080
window_height = 540
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("PyClicker")
clock = pygame.time.Clock()
main_color = (0, 94, 255) # Blue
secundary_color = (185, 209, 0) # Yellow
# Fonts 
font = pygame.font.Font("font/Pixeltype.ttf", 30)

# Python
python_click = pygame.image.load("sprites\pythonlogo.png")
python_click = pygame.transform.scale_by(python_click, 2)
python_click_rect = python_click.get_rect(center = (window_width/2 - 100, window_height/2))

# Title
gametitle = font.render("PyClicker!", False, secundary_color)
gametitle = pygame.transform.scale_by(gametitle, (3))
gametitle_rect = gametitle.get_rect(topleft = (32, 16))

# Click Update
pyclick_uptade = pygame.image.load("sprites/pyclick-uptade.png")
pyclick_uptade = pygame.transform.scale_by(pyclick_uptade, 0.4)
pyclick_uptade_rect = pyclick_uptade.get_rect(topleft = (250, 50))

# Buttons _______________________________________________________________________

# Upgrades
button_to_upgrades = pygame.image.load("sprites/button.png")
button_to_upgrades = pygame.transform.scale_by(button_to_upgrades, 1.7)
button_to_upgrades_rect = button_to_upgrades.get_rect(topleft = (700, 80))

# Generators
button_to_generators = pygame.image.load("sprites/button.png")
button_to_generators = pygame.transform.scale_by(button_to_generators, 1.7)
button_to_generators_rect = button_to_upgrades.get_rect(topleft = (700, 280))

# Returns
return_to = pygame.image.load("sprites/button.png")
return_to = pygame.transform.scale_by(return_to, 0.9)
return_rect = button_to_upgrades.get_rect(topleft = (20, 20))

# Button Click Update
button_to_pyclick_update = pygame.image.load("sprites/button.png")
button_to_pyclick_update = pygame.transform.scale_by(button_to_pyclick_update, 0.7)
button_to_pyclick_update_rect = button_to_pyclick_update.get_rect(center = (pyclick_uptade_rect.centerx + 120, pyclick_uptade_rect.centery))

# Texts
text_upgrade = font.render("Upgrades", False, main_color)
text_upgrade = pygame.transform.scale_by(text_upgrade, 2)
text_upgrade_rect = text_upgrade.get_rect(center = (button_to_upgrades_rect.centerx, button_to_upgrades_rect.centery))

text_generators = font.render("Generators", False, main_color)
text_generators = pygame.transform.scale_by(text_generators, 2)
text_generators_rect = text_upgrade.get_rect(center = (button_to_generators_rect.centerx, button_to_generators_rect.centery))

text_return = font.render("Return", False, main_color)
text_return = pygame.transform.scale_by(text_return, 1.5)
text_return_rect = text_upgrade.get_rect(center = (return_rect.centerx*0.8, return_rect.centery*0.7))


# ______________________________________________________________________________

# Game States
game_mainpage = True
upgrades_page = False
generators_page = False

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
        # Inicial State
        if game_mainpage:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if python_click_rect.collidepoint(event.pos):
                    pycoin += pycoin_click
                
                if button_to_upgrades_rect.collidepoint(event.pos):
                    game_mainpage = False
                    upgrades_page = True
                    
                if button_to_generators_rect.collidepoint(event.pos):
                    game_mainpage = False
                    generators_page = True
        
        # Upgrade state
        if upgrades_page:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_rect.collidepoint(event.pos):
                    upgrades_page = False
                    game_mainpage = True
        
        # Generators state
        if generators_page:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_rect.collidepoint(event.pos):
                    generators_page = False
                    game_mainpage = True
                    
    # PyCoins display
    show_coins = font.render(f"{pycoin} PyCoins", False, secundary_color)
    show_coins = pygame.transform.scale_by(show_coins, (2))
    show_coins_rect = show_coins.get_rect(center = (window_width/2 - 100, python_click_rect.bottom + 50))
    
    if game_mainpage:
        screen.fill(main_color)
        screen.blit(python_click, python_click_rect)
        screen.blit(show_coins, show_coins_rect)
        screen.blit(gametitle, gametitle_rect)
        screen.blit(button_to_upgrades, button_to_upgrades_rect)
        screen.blit(button_to_generators, button_to_generators_rect)
        screen.blit(text_upgrade, text_upgrade_rect)
        screen.blit(text_generators, text_generators_rect)
    
    if upgrades_page:
        screen.fill(main_color)
        screen.blit(return_to, return_rect)
        screen.blit(text_return, text_return_rect)
        screen.blit(pyclick_uptade, pyclick_uptade_rect)
        screen.blit(button_to_pyclick_update, button_to_pyclick_update_rect)
        
    if generators_page:
        screen.fill(main_color)
        screen.blit(return_to, return_rect)
        screen.blit(text_return, text_return_rect)
        
    pygame.display.update()
    clock.tick(60)