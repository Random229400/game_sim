from settings import *

class WoodPile(pygame.sprite.Sprite):
    def __init__(self, groups, player):
        super().__init__(groups)
        self.groups = groups
        self.image = pygame.image.load(join('assets', 'sprites', 'wood_pile.png'))
        self.rect = self.image.get_frect(bottomleft=(WINDOW_WIDTH - 30, WINDOW_HEIGHT - 30))
        self.player = player
        self.surf = pygame.image.load(join('assets', 'items', 'wood_stud.png'))
        self.wood = None
    def update(self, dt):
        if pygame.sprite.spritecollide(self, self.player, False, pygame.sprite.collide_mask):
            if pygame.mouse.get_just_pressed()[0]:
                if not(self.wood):
                    self.wood = Wood(self.groups, player=self.player, surf=self.surf)     
                else:
                    self.wood.kill()
                    self.wood = Wood(self.groups, player=self.player, surf=self.surf)

class Wood(pygame.sprite.Sprite):
    def __init__(self, groups, player, surf):
        super().__init__(*groups)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_frect(center=(randint(150, 175), randint(150, 175)))
        self.player = player
    # def update(self, dt):
    #     if pygame.sprite.spritecollide(self, self.player, False, pygame.sprite.collde_mask):
    #         if pygame.mouse.get_pressed()[0]:
    #             self.rect.center