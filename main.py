import pygame
from menu import mostrar_menu
from jogo import executar_jogo
from config import Configuracoes


class JogoLabirinto:
    """Classe principal que gerencia o jogo do labirinto."""

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Labirinto")
        self.rodando = True
        self.config = Configuracoes()

    def executar(self):
        """Loop principal do jogo."""
        while self.rodando:
            opcao_selecionada = mostrar_menu(self.config)

            if opcao_selecionada == "jogar":
                self.rodando = executar_jogo(self.config)
            elif opcao_selecionada == "sair":
                self.rodando = False

        pygame.quit()


if __name__ == "__main__":
    jogo = JogoLabirinto()
    jogo.executar()
