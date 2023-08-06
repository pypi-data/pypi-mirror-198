from Shyne.SpritePicker import SpritePicker, FuncPicker

from pyNDL.Node import NodePrefab, Event, ImpureNode, PureNode, Node
from pyNDL.Pin import Input, Output


class CallFunctionFromSprite(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()

        self.inputs["Sprite"] = Input("Sprite", self, ptype="sprite", is_dropdown=True, dropdown=SpritePicker)
        self.outputs["Output"] = Output("Output", self, ptype=None)
        self.name = "Call Function From Sprite"
        self.sprite = None
        self.function = None

    def update(self):
        for name, i in self.function.inputs.items():
            if name not in self.inputs.keys():
                self.add_input_runtime(Input(name, self, default_value=i, ptype=None), name)

        for name, i in self.inputs.items():
            if name != "Sprite" and name != "Function" and not i.is_execution_pin:
                if name not in self.function.inputs.keys():
                    self.remove_input_runtime(name)

    def func(self):
        for k, o, in self.function.inputs_node.outputs.items():
            o.stored_value = self.inputs[k].value
        self.outputs["Output"].stored_value = self.function.execute()

    def on_sprite_selected(self, sprite):
        self.sprite = sprite
        self.add_input_runtime(Input("Function", self, ptype=None, is_dropdown=True, dropdown=FuncPicker), "Function")

    def on_func_selected(self, func):
        self.function = func
        self.function.callers.append(self)
        self.update()

    def on_load(self):
        if self.function:
            self.function = self.pyNDL.parent.shyne.get_sprite_with_id(
                self.sprite.id).pyNDL.get_function_from_name(self.function.name)
            self.function.callers.append(self)


class GetSpritePosition(PureNode, NodePrefab):
    def __init__(self):
        super().__init__()

        self.inputs["Sprite"] = Input("Sprite", self, ptype="sprite", is_dropdown=True, dropdown=SpritePicker)
        self.outputs["Position"] = Output("Position", self, ptype="vec2")
        self.name = "Get Sprite Position"
        self.sprite = None

    def func(self):
        self.outputs["Position"].stored_value = self.sprite.position.value

    def on_sprite_selected(self, sprite):
        self.sprite = sprite
