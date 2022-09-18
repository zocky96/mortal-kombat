import pygame
class Player:
    def __init__(self,x,y,list_player,selected,liste_name):
        self.index = 0
        self.down_index = 0
        self.life = 342
        self.selected = selected
        self.list_name = {'lui kang':pygame.transform.scale(liste_name.subsurface(53,20,47,11),(100,25))}
        self.list_player = {'lui kang':pygame.transform.scale(list_player.subsurface(201,4,32,57),(80,80))}
        self.life_rect = pygame.Rect(90,39,350,22)
        self.stat = 'stand-up'
        self.arrow_direction = None
        self.lui_kang = pygame.image.load('images/players/Liu Kang.png')
        self.lui_kang_kut_pye = [
                                 pygame.transform.scale(self.lui_kang.subsurface(9,296,30,60),(80,200)),
                                 pygame.transform.scale(self.lui_kang.subsurface(38,296,30,60),(80,200)),
                                 pygame.transform.scale(self.lui_kang.subsurface(69,296,30,60),(80,200)),
                                 pygame.transform.scale(self.lui_kang.subsurface(98,296,30,60),(80,200)),
                                 pygame.transform.scale(self.lui_kang.subsurface(133,296,39,60),(80,200)),
                                 ]
        self.lui_kang_kout_pwen = [pygame.transform.scale(self.lui_kang.subsurface(148,229,35,60),(80,200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(185,229,35,60),(80,200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(224,229,45,60),(80,200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(276,229,30,60),(80,200)),]
        self.lui_kang_walk_right = [
                               pygame.transform.scale(self.lui_kang.subsurface(9,87,30,60),(80,200)),
                               pygame.transform.scale(self.lui_kang.subsurface(41, 87, 30, 60), (80, 200)),
                               pygame.transform.scale(self.lui_kang.subsurface(65, 87, 30, 60), (80, 200)),
                               pygame.transform.scale(self.lui_kang.subsurface(92, 87, 30, 60), (80, 200)),
                               pygame.transform.scale(self.lui_kang.subsurface(115, 87, 30, 60), (80, 200)),
                               pygame.transform.scale(self.lui_kang.subsurface(144, 87, 30, 60), (80, 200)),
                               pygame.transform.scale(self.lui_kang.subsurface(171, 87, 30, 60), (80, 200)),
                               pygame.transform.scale(self.lui_kang.subsurface(197, 87, 30, 60), (80, 200)),
                               pygame.transform.scale(self.lui_kang.subsurface(223, 87, 30, 60), (80, 200)),
                             ]
        self.lui_kang_walk_left = self.lui_kang_walk_right[::-1]
        self.lui_kang_walk_koupi = [pygame.transform.scale(self.lui_kang.subsurface(579,16,33,54),(80,200)),
                                    pygame.transform.scale(self.lui_kang.subsurface(618,16,33,54),(80,200)),
                                    pygame.transform.scale(self.lui_kang.subsurface(651,16,33,54),(80,200)),]
        self.lui_kang_stand_up = [
                                   pygame.transform.scale(self.lui_kang.subsurface(8,11,33,60),(80,200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(49, 11, 33, 60), (80, 200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(87, 11, 33, 60), (80, 200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(119, 11, 33, 60), (80, 200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(153, 11, 33, 60), (80, 200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(188, 11, 33, 60), (80, 200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(221, 11, 33, 60), (80, 200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(255, 11, 33, 60), (80, 200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(289, 11, 33, 60), (80, 200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(333, 11, 33, 60), (80, 200)),
                                   pygame.transform.scale(self.lui_kang.subsurface(8, 11, 33, 60), (80, 200)),
                                 ]
        self.lui_kang_stats ={'stand-up':self.lui_kang_stand_up,
                              'walk-right':self.lui_kang_walk_right,
                              'walk-left':self.lui_kang_walk_left,
                              'kout-pye':self.lui_kang_kut_pye,
                              'koupi':self.lui_kang_walk_koupi,
                              'kout-pwen':self.lui_kang_kout_pwen}
        self.rect = pygame.Rect(x,y,50,50)
    def gravity(self):
        self.rect.y += 2
    def showPlayer(self,screen):
        if self.index >= len(self.lui_kang_stats[self.stat]):
            self.index = 0
        if self.arrow_direction == 'down':
            self.down_index +=1
            if self.down_index > 2:
                self.index = len(self.lui_kang_stats[self.stat]) - 1
        else:
            self.down_index = 0
        screen.blit(self.lui_kang_stats[self.stat][self.index],(self.rect.x,self.rect.y))
        self.index +=1
        screen.blit(self.list_player[self.selected],(5,5))
        pygame.draw.rect(screen,(255,0,0),self.life_rect,1)
        pygame.draw.rect(screen, (255, 100, 0), (94,42.7,self.life,15), 0)
        ob= pygame.font.SysFont("arial",20,True)
        a= ob.render('Zocky',True,(255,0,0))
        #screen.blit(a, (90, 3))
        screen.blit(self.list_name[self.selected],(90,3))
