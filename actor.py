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

    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
        screen.blit(
            self.name_text,
            (
                self.image_rect.x - self.name_text.get_width() / 4,
                self.image_rect.y + self.image_rect.height + 5,
            ),
        )
