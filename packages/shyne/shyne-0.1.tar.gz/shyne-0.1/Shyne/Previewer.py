import sys

import pygame

from Shyne.Game import Game

small_font = pygame.font.SysFont('arial', 25)

class Previewer:
    def __init__(self, shyne, display, pos, size):
        self.main_display = display
        self.shyne = shyne
        self.pos = pos
        self.size = size

        self.show_fps = True

    def frame(self, events, mouse_pos):
        rect = pygame.Rect(self.pos, self.size)
        pygame.draw.rect(self.main_display, (255, 255, 255), rect)
        debug = False
        success = True
        ratio = self.main_display.get_width()/self.size[0]
        mouse_pos_delta = ((mouse_pos[0]-self.pos[0])*ratio,(mouse_pos[1]-self.pos[1])*ratio)
        if self.shyne.game:
            if debug:
                self.shyne.game.frame(events, mouse_pos_delta)
                self.main_display.blit(pygame.transform.scale(self.shyne.game.display, self.size), self.pos)
            else:
                try:
                    self.shyne.game.frame(events, mouse_pos_delta)
                    self.main_display.blit(pygame.transform.scale(self.shyne.game.display, self.size), self.pos)
                except :
                    success = False
            if self.show_fps:
                fps = small_font.render(str(self.shyne.game.fps), True, (0, 0, 255) if success else (255, 0, 0))
                self.main_display.blit(fps, (
                self.pos[0] + self.size[0] - fps.get_width(), self.pos[1] + self.size[1] - fps.get_height()))
