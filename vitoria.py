import pygame


def mostrar_vitoria(config):
    """Exibe a tela de vitória."""
    tela = pygame.display.set_mode((config.largura_tela, config.altura_tela))

    texto = config.fonte_mensagem.render(
        "Você venceu!", True, config.cor_texto_selecionado)
    texto_rect = texto.get_rect(
        center=(config.largura_tela // 2, config.altura_tela // 2 - 50))

    opcao1 = config.fonte_opcoes.render(
        "Pressione ENTER para jogar novamente", True, config.cor_texto_normal)
    opcao2 = config.fonte_opcoes.render(
        "Pressione ESC para sair", True, config.cor_texto_normal)

    clock = pygame.time.Clock()
    tempo = 0

    # Tentar carregar som de vitória
    try:
        pygame.mixer.init()
        som = pygame.mixer.Sound("assets/vitoria.wav")
        som.play()
    except:
        pass

    esperando = True
    while esperando:
        tela.fill(config.cor_fundo)

        # Texto piscante
        tempo += 1
        if tempo % 60 < 40:  # Texto visível 2/3 do tempo
            tela.blit(texto, texto_rect)

        tela.blit(opcao1, (config.largura_tela // 2 -
                  opcao1.get_width() // 2, config.altura_tela // 2 + 30))
        tela.blit(opcao2, (config.largura_tela // 2 -
                  opcao2.get_width() // 2, config.altura_tela // 2 + 70))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "sair"
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return "jogar"
                elif evento.key == pygame.K_ESCAPE:
                    return "sair"

        clock.tick(30)
