#importando coisas
import pygame
from os import path
from Candidatos import Candidatos
from configuracoes import *
import time
player = ''
def menu_screen(screen,WIDTH, HEIGHT):
    #unidade de tempo
    clock=pygame.time.Clock()
    clock.tick(FPS)
    tempo=0
    #tempo que vai ficar nessa mesma tela
    
    while tempo<60:
        tempo+=1
        #carregar o fundo da tela de menu
        fundo1=pygame.image.load(path.join(IMG_DIR, 'Warning.png')).convert()
        fundo2 = pygame.image.load(path.join(IMG_DIR, 'Imagemdefundo.png')).convert()
        fundo1_small = pygame.transform.scale(fundo1, (WIDTH, HEIGHT))
        fundo2_small = pygame.transform.scale(fundo2, (WIDTH, HEIGHT))
        tela_fundo1_rect = fundo1.get_rect()
        tela_fundo2_rect = fundo2.get_rect()

        
        #primeira tela de aviso
        screen.fill((0,0,0))
        screen.blit(fundo1_small,(0,0))
        pygame.display.update()

    

    




    #segunda tela de escolha personagens
    continuar = True
    while continuar:
        clock.tick(60)
        screen.fill((0,0,0))
        screen.blit(fundo2_small,(0,0))

        pygame.display.update()
    	#esse evento delimitará qual personagem que vai ser esocolhido
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player=ENCERRAR
                continuar = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    player = 'Ciro'
                    continuar = False
                if event.key == pygame.K_l:
                    player = 'Lula'
                    continuar = False
                if event.key == pygame.K_m:
                    player = 'Moro'
                    continuar = False
                if event.key == pygame.K_b:
                    player = 'Bolsonaro'
                    continuar = False
                if event.key == pygame.K_d:
                    player = 'Doria'
                    continuar = False
    #retorna o luta para mudar de tela e o nome do personagem    
    return LUTA, player
        

                    

            
        
        
            

    
#players



class escolha(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = 0

