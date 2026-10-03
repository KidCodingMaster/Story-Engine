import pygame

class Actor:
    def __init__(self, pos: list[int, int], name: str):
        self.pos = pos
        self.name = name
        
        self.image = pygame.image.load('./assets/imgs/dflt_actor.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.image_rect = self.image.get_rect(center=pos)
        
    def draw(self, screen):
        screen.blit(self.image, self.image_rect)