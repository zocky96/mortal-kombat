import pygame
class Enemy:
    def __init__(self,x,y,list_player,selected,list_name):
        self.scorpion = pygame.image.load('images/players/Scorpion.png')
        self.list_name = {'scorpion':pygame.transform.scale(list_name.subsurface(1,30,47,11),(100,25))}
        self.selected = selected
        self.index = 0
        self.stat = 'stand-up'
        self.list_player = {'scorpion': pygame.transform.scale(list_player.subsurface(238, 4, 32, 57), (80, 80)),}
        self.scorpion_stand_up = [pygame.transform.flip(pygame.transform.scale(self.scorpion.subsurface(9, 11, 30, 60), (80, 200)),True,False),
                                  pygame.transform.flip(pygame.transform.scale(self.scorpion.subsurface(52, 11, 30, 60), (80, 200)),True,False),
                                  pygame.transform.flip(pygame.transform.scale(self.scorpion.subsurface(86, 11, 30, 60), (80, 200)),True,False),
                                  pygame.transform.flip(pygame.transform.scale(self.scorpion.subsurface(120, 11, 30, 60), (80, 200)),True,False),
                                  pygame.transform.flip(pygame.transform.scale(self.scorpion.subsurface(154, 11, 30, 60), (80, 200)),True,False),
                                  pygame.transform.flip(pygame.transform.scale(self.scorpion.subsurface(187, 11, 30, 60), (80, 200)),True,False),
                                  pygame.transform.flip(pygame.transform.scale(self.scorpion.subsurface(219, 11, 30, 60), (80, 200)),True,False),
                                  pygame.transform.flip(pygame.transform.scale(self.scorpion.subsurface(254, 11, 30, 60), (80, 200)),True,False),
                                  ]
        self.scorpion_walk_right = [
            pygame.transform.scale(self.scorpion.subsurface(9, 87, 30, 60), (80, 200)),
            pygame.transform.scale(self.scorpion.subsurface(41, 87, 30, 60), (80, 200)),
            pygame.transform.scale(self.scorpion.subsurface(65, 87, 30, 60), (80, 200)),
            pygame.transform.scale(self.scorpion.subsurface(92, 87, 30, 60), (80, 200)),
            pygame.transform.scale(self.scorpion.subsurface(115, 87, 30, 60), (80, 200)),
            pygame.transform.scale(self.scorpion.subsurface(144, 87, 30, 60), (80, 200)),
            pygame.transform.scale(self.scorpion.subsurface(171, 87, 30, 60), (80, 200)),
            pygame.transform.scale(self.scorpion.subsurface(197, 87, 30, 60), (80, 200)),
            pygame.transform.scale(self.scorpion.subsurface(223, 87, 30, 60), (80, 200)),
        ]
        self.scorpion_stats = {'stand-up':self.scorpion_stand_up}
        self.rect = pygame.Rect(x, y, 50, 60)
        self.life = 342

    def gravity(self):
        self.rect.y += 10
    def drawEnemy(self,screen):
        if self.index >= len(self.scorpion_stats[self.stat]):
            self.index = 0
        #pygame.draw.rect(screen,(240,30,0),self.rect,0)
        screen.blit(self.scorpion_stats[self.stat][self.index], (self.rect.x, self.rect.y))
        self.index += 1
        pygame.draw.rect(screen, (255, 0, 0), (648,39,350,22), 1)
        pygame.draw.rect(screen, (255, 100, 0), (652, 42.7, self.life, 15), 0)
        screen.blit(self.list_player[self.selected], (1005, 5))
        screen.blit(self.list_name[self.selected], (900, 3))
