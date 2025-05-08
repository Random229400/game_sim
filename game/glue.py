from settings import *

class Glue(pygame.sprite.Sprite):
    def __init__(self, *groups, collided_sprite):
        super().__init__(*groups)
        self.image = pygame.image.load(join('assets', 'sprites', 'elmers_glue.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.image = pygame.transform.rotozoom(self.image, -45, 1)
        self.rect = self.image.get_frect(topright=(WINDOW_WIDTH - 20, 20))
        self.player = collided_sprite
    # def update(self, dt):
    #     if pygame.sprite.spritecollide(self, self.player, False, pygame.sprite.collide_mask):
    #         if pygame.mouse.get_pressed()[0]:
    #             self.rect.center = pygame.mouse.get_pos()
        