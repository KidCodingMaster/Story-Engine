import pygame
import time
from actor import Actor
from story_director import StoryDirector

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.temp_actor = Actor((640, 360), "Bob")

        self.actors = [self.temp_actor]

        self.story_director = StoryDirector()

        self.story_director.add_script("teleport", self.temp_actor, (500, 300))
        self.story_director.add_script('wait', None, None, 1)

        self.start_time = time.time()
        self.end_time = self.start_time + 1

    def run(self):
        while True:
            self.screen.fill((74, 74, 74))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.reset()

            self.temp_actor.draw(self.screen)

            if time.time() >= self.end_time:
                self.story_director.play()

                self.end_time = self.end_time + 1

            pygame.display.update()

    def reset(self):
        for actor in self.actors:
            actor.image_rect.center = actor.pos


if __name__ == "__main__":
    Game().run()
