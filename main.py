import pygame

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
            
if __name__ == "__main__":
    Game().run()