import pygame
import  random
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("ressourceG/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 5)
        self.rect.x = random.randint(1,700)
        # self.rect.y = random.randint(1, 700)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 600:
            print ("sol")
            #retirer la comete
            self.remove()

        #verifier si la comete touche le joueur
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
        ):
            print('joueur touché !')
            # retirer la comete
            self.remove()
            # subir degats
            self.comet_event.game.player.damage(20)
