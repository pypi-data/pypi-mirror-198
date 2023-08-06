import pygame

from pyNDL.Components import KeyPicker
from pyNDL.Node import NodePrefab, Event, ImpureNode, PureNode, Node
from pyNDL.Pin import Input, Output


class OnKeyPressEvent(Event, NodePrefab):

    def __init__(self):
        super().__init__()
        self.name = "On Key Pressed"


class IsKeyPressed(PureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.inputs["Key"] = Input("Key", self, ptype="key", is_dropdown=True, dropdown = KeyPicker)
        self.outputs["Output"] = Output("Output", self, ptype=bool)

        self.name = "Is Key Pressed"

    def func(self):
        keys = pygame.key.get_pressed()
        self.outputs["Output"].stored_value = keys[self.inputs["Key"].value]


class GetMousePosition(PureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.outputs["Position"] = Output("Position", self, ptype="vec2")

        self.name = "Get Mouse Position"

    def func(self):
        self.outputs["Position"].stored_value = self.pyNDL.parent.shyne.game.mouse_pos - self.pyNDL.parent.shyne.game.screen_center