from settings import *
from player import Player
from t_pin import *
from glue import *
from wood import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Structures")
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
        self.t_pins = T_Pins((self.all_sprites, self.collision_sprites), collided_sprite=self.player_sprite)
        self.glue = Glue((self.all_sprites, self.collision_sprites), collided_sprite=self.player_sprite)
        self.wood = WoodPile((self.all_sprites, self.collision_sprites), player=self.player_sprite)
        self.player = Player((self.all_sprites, self.player_sprite), collided_sprite=self.collision_sprites)
        self.background = pygame.image.load(join('assets', 'wood_background.jpg')).convert()
        self.background = pygame.transform.smoothscale_by(self.background, 3.35)
    
    def run(self):
        dt = self.clock.tick()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.all_sprites.update(dt)
            self.screen.fill('black')
            self.screen.blit(self.background)
            self.all_sprites.draw(self.screen)
            pygame.display.update()
        pygame.quit()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()

