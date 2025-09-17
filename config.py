import pygame


class Configuracoes:
    """Armazena todas as configurações do jogo."""

    def __init__(self):
        # Dimensões da tela
        self.largura_tela = 600
        self.altura_tela = 600

        # Cores
        self.cor_fundo = (30, 30, 30)
        self.cor_jogador = (0, 255, 0)
        self.cor_saida = (255, 0, 0)
        self.cor_parede = (200, 200, 200)
        self.cor_texto_titulo = (255, 255, 0)
        self.cor_texto_normal = (255, 255, 255)
        self.cor_texto_selecionado = (0, 255, 0)

        # Velocidades
        self.velocidade_jogador = 5
        self.fps = 60

        # Fontes
        self.fonte_titulo = pygame.font.SysFont("Arial", 70, bold=True)
        self.fonte_opcoes = pygame.font.SysFont("Arial", 40)
        self.fonte_mensagem = pygame.font.SysFont("Arial", 60, bold=True)
