
from pyNDL.Node import NodePrefab, Event, ImpureNode, PureNode
from pyNDL.Pin import Input, Output
import math

class SetPosition(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()

        self.inputs["Position"] = Input("Position", self, ptype="vec2")

        self.name = "Set Position"

    def func(self):
        self.pyNDL.parent.position.value = self.pyNDL.parent.shyne.game.screen_center + self.inputs["Position"].value

    def on_variable_change(self, var):
        pass

class GetPosition(PureNode, NodePrefab):
    def __init__(self):
        super().__init__()

        self.outputs = {"Value": Output("Position", self, ptype=None)}

        self.name = "Pos"
        self.show_name = False
        self.compact = True

        self.is_visible_on_search = False

    def func(self):
        self.outputs["Value"].stored_value = self.pyNDL.parent.position.value - self.pyNDL.parent.shyne.game.screen_center


class ChangePosition(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()

        self.inputs["Position"] = Input("Position", self, ptype="vec2")

        self.name = "Change Position"

    def func(self):
        self.pyNDL.parent.position.value += self.inputs["Position"].value


class Turn(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()

        self.inputs["Degree"] = Input("Degree", self, ptype=float)

        self.name = "Turn"

    def func(self):
        self.pyNDL.parent.rotation.value += self.inputs["Degree"].value

class PointTowards(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()

        self.inputs["Position"] = Input("Position", self, ptype="vec2")

        self.name = "Point Towards"

        self.add_import("math")

    def func(self):
        a = self.pyNDL.parent.position.value
        b = self.inputs["Position"].value
        self.pyNDL.parent.rotation.value = 360-math.degrees(math.atan2(b[1]-a[1], b[0]-a[0]))