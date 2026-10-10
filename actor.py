import pygame


class Actor:
    def __init__(self, pos: list[int, int], name: str):
        self.pos = pos
        self.name = name

        self.image = pygame.image.load("./assets/imgs/dflt_actor.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.image_rect = self.image.get_rect(center=pos)

        self.font = pygame.font.Font("./assets/fonts/slkscr.ttf", 24)

        self.name_text = self.font.render(self.name, False, (255, 255, 255))
        
        self.dest = None
        
        self.moving = False

    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
        screen.blit(
            self.name_text,
            (
                self.image_rect.centerx - self.name_text.get_width() / 2,
                self.image_rect.y + self.image_rect.height + 5,
            ),
        )
        
    def teleport(self, cords):
        self.image_rect.center = cords
        
    def move(self, cords, time):
        self.moving = True
        
        self.dest = cords
        
        self.image_rect.x += (cords[0] - self.image_rect.x) / time
        self.image_rect.y += (cords[1] - self.image_rect.y) / time
        
        distance_x = abs(cords[0] - self.image_rect.x)
        distance_y = abs(cords[1] - self.image_rect.y)
        
        if distance_x < 2 and distance_y < 2:
            self.dest = None
            self.image_rect.center = cords
            
            self.moving = False
            
            return True
        
        return False
