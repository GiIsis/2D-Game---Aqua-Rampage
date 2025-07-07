#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from pygame.locals import KEYDOWN, K_RETURN, K_ESCAPE

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_YELLOW, C_WHITE


class GameOver:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/GameOver.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(self.surf, self.rect)
            self.draw_text("GAME OVER", 64, C_YELLOW, (WIN_WIDTH // 2, WIN_HEIGHT // 3))
            self.draw_text("Press Enter to restart or Esc to quit", 24, C_WHITE, (WIN_WIDTH // 2, WIN_HEIGHT // 2))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        return "restart"
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    def draw_text(self, text: str, size: int, color: tuple, center_pos: tuple):
        font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        surf = font.render(text, True, color).convert_alpha()
        rect = surf.get_rect(center=center_pos)
        self.window.blit(surf, rect)
