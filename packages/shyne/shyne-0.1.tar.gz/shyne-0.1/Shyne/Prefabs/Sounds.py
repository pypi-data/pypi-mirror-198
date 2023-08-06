import pygame

from pyNDL.Node import NodePrefab, Event, ImpureNode, PureNode
from pyNDL.Pin import Input, Output


class PlaySound(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.name = "Play Sound"
        self.inputs["Name"] = Input("Name", self, ptype=str, text_box_width_mult=2)
        self.outputs["Sound"] = Output("   Sound", self, ptype=None)

        self.sound = None
        self.current_sound_name = ""
        self.unpickle_vars.append("sound")

        self.custom_vars.append("sound")
        self.custom_vars.append("current_sound_name")

    def func(self):
        name = self.inputs["Name"].value
        if not self.sound or name != self.current_sound_name:
            self.sound = pygame.mixer.Sound(self.pyNDL.parent.shyne.assets_path + name)
            self.current_sound_name = name
            self.outputs["Sound"].stored_value = self.sound
        pygame.mixer.Sound.play(self.sound)

    def on_load(self):
        self.sound = None


class SetVolume(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.name = "Set Volume"

        self.inputs["Sound"] = Input("Sound", self, ptype=None)
        self.inputs["Volume"] = Input("Volume", self, ptype=float)

    def func(self):
        self.inputs["Sound"].value.set_volume(self.inputs["Volume"].value)

class GetVolume(PureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.name = "Get Volume"

        self.inputs["Sound"] = Input("Sound", self, ptype=None)
        self.outputs["Volume"] = Output("Volume", self, ptype=float)

    def func(self):
        self.outputs["Volume"].stored_value = self.inputs["Sound"].value.get_volume()


class PlayMusic(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.name = "Play Music"
        self.inputs["Name"] = Input("Name", self, ptype=str, text_box_width_mult=2)
        self.inputs["Repeat"] = Input("Repeat", self, ptype=int, default_value=-1)

    def func(self):
        pygame.mixer.music.load(self.pyNDL.parent.shyne.assets_path + self.inputs["Name"].value)
        pygame.mixer.music.play(self.inputs["Repeat"].value)


class PauseMusic(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.name = "Pause Music"

    def func(self):
        pygame.mixer.music.pause()


class UnpauseMusic(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.name = "Unpause Music"

    def func(self):
        pygame.mixer.music.unpause()


class StopMusic(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.name = "Stop Music"

    def func(self):
        pygame.mixer.music.stop()


class Fadeout(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.name = "Fade Out"
        self.inputs["Sound"] = Input("Sound", self, ptype=None)
        self.inputs["Time"] = Input("Time", self, ptype=float, default_value=1)

    def func(self):
        self.inputs["Sound"].value.fadeout(self.inputs["Time"].value*1000)
