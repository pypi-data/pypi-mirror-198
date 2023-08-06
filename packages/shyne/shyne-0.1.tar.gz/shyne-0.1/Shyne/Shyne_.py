import os
import shutil
import sys

import pygame
import threading


from Shyne import Assets
from Shyne.DataHandler import load_data, save_data
from Shyne.Previewer import Previewer
from Shyne.SpriteSelector import SpriteSelector, SpriteNameSetter
from Shyne.Prefabs import *
from pyNDL.VariableAndFunction import Variable, Function
from Shyne.Game import Game


class Shyne:
    BACKGROUND_COLOR = (61, 61, 61)
    instance = None

    def __init__(self, name):
        pygame.init()
        
        Shyne.instance = self
        self.window = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        pygame.display.set_caption('Shyne')

        self.size = self.window.get_size()

        Assets.init()

        self.name = name

        self.data = None

        self.project_path = os.path.dirname(sys.argv[0]) + "/"

        self.assets_path = self.project_path + "Assets/"
        try:
            os.mkdir(self.assets_path)
        except FileExistsError:
            pass

        self.builds_path = self.project_path + "Builds/"

        self.scripts_size = self.size[0] * 2 / 3, self.size[1]

        self.current_sprite = None

        self.previewer = Previewer(self, self.window, (self.scripts_size[0], 0),
                                   (self.size[0] - self.scripts_size[0], self.window.get_height() * (
                                           self.size[0] - self.scripts_size[0]) / self.window.get_width()))

        self.sprite_selector = SpriteSelector(self, self.window, (self.scripts_size[0], self.previewer.size[1]), (
            self.size[0] - self.scripts_size[0], self.size[1] - self.previewer.size[1]))

        self.gui_components = []

        self.colors = {"sprite": (60, 0, 255)}

        self.load_data_from_file(self.name)  # Loads project data

        self.is_fullscreen = False
        self.game = None
        self.start_game()
        self.set_fullscreen(False)

        self.start()

    def start(self):
        self.build()
        while True:
            self.window.fill(self.BACKGROUND_COLOR)

            events = pygame.event.get()
            pos = pygame.mouse.get_pos()
            if not self.is_fullscreen:
                if self.current_sprite:
                    self.current_sprite.pyNDL.frame(events, pos)

                self.previewer.frame(events, pos)
                self.sprite_selector.frame(events, pos)

                for gui_component in self.gui_components:
                    gui_component.frame(events, pos)
            else:
                self.game.frame(events, pos)
            self.keyboard_handler(events, pos)

            pygame.display.update()

    def keyboard_handler(self, events, pos):
        for event in events:
            if event.type == pygame.QUIT:
                self.save()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:  # On Save
                    self.save()
                if event.key == pygame.K_F5:  # Start Program
                    self.start_game()
                if event.key == pygame.K_F6:  # Build
                    self.build()
                if event.key == pygame.K_F11:  # Start Program
                    if not self.is_fullscreen:
                        self.set_fullscreen(True)
                    else:
                        self.set_fullscreen(False)

    def set_fullscreen(self, f):
        self.is_fullscreen = f
        if f:
            self.game.show_fps = True
            self.game.display = self.window
        else:
            self.game.show_fps = False
            self.game.display = pygame.Surface(self.window.get_size())

    def select_sprite(self, sprite):
        self.current_sprite = sprite

    def add_new_sprite(self, sprite=None):
        if sprite is None:
            self.gui_components.append(SpriteNameSetter(self.window, self))
            pass
        else:
            self.data.sprites.append(sprite)
            sprite.on_load(self)

            var = Variable("Position", vtype="vec2", custom_set=SetPosition, custom_get=GetPosition)
            sprite.pyNDL.add_variable(var)
            var = Variable("Rotation", vtype=float)
            sprite.pyNDL.add_variable(var)
            func = Function("Draw")
            sprite.pyNDL.add_function(func)
            sprite.pyNDL.leftBar.update()

            self.current_sprite = sprite
            self.sprite_selector.sprites = self.data.sprites
            self.sprite_selector.update()
            for gui_component in self.gui_components:
                if type(gui_component) is SpriteNameSetter:
                    self.gui_components.remove(gui_component)
                    break
            self.game.start()
            self.build()

    def save(self):
        save_data(self.name, self.data)
        for sprite in self.data.sprites:
            sprite.pyNDL.save()

    def load_data_from_file(self, filename):
        data = load_data(filename)
        self.load_data(data)

    def load_data(self, data):
        self.data = data
        for sprite in self.data.sprites:
            sprite.on_load(self)
        self.sprite_selector.sprites = self.data.sprites
        self.sprite_selector.update()

        for sprite in self.data.sprites:
            for node in sprite.pyNDL.get_main_data().get_all_nodes():
                node.on_load()

    def set_focus_blocked(self, focus):
        if self.current_sprite:
            self.current_sprite.pyNDL.set_focus_blocked(focus)

    def start_game(self):
        """ Start the current script """
        print("--------------------New Start Call--------------------")
        self.game = Game(self.window if self.is_fullscreen else pygame.Surface(self.window.get_size()), self.data,
                         show_fps=True if self.is_fullscreen else False)

        self.game.start()

    def get_sprite_with_id(self, id):
        for sprite in self.data.sprites:
            if sprite.id == id:
                return sprite
        return None

    def build(self):
        x = threading.Thread(target=self.build_threaded)
        x.start()

    def build_threaded(self):
        show_fps = True

        print("Building started...")
        shutil.rmtree(self.builds_path, ignore_errors=True)     # Removing the builds directory
        try:
            os.mkdir(self.builds_path)
        except FileExistsError:
            pass

        shutil.copytree(self.assets_path, self.builds_path + "Assets")

        """ main.py """
        with open(self.builds_path + "main.py", "w+") as main:
            self.write_file(f"import pygame", main)
            for sprite in self.data.sprites:
                self.write_file(f"import {sprite.name}", main)

            self.write_file("pygame.init()", main)
            self.write_file("small_font = pygame.font.SysFont('arial', 25)", main)
            self.write_file("", main)

            self.write_file("win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)", main)
            self.write_file("pygame.display.set_caption('Shyne')", main)
            self.write_file("clock = pygame.time.Clock()", main)
            self.write_file("tags = {}", main)

            self.write_file("", main)

            for sprite in self.data.sprites:
                self.write_file(f"s_{sprite.name} = {sprite.name}.{sprite.name}(win, tags=tags)", main)

            self.write_file("", main)

            for sprite in self.data.sprites:
                vars = [f"s_{sprite.name}.s_{s.name}" for s in self.data.sprites if s is not sprite]
                sprites = [f"s_{s.name}" for s in self.data.sprites if s is not sprite]
                if vars and sprites:
                    self.write_file(f"{', '.join(vars)} = {', '.join(sprites)}", main)

            self.write_file("", main)

            for sprite in self.data.sprites:
                if sprite.on_start:
                    self.write_file(f"s_{sprite.name}.start()", main)

            self.write_file("", main)

            self.write_file("while True:", main)
            self.write_file("dt = clock.tick()", main, 1, 1)
            self.write_file("fps = int(clock.get_fps())", main, 1, 1)
            self.write_file("events = pygame.event.get()", main, 1)
            self.write_file("mouse_pos = pygame.mouse.get_pos()", main, 1)
            self.write_file("win.fill((255, 255, 255))", main, 1, 1)

            self.write_file("", main)

            for sprite in self.data.sprites:
                self.write_file(f"s_{sprite.name}.frame(events, mouse_pos, dt)", main, 1)

            self.write_file("", main)
            if show_fps:
                self.write_file("fps_txt = small_font.render(str(fps), True, (0, 0, 255))", main, 1)
                self.write_file("win.blit(fps_txt, (10, 10))", main, 1)
            self.write_file("pygame.display.update()", main, 1)

        """ Sprites """

        for sprite in self.data.sprites:
            sprite.build_file_path = self.builds_path + f"{sprite.name}.py"
            sprite.build_to_file()

        print("Done")

    def write_file(self, text, file, indents=0, br=0):
        for i in range(0, br):
            print(file=file)
        if indents > 0:
            print("    " * indents + text, file=file)
        else:
            print(text, file=file)
