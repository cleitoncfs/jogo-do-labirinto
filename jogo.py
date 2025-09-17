import pygame
from fases import GerenciadorFases
from vitoria import mostrar_vitoria


class Jogador:
    """Representa o jogador e seu movimento."""

    def __init__(self, rect_inicial, velocidade):
        self.rect = rect_inicial.copy()
        self.velocidade = velocidade
        self.pos_anterior = self.rect.copy()

    def mover(self, direcao):
        """Move o jogador na direção especificada."""
        self.pos_anterior = self.rect.copy()

        if direcao == "esquerda":
            self.rect.x -= self.velocidade
        elif direcao == "direita":
            self.rect.x += self.velocidade
        elif direcao == "cima":
            self.rect.y -= self.velocidade
        elif direcao == "baixo":
            self.rect.y += self.velocidade

    def reverter_movimento(self):
        """Reverte o movimento em caso de colisão."""
        self.rect = self.pos_anterior.copy()


def executar_jogo(config):
    """Executa o loop principal do jogo."""
    tela = pygame.display.set_mode((config.largura_tela, config.altura_tela))
    clock = pygame.time.Clock()
    gerenciador_fases = GerenciadorFases()

    executando = True
    while executando and gerenciador_fases.fase_atual < gerenciador_fases.total_fases:
        fase = gerenciador_fases.obter_fase_atual()
        if fase is None:
            break

        jogador = Jogador(fase["inicio"], config.velocidade_jogador)
        saida = fase["saida"]
        paredes = fase["paredes"]

        fase_concluida = False
        while not fase_concluida and executando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return True  # Volta ao menu

            # Movimento do jogador - nova lógica para detectar direções pressionadas
            teclas = pygame.key.get_pressed()
            movimentos = []

            if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
                movimentos.append("esquerda")
            if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
                movimentos.append("direita")
            if teclas[pygame.K_UP] or teclas[pygame.K_w]:
                movimentos.append("cima")
            if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
                movimentos.append("baixo")

            # Aplica os movimentos um de cada vez e verifica colisões
            for movimento in movimentos:
                jogador.mover(movimento)

                # Verificação de colisão com paredes
                colidiu = False
                for parede in paredes:
                    if jogador.rect.colliderect(parede):
                        colidiu = True
                        break

                # Se colidiu, reverte apenas este movimento específico
                if colidiu:
                    jogador.reverter_movimento()

            # Verifica se chegou à saída
            if jogador.rect.colliderect(saida):
                fase_concluida = True
                if not gerenciador_fases.avancar_fase():
                    if mostrar_vitoria(config) == "jogar":
                        gerenciador_fases.reiniciar()
                        return True
                    else:
                        return False

            # Renderização
            tela.fill(config.cor_fundo)

            # Desenha saída
            pygame.draw.rect(tela, config.cor_saida, saida)

            # Desenha paredes
            for parede in paredes:
                pygame.draw.rect(tela, config.cor_parede, parede)

            # Desenha jogador (por último para ficar sobre as outras coisas)
            pygame.draw.rect(tela, config.cor_jogador, jogador.rect)

            # Exibe o nome da fase e número
            texto_fase = config.fonte_opcoes.render(
                f"{fase['nome']} ({gerenciador_fases.fase_atual + 1}/{gerenciador_fases.total_fases})",
                True, config.cor_texto_normal
            )
            tela.blit(texto_fase, (10, 10))

            pygame.display.flip()
            clock.tick(config.fps)

    return True
