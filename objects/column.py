import pygame.sprite

import assets
import configs


class Column(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.sprite = assets.get_sprite("pipe-green")
        self.sprite_rect = self.sprite.get_rect()

        self.image = pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=(0, 0))

        super().__init__(*groups)

    # def update(self):
    #     self.rect.x -= 1

youtube 15:20