import pygame


class GerenciadorFases:
    """Gerencia as fases do jogo."""

    def __init__(self):
        self.fases = self._criar_fases()
        self.fase_atual = 0
        self.total_fases = len(self.fases)

    def _criar_fases(self):
        """Cria e retorna todas as fases do jogo."""
        return [
            {
                "nome": "Fase 1 - Introdução",
                "inicio": pygame.Rect(50, 50, 40, 40),
                "saida": pygame.Rect(550, 550, 40, 40),
                "paredes": [
                    pygame.Rect(100, 0, 20, 500),
                    pygame.Rect(200, 100, 300, 20),
                    pygame.Rect(0, 300, 400, 20),
                ]
            },
            {
                "nome": "Fase 2 - Caminhos Cruzados",
                "inicio": pygame.Rect(50, 550, 40, 40),
                "saida": pygame.Rect(550, 50, 40, 40),
                "paredes": [
                    pygame.Rect(50, 100, 500, 20),
                    pygame.Rect(300, 150, 20, 400),
                    pygame.Rect(100, 400, 400, 20),
                ]
            },
            {
                "nome": "Fase 3 - Corredores",
                "inicio": pygame.Rect(50, 50, 40, 40),
                "saida": pygame.Rect(550, 550, 40, 40),
                "paredes": [
                    pygame.Rect(150, 0, 20, 600),
                    pygame.Rect(300, 0, 20, 600),
                    pygame.Rect(450, 0, 20, 600),
                ]
            },
            {
                "nome": "Fase 4 - Travessia Central",
                "inicio": pygame.Rect(50, 300, 40, 40),
                "saida": pygame.Rect(550, 300, 40, 40),
                "paredes": [
                    pygame.Rect(100, 100, 400, 20),
                    pygame.Rect(100, 480, 400, 20),
                    pygame.Rect(300, 120, 20, 360),
                ]
            },
            {
                "nome": "Fase 5 - Barreiras Horizontais",
                "inicio": pygame.Rect(50, 50, 40, 40),
                "saida": pygame.Rect(550, 550, 40, 40),
                "paredes": [
                    pygame.Rect(100, 100, 400, 20),
                    pygame.Rect(100, 200, 400, 20),
                    pygame.Rect(100, 300, 400, 20),
                    pygame.Rect(100, 400, 400, 20),
                ]
            },
            {
                "nome": "Fase 6 - Três Portas",
                "inicio": pygame.Rect(300, 50, 40, 40),
                "saida": pygame.Rect(300, 550, 40, 40),
                "paredes": [
                    pygame.Rect(0, 150, 600, 20),
                    pygame.Rect(0, 300, 600, 20),
                    pygame.Rect(0, 450, 600, 20),
                ]
            },
            {
                "nome": "Fase 7 - Colunas",
                "inicio": pygame.Rect(50, 550, 40, 40),
                "saida": pygame.Rect(550, 50, 40, 40),
                "paredes": [
                    pygame.Rect(100, 100, 20, 400),
                    pygame.Rect(200, 100, 20, 400),
                    pygame.Rect(300, 100, 20, 400),
                    pygame.Rect(400, 100, 20, 400),
                ]
            },
            {
                "nome": "Fase 8 - Caixa Central",
                "inicio": pygame.Rect(50, 50, 40, 40),
                "saida": pygame.Rect(550, 550, 40, 40),
                "paredes": [
                    pygame.Rect(150, 150, 300, 20),
                    pygame.Rect(150, 150, 20, 300),
                    pygame.Rect(150, 450, 300, 20),
                    pygame.Rect(430, 150, 20, 300),
                ]
            },
            {
                "nome": "Fase 9 - Floresta de Pilares",
                "inicio": pygame.Rect(50, 300, 40, 40),
                "saida": pygame.Rect(550, 300, 40, 40),
                "paredes": [
                    pygame.Rect(100, 0, 20, 600),
                    pygame.Rect(200, 0, 20, 600),
                    pygame.Rect(300, 0, 20, 600),
                    pygame.Rect(400, 0, 20, 600),
                ]
            },
            {
                "nome": "Fase 10 - Labirinto Final",
                "inicio": pygame.Rect(300, 300, 40, 40),
                "saida": pygame.Rect(550, 550, 40, 40),
                "paredes": [
                    pygame.Rect(100, 100, 400, 20),
                    pygame.Rect(100, 200, 400, 20),
                    pygame.Rect(100, 300, 400, 20),
                    pygame.Rect(100, 400, 400, 20),
                    pygame.Rect(100, 500, 400, 20),
                ]
            }
        ]

    def obter_fase_atual(self):
        """Retorna os dados da fase atual."""
        if self.fase_atual < self.total_fases:
            return self.fases[self.fase_atual]
        return None

    def avancar_fase(self):
        """Avança para a próxima fase."""
        self.fase_atual += 1
        return self.fase_atual < self.total_fases

    def reiniciar(self):
        """Reinicia o jogo da primeira fase."""
        self.fase_atual = 0
