from settings import *

class T_Pins(pygame.sprite.Sprite):
    def __init__(self, *groups, collided_sprite):
        super().__init__(*groups)
        self.groups = groups
        self.image = pygame.image.load(join('assets', 'sprites', 'pins.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_frect(topleft=(20, 20))
        self.player = collided_sprite
        self.surf = pygame.image.load(join('assets', 'items', 'pin.png'))
        self.pin = None
    def update(self, dt):
        if pygame.sprite.spritecollide(self, self.player, False, pygame.sprite.collide_mask):
            if pygame.mouse.get_just_pressed()[0]:
                if not(self.pin):        
                    self.pin = T_Pin(self.groups, surf=self.surf, player=self.player)
                else:
                    self.pin.kill()
                    self.pin = T_Pin(self.groups, surf=self.surf, player=self.player)
            
        
class T_Pin(pygame.sprite.Sprite):
    def __init__(self, *groups, surf, player):
        super().__init__(*groups)
        self.image = surf
        rotate_amt = randint(0, 360)
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.image = pygame.transform.rotozoom(self.image, rotate_amt, 1)
        self.rect = self.image.get_frect(center=(randint(150, 175), randint(150, 175)))
        self.player = player
    # def update(self, dt):
    #     if pygame.sprite.spritecollide(self, self.player, False, pygame.sprite.collide_mask):
    #         if pygame.mouse.get_pressed()[0]:
    #             pos = pygame.mouse.get_pos()
    #             self.rect.center = pos