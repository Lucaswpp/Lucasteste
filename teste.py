import pygame
from sys import exit
from random import randint

pygame.init()

def maca():
    x = randint(0,800)
    y = randint(0,600)

    return (x // tamanho_pixel*tamanho_pixel,y // tamanho_pixel*tamanho_pixel)

def colisao_tela(pos):
    global jogo_ativo
    if 0 <= pos[0] < tamanho_tela[0] and 0 <= pos[1] < tamanho_tela[1]:
        jogo_ativo = True
    else:
        jogo_ativo = False

tamanho_tela = (800,600)
tamanho_pixel = 10
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Jogo da cobra")
cobra_surface = pygame.Surface((tamanho_pixel,tamanho_pixel))
cobra_surface.fill((255,255,255))
cobra_pos = [(400,300),(410,300),(420,300)]
maca_surface = pygame.Surface((tamanho_pixel,tamanho_pixel))
maca_surface.fill((255,0,0))
maca_pos = maca()
clock = pygame.time.Clock()
lista_input = ["K_RIGHT","K_LEFT","K_UP","K_DOWN"]
direcao = lista_input[1]
jogo_ativo = True


while jogo_ativo:

    clock.tick(20)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit()

        if evento.type == pygame.KEYDOWN:

            if evento.key in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]:

                if evento.key == pygame.K_LEFT:
                    direcao = "K_LEFT"
                
                if evento.key == pygame.K_RIGHT:
                    direcao = "K_RIGHT"
                
                if evento.key == pygame.K_UP:
                    direcao = "K_UP"
                
                if evento.key == pygame.K_DOWN:
                    direcao = "K_DOWN"
                
    for pos in cobra_pos:

        tela.blit(cobra_surface,pos)

        tela.blit(maca_surface,maca_pos)

    for i in range(len(cobra_pos)-1,0,-1):
        cobra_pos[i] = cobra_pos[i - 1]

    colisao_tela(cobra_pos[0])

    if cobra_pos[0] == maca_pos:
        maca_pos = maca()
        cobra_pos.append((-10,-10))


    if direcao == lista_input[0]:
        cobra_pos[0] = (cobra_pos[0][0] + tamanho_pixel, cobra_pos[0][1])
    
    if direcao == lista_input[1]:
        cobra_pos[0] = (cobra_pos[0][0] - tamanho_pixel, cobra_pos[0][1])
    
    if direcao == lista_input[2]:
        cobra_pos[0] = (cobra_pos[0][0],cobra_pos[0][1] - tamanho_pixel)
    
    if direcao == lista_input[3]:
        cobra_pos[0] = (cobra_pos[0][0], cobra_pos[0][1] + tamanho_pixel)
        
    pygame.display.update()
    tela.fill((0,0,0))