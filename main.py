import pygame
from actor import Actor

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.temp_actor = Actor((640, 360), "")
        
    def run(self):
        while True:
            self.screen.fill((74, 74, 74))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            self.temp_actor.draw(self.screen)
            
            pygame.display.update()
            
if __name__ == "__main__":
    Game().run()