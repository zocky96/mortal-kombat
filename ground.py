import pygame
class Ground:
    def __init__(self):
        self.rect = pygame.Rect(0,440,1100,40)
    def drawGround(self,screen):
        pygame.draw.rect(screen,(255,0,0),self.rect,0)