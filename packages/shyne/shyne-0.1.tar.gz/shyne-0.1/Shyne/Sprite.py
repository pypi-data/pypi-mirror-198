import copy
import os
import re

import numpy
import pygame
import inspect

from pyNDL import pyNDL
import random

from pyNDL.Node import Line, ImpureNode, Event


class Sprite:
    def __init__(self, shyne, name):
        self.name = name
        self.id = random.randint(0, 1000000)
        self.shyne = shyne
        self.pyNDL = None
        self.on_load(shyne)

        self.display = None
        self.rotated_display = None

        self.mask = None
        self.rect = None
        self.rotated_rect = None

        self.position = None
        self.rotation = None
        self.last_rot = -99999

        self.draw_func = None
        self.on_frame = None
        self.on_start = None
        self.on_keyboard_event = None

        self.calculate_collisions = False

        self._has_rotation = False  # True if the sprite contains a rotation node

        self.build_file_path = ""

    def on_load(self, shyne):
        self.shyne = shyne
        self.pyNDL = pyNDL(self.shyne.project_path + self.name, self.shyne.window, (0, 0),
                                           self.shyne.scripts_size, show_top_bar=False, allow_save=False, parent=self,
                                           additional_colors=self.shyne.colors, on_action=self.on_action)
        self.display = pygame.Surface(self.shyne.window.get_size()).convert_alpha()
        self.display.fill([0, 0, 0, 0])
        self.mask = None

    def add_tag(self, tag):
        if self.shyne.game.tags.get(tag):
            self.shyne.game.tags[tag].append(self)
        else:
            self.shyne.game.tags[tag] = [self]

    def copy(self):
        return Sprite(self.shyne, self.name)

    def __getstate__(self):
        state = self.__dict__.copy()
        # Don't pickle display
        try:
            del state["shyne"]
            del state["pyNDL"]
            del state["display"]
            del state["mask"]
        except KeyError:
            pass
        return state

    def build_to_file(self):
        self._has_rotation = False
        v_file = []
        imports = ["numpy", "pygame"]
        variables = []

        self.write_v_file(f"class {self.name}:", v_file, br=2)
        self.write_v_file(f"def __init__(self, win, tags=None):", v_file, 1)
        self.write_v_file(f"self.win = win", v_file, 2)
        self.write_v_file(f"self.display = pygame.Surface(self.win.get_size()).convert_alpha()", v_file, 2)
        self.write_v_file(f"self.saved_display = None", v_file, 2)
        self.write_v_file(f"self.display.fill([0, 0, 0, 0])", v_file, 2)
        self.write_v_file(f"self._mouse_pos = None", v_file, 2)
        self.write_v_file(f"self._events = None", v_file, 2)

        self.write_v_file(f"self.tags = tags", v_file, 2)
        self.write_v_file("self.screen_center = numpy.array((self.win.get_width()/2, self.win.get_height()/2))", v_file,
                          2)

        self.write_v_file(f"self.position = numpy.array(self.screen_center)", v_file, 2, br=1)
        self.write_v_file(f"self.rotation = 0", v_file, 2)
        self.write_v_file(f"self._last_rot = 0", v_file, 2)

        self.write_v_file(f"self.mask = None", v_file, 2)
        self.write_v_file(f"self.mask = None", v_file, 2)
        self.write_v_file(f"self.rect = None", v_file, 2)
        self.write_v_file(f"self._first_frame = True", v_file, 2)

        self.write_v_file("", v_file, 2)

        for sprite in self.shyne.data.sprites:
            if sprite is not self:
                self.write_v_file(f"self.s_{sprite.name} = None", v_file, 2)

        """ On Start function """
        if self.on_start:
            self.write_v_file(f"def start(self):", v_file, 1, br=1)
            self.build_nodes(self.on_start, v_file, 2, imports, variables)

        """ Frame function """
        self.write_v_file(f"def frame(self, events, mouse_pos, delta_time):", v_file, 1, br=1)
        self.write_v_file(f"self.display.fill([0,0,0,0])", v_file, 2)
        self.write_v_file(f"self._mouse_pos = mouse_pos", v_file, 2)
        self.write_v_file(f"self._events = events", v_file, 2)
        if self.on_keyboard_event:
            self.write_v_file(f"for event in events:", v_file, 2)
            self.write_v_file(f"if event.type == pygame.KEYDOWN:", v_file, 3)
            self.write_v_file(f"self.on_key_pressed()", v_file, 4)
        if self.on_frame:
            self.build_nodes(self.on_frame, v_file, 2, imports, variables)
        self.write_v_file(f"self.Draw()", v_file, 2)

        rotation_position = len(v_file)

        self.write_v_file(f"if self._first_frame:", v_file, 2)
        self.write_v_file(f"self.setup_collisions(display)", v_file, 3)
        self.write_v_file(f"self._first_frame = False", v_file, 3)
        self.write_v_file(f"self.rect.topleft = self.position", v_file, 2)

        """ On Key Pressed function """
        if self.on_keyboard_event:
            self.write_v_file(f"def on_key_pressed(self):", v_file, 1, br=1)
            self.build_nodes(self.on_keyboard_event, v_file, 2, imports, variables)

        """ Add tag function """
        self.write_v_file("\n".join(("def add_tag(self, tag):",
                                     "    if self.tags.get(tag):",
                                     "        self.tags[tag].append(self)",
                                     "    else:",
                                     "        self.tags[tag] = [self]"
                                     )), v_file, 1, br=1)

        """ Custom functions """
        for func in self.pyNDL.data.functions:
            name = func.name.replace(" ", "_")
            cur_outputs = {}
            for default_name in func.inputs.keys():
                new_name = default_name.replace(" ", "_")
                cur_outputs[func.inputs_node.outputs[default_name]] = new_name
            arguments = ["," + i for i in cur_outputs.values()]
            self.write_v_file(f"def {name}(self{''.join(arguments)}):", v_file, 1, 1)
            self.build_nodes(func.inputs_node, v_file, 2, imports, variables, cur_outputs=cur_outputs)

        """ Setup Collisions function """
        self.write_v_file("def setup_collisions(self, display):", v_file, 1, br=1)
        self.write_v_file("\n".join(("self.Draw()",
                                     "self.mask = pygame.mask.from_surface(display)",
                                     "self.rect = display.get_rect()",
                                     "self.rect.topleft = self.position")), v_file, 2)

        """ Rot Center function """
        self.write_v_file("def rot_center(self, image, angle, x, y):", v_file, 1, br=1)
        self.write_v_file("\n".join(("rotated_image = pygame.transform.rotate(image, angle)",
                                     "new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)",
                                     "return rotated_image, new_rect")), v_file, 2)

        if self._has_rotation:
            self.write_v_file(
                f"rot_display, rect = self.rot_center(self.display, self.rotation, self.position[0], self.position[1])",
                v_file, 2, l=rotation_position)
            self.write_v_file(f"display = rot_display", v_file, 2, l=rotation_position + 1)
            self.write_v_file(f"self.win.blit(rot_display, rect)", v_file, 2, l=rotation_position + 2)
        else:
            self.write_v_file(f"display = self.display", v_file, 2, l=rotation_position)
            self.write_v_file(
                f"self.win.blit(self.display, (self.position[0]-self.display.get_width()/2, self.position[1]-self.display.get_height()/2))",
                v_file, 2, l=rotation_position + 1)

        for var in variables:
            self.write_v_file(f"self.{var[0]} = {var[1]}", v_file, 2, l=16)

        for imp in imports:
            self.write_v_file(f"import {imp}", v_file, l=0)

        with open(self.build_file_path, "w+") as file:
            self.v_file_to_file(v_file, file)

    def build_nodes(self, node, v_file, indent, imports, variables, cur_outputs=None):
        func = self.pyNDL.get_builded_node(node, imports, variables, cur_outputs=cur_outputs, compute_replacements=self.compute_replacements)[0]

        if len(func) == 1 and func[0].line == "pass":
            self.write_v_file("pass", v_file, indent)
        else:
            n_func = copy.copy(func)
            for i, line in enumerate(n_func):
                if line.line.find("pass") != -1:
                    try:
                        incr = line.get_increments()
                        if n_func[i - 1].get_increments() < incr and n_func[i + 1].get_increments() < incr:
                            pass
                        else:
                            func.remove(line)
                    except IndexError:
                        pass
            self.write_v_file(self.func_to_string(func), v_file, indent)

    def compute_replacements(self, node, variables):
        replacements = {"self.pyNDL.parent.shyne.game.delta_time": "delta_time",
                        "self.pyNDL.parent.shyne.game.first_frame": "self._first_frame",
                        "self.pyNDL.parent.shyne.game.mouse_pos": "self._mouse_pos",
                        "self.pyNDL.parent.shyne.game.screen_center": "self.screen_center",
                        "self.pyNDL.parent.add_tag": "self.add_tag",
                        "self.pyNDL.parent.shyne.assets_path": '"./Assets/"',
                        "self.pyNDL.parent.shyne.game.tags": "self.tags",
                        "for k, o, in self.function.inputs_node.outputs.items():": 0,
                        "o.stored_value = self.inputs[k].value": 0,
                        "self.return_value = ": "return ",
                        "position.value": "position",
                        "rotation.value": "rotation",
                        "self.pyNDL.parent": "self"}
        try:
            last_name = node.variable.name
            name = last_name.replace(' ', '_')
            found = False
            for n, default_value, var in variables:
                if node.variable == var:
                    name = n
                    found = True
                    break
            if not found:
                value = node.variable.value

                if type(value) is str:
                    value = f'"{value}"'
                elif type(value) is numpy.ndarray:
                    value = None
                else:
                    value = str(value)
                variables.append((name, value, node.variable))

            replacements["self.variable.value"] = "self." + name
        except AttributeError:
            pass

        try:
            last_name = node.function.name
            name = last_name.replace(' ', '_')
            if node.function.inputs_node.pyNDL.parent != self:
                inp = node.inputs.copy()
                del inp["Sprite"]
                del inp["Function"]
                args = ','.join(
                    [f'self.inputs["{i_n}"].value' for i_n, i in inp.items() if not i.is_execution_pin])
                replacements[
                    "self.function.execute()"] = f"self.s_{node.function.inputs_node.pyNDL.parent.name}.{name}({args})"
            else:
                args = ','.join(
                    [f'self.inputs["{i_n}"].value' for i_n, i in node.inputs.items() if not i.is_execution_pin])
                replacements[
                    "self.function.execute()"] = "self." + name + f"({args})"
        except AttributeError:
            pass

        try:
            name = node.sprite.name

            replacements[
                "self.sprite"] = "self." + "s_" + name
        except AttributeError:
            pass

        return replacements


    def write_v_file(self, text, v_file, indents=0, br=0, l=-1):
        txt = text.split("\n")
        for i in range(0, br):
            if l > -1:
                v_file.insert(l, "")
            else:
                v_file.append("")

        for line in txt:
            if l > -1:
                if indents > 0:
                    if br > 0:
                        v_file.insert(l + 1, "    " * indents + line)
                    else:
                        v_file.insert(l, "    " * indents + line)
                else:
                    if br > 0:
                        v_file.insert(l + 1, line)
                    else:
                        v_file.insert(l, line)
            else:
                if indents > 0:
                    v_file.append("    " * indents + line)
                else:
                    v_file.append(line)

    def v_file_to_file(self, v_file, file):
        print("\n".join(v_file), file=file)

    def func_to_string(self, func):
        func_str = []
        for f in func:
            func_str.append(f.line)
        return "\n".join(func_str)

    def on_action(self):
        #self.build_to_file()
        pass
