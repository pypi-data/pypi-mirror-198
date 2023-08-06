from pyNDL.Node import NodePrefab, Event
from Shyne.Prefabs.Looks import *
from Shyne.Prefabs.Motion import *
from Shyne.Prefabs.Inputs import *
from Shyne.Prefabs.Communication import *
from Shyne.Prefabs.Sounds import *

class OnFrameEvent(Event, NodePrefab):

    def __init__(self):
        super().__init__()
        self.name = "On Frame"
        self.outputs["Delta Time"] = Output("Delta Time", self, ptype=float)

    def func(self):
        self.outputs["Delta Time"].stored_value = self.pyNDL.parent.shyne.game.delta_time

class SpawnNewSprite(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.name = "Spawn New Sprite"
        self.inputs["sprite"] = Input("Sprite", self, ptype="sprite", is_dropdown=True, dropdown=SpritePicker)
        self.outputs["new sprite"] = Output("Sprite", self, ptype="sprite")

        self.sprite = None

    def func(self):
        self.outputs["new sprite"].stored_value = self.sprite.clone()

    def on_sprite_selected(self, sprite):
        self.sprite = sprite