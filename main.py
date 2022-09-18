import random
from ground import Ground
from player import Player
from  enemy import Enemy
import pygame
import os
class MortalKombat:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        width = 1100
        height = 600
        self.fps = pygame.time.Clock()
        self.velocity = 0
        self.velocity_y = 0
        self.sol = Ground()
        x = 50
        y= 392
        self.list_player = pygame.image.load('images/players/faces.png')
        self.selected = 'lui kang'
        self.list_name = pygame.image.load("images/bg/names.png")
        self.player = Player(x,y,self.list_player,self.selected,self.list_name)
        enemy_x = 900
        enemy_y = 392
        self.selected_enemy = 'scorpion'
        self.enemy = Enemy(enemy_x,enemy_y,self.list_player,self.selected_enemy,self.list_name)
        self.bg_list = [
                        pygame.image.load("images/bg/bg1.png"),
                        pygame.image.load("images/bg/bg2.png"),
                        pygame.image.load("images/bg/bg3.png"),
                        pygame.image.load("images/bg/bg4.png"),
                        pygame.image.load("images/bg/bg5.png"),
                        pygame.image.load("images/bg/bg6.png")
                        ]
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Mortal Kombat MXI By Zocky")
        self.choose_bg()
        self.screen_on = True
        pygame.mixer.music.load("sound\music.mp3")
        pygame.mixer.music.play(-1)
    def choose_bg(self):
        self.bg = random.choice(self.bg_list)
        self.bg = pygame.transform.scale(self.bg,(1100,600))


    def main_Loop(self):
        while self.screen_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.screen_on = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.velocity = 10
                        self.player.stat = 'walk-right'
                    if event.key == pygame.K_LEFT:
                        self.velocity = -10
                        self.player.stat = 'walk-left'
                    if event.key == pygame.K_p:
                        self.player.stat = 'kout-pye'
                    if event.key == pygame.K_UP:
                        self.velocity_y = -50
                    if event.key == pygame.K_a:
                        self.player.stat = 'kout-pwen'
                    if event.key == pygame.K_DOWN:
                        self.player.stat = 'koupi'
                        self.player.arrow_direction = 'down'
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.velocity = 0
                        self.player.stat = 'stand-up'
                    if event.key == pygame.K_LEFT:
                        self.velocity = 0
                        self.player.stat = 'stand-up'
                    if event.key == pygame.K_p:
                        self.player.stat = 'stand-up'
                    if event.key == pygame.K_a:
                        self.player.stat = 'stand-up'
                    if event.key == pygame.K_DOWN:
                        self.player.stat = 'stand-up'
                        self.player.arrow_direction = None
                    if event.key == pygame.K_UP:
                        self.velocity_y = 0
            self.screen.fill((0,0,0))
            self.screen.blit(self.bg,(0,0))
            #self.sol.drawGround(self.screen)
            self.player.showPlayer(self.screen)
            self.enemy.drawEnemy(self.screen)
            if not self.player.rect.colliderect(self.sol.rect):
                self.player.gravity()
            if not self.enemy.rect.colliderect(self.sol.rect):
                self.enemy.gravity()
            self.player.rect.x += self.velocity
            self.player.rect.y += self.velocity_y
            self.fps.tick(10)
            pygame.display.update()
if __name__ == '__main__':
    MortalKombat().main_Loop()