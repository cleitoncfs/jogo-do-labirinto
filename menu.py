import pygame


def mostrar_menu(config):
    """Exibe o menu principal e retorna a opção selecionada."""
    tela = pygame.display.set_mode((config.largura_tela, config.altura_tela))

    opcoes = ["Jogar", "Sair"]
    selecionada = 0

    clock = pygame.time.Clock()

    while True:
        tela.fill(config.cor_fundo)

        # Título
        titulo = config.fonte_titulo.render(
            "Jogo do Labirinto", True, config.cor_texto_titulo)
        tela.blit(titulo, (config.largura_tela //
                  2 - titulo.get_width() // 2, 100))

        # Opções do menu
        for i, texto in enumerate(opcoes):
            cor = config.cor_texto_selecionado if i == selecionada else config.cor_texto_normal
            opcao = config.fonte_opcoes.render(texto, True, cor)
            tela.blit(opcao, (config.largura_tela // 2 -
                      opcao.get_width() // 2, 250 + i * 60))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return "sair"
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    selecionada = (selecionada - 1) % len(opcoes)
                elif evento.key == pygame.K_DOWN:
                    selecionada = (selecionada + 1) % len(opcoes)
                elif evento.key == pygame.K_RETURN:
                    if opcoes[selecionada] == "Jogar":
                        return "jogar"
                    elif opcoes[selecionada] == "Sair":
                        return "sair"

        clock.tick(30)
