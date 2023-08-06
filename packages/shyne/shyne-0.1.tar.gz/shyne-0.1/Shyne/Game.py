import copy

import numpy as np
import pygame

from pyNDL import ThreadedProcess
from pyNDL.NodePrefabs import EventStart

small_font = pygame.font.SysFont('arial', 25)


class Game:
    instance = None

    def __init__(self, display, shyne_data, show_fps=False):
        Game.instance = self

        self.display = display
        self.shyne_data = shyne_data

        self.frame_events = []
        self.on_key_press_events = []
        from Shyne.Prefabs import OnFrameEvent
        from Shyne.Prefabs import OnKeyPressEvent

        for sprite in self.shyne_data.sprites:
            for node in sprite.pyNDL.get_main_data().nodes:
                if type(node) is OnFrameEvent:
                    self.frame_events.append(node)
                    sprite.on_frame = node
                if type(node) is OnKeyPressEvent:
                    self.on_key_press_events.append(node)
                    sprite.on_keyboard_event = node

        self.threads = []
        self.started = False

        self.show_fps = show_fps
        self._show_fps = self.show_fps
        self.fps = 0

        self.delta_time = 0
        self.clock = pygame.time.Clock()

        self.mouse_pos = (0, 0)

        self.first_frame = True

        self.screen_center = np.array((self.display.get_width() / 2, self.display.get_height() / 2))

        self.tags = {}

    def frame(self, events, pos):
        self.delta_time = self.clock.tick() / 1000
        self.fps = int(self.clock.get_fps())
        self.display.fill((255, 255, 255))
        if self.started:
            self.mouse_pos = np.array(pos)
            for sprite in self.shyne_data.sprites:
                sprite.display.fill([0, 0, 0, 0])
            for event in events:
                if event.type == pygame.KEYDOWN:
                    for on_key_press_event in self.on_key_press_events:
                        on_key_press_event.execute()
            for frame_event in self.frame_events:
                frame_event.execute()
            for sprite in self.shyne_data.sprites:
                if sprite.draw_func:
                    sprite.draw_func.execute()
                sprite_display, rect = self.rot_center(sprite.display, sprite.rotation.value, sprite.position.value[0],
                                                       sprite.position.value[1])
                self.display.blit(sprite_display, rect)
                if self.first_frame or sprite.calculate_collisions:
                    sprite.mask = pygame.mask.from_surface(sprite_display)
                    sprite.rect = rect
                    sprite.calculate_collisions = False
                sprite.rect.topleft = sprite.position.value
            if self.show_fps:
                fps = small_font.render(str(self.fps), True, (0, 0, 255))
                self.display.blit(fps, (10, 10))
            self.first_frame = False

    def start(self):
        pygame.mixer.pause()
        self.tags = {}
        for sprite in self.shyne_data.sprites:
            for variable in sprite.pyNDL.data.variables:
                if variable.name == "Position":
                    variable.value = self.screen_center
                    sprite.position = variable
                elif variable.name == "Rotation":
                    variable.value = 0
                    sprite.rotation = variable
                else:
                    variable.value = 0
            for function in sprite.pyNDL.data.functions:
                if function.name == "Draw":
                    sprite.draw_func = function

            event_start_nodes = []
            nodes = sprite.pyNDL.get_main_data().nodes

            for i, node in enumerate(nodes):
                if type(node) is EventStart:
                    event_start_nodes.append(node)
                    node.pyNDL.parent.on_start = node
                    t = ThreadedProcess.ThreadedProcess(f"Thread {i}", node.execute)
                    t.start()
                    self.threads.append(t)

        self.started = True
        self.first_frame = True

    def stop(self):
        for t in self.threads:
            t.raise_exception()
            t.join()
        self.threads = []
        self.started = False
        del self

    def rot_center(self, image, angle, x, y):

        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

        return rotated_image, new_rect
