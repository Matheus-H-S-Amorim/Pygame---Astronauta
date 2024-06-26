from os import *
import numpy as np
import random
import pygame

# ATALHOS para Pastas com Figuras e Sons 
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
ANIMACAO_ASTRONA = "animacao_astrona"
BACKGROUND_IMG = 'fundo_jogo'
TELADEINICIO = 'tela_inicial'
TELAFINAL = 'tela_final'
SOM_FUNDO = 'som_de_fundo'
FUNDO_F2 = 'fundo_F2'
FUNDO_F3 = 'fundo_F3'
FUNDO_F4 = 'fundo_F4'
SOM_STAR = 'som_star'
SOM_METEORO = 'som_meteoro'
SOM_GAME_OVER = 'som_game_over'


def load_assets():
    assets = {} # Cria dicionário

    #assets[BACKGROUND_IMG] = pygame.image.load(path.join(IMG_DIR, 'fundo\\fundo_planeta_vermelho.png')).convert()
    assets[TELADEINICIO] = pygame.image.load(path.join(IMG_DIR, 'tela_inicial.png')).convert()
    assets[TELAFINAL] = pygame.image.load(path.join(IMG_DIR, 'tela_final.png')).convert()
    assets[SOM_FUNDO] = pygame.mixer.Sound(path.join(SND_DIR, 'fundo_som_neon.mp3'))
    assets[FUNDO_F2] = pygame.image.load(path.join(IMG_DIR, 'fundo\\saturno_fundo.png')).convert()
    assets[FUNDO_F4] = pygame.image.load(path.join(IMG_DIR, 'fundo_dinos_no_ceu.jpg')).convert()
    assets[FUNDO_F3] = pygame.image.load(path.join(IMG_DIR, 'planeta_roxo.png')).convert()

    assets[SOM_STAR] = pygame.mixer.Sound(path.join(SND_DIR, 'som_sino.mp3')) 
    assets[SOM_GAME_OVER] = pygame.mixer.Sound(path.join(SND_DIR, 'gameover_som.mp3'))
    assets[SOM_METEORO] = pygame.mixer.Sound(path.join(SND_DIR, 'meteoro_som.mp3'))



    animacao_astrona = []
    for i in range(8):
        # Os arquivos de animação são numerados de 00 a 40
        filename = path.join(IMG_DIR, 'astronauta_anda','tile{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (100, 100))
        animacao_astrona.append(img)

    assets[ANIMACAO_ASTRONA] = animacao_astrona
    return assets


### COLOCAR SOM 
#assets[SOM_FUNDO] = pygame.mixer.music.load(os.path.join(SND_DIR, 'som_suspense.mp3')) #pygame.mixer.Sound(os.path.join(SND_DIR, 'sound_suspense_galatic.mp3'))
#pygame.mixer.music.set_volume(0.4)