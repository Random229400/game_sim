from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups, collided_sprite):
        super().__init__(*groups)
        self.image1 = pygame.image.load(join('assets', 'sprites', '1.png')).convert_alpha()
        self.image2 = pygame.image.load(join('assets', 'sprites', '2.png')).convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, (55, 55))
        self.image1 = pygame.transform.scale(self.image1, (55, 55))
        self.image = self.image2
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.collided_sprite = collided_sprite
    def collision(self):
        if pygame.sprite.spritecollide(self, self.collided_sprite, False, pygame.sprite.collide_mask):
            self.image = self.image1
        else:
            self.image = self.image2
    def update(self, dt):
        for sprite in self.collided_sprite:
            if pygame.mouse.get_pressed() and pygame.Rect.colliderect(self.rect, sprite.rect):
                sprite.rect.center = pygame.mouse.get_pos()
        self.collision()