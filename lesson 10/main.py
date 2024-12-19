
import pygame
pygame.init()
screen = pygame.display.set_mode((1210, 908))
screen.fill("light blue")
pygame.display.update() 
background = pygame.image.load("background.png")
class not_recyclable (pygame.sprite.Sprite):
    def __init__ (self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("plastic_bag.png")
        self.image = pygame.transform.scale(self.image, (50,50)) 
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y  


class Bin (pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image =  pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.image, (100,150)) 
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y  
bin = Bin(605,454)
bin_group = pygame.sprite.Group()
bin_group.add(bin)        
while True :
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    bin_group.draw(screen)   
    pygame.display.update()
            
            
    
