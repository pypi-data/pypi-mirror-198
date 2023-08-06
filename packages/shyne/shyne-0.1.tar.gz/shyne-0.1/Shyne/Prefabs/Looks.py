import pygame

from pyNDL.Node import NodePrefab, Event, ImpureNode, PureNode
from pyNDL.Pin import Input, Output
from Shyne.SpritePicker import SpritePicker


class DrawRect(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()

        self.inputs["Position"] = Input("Relative Position", self, ptype="vec2")
        self.inputs["Size"] = Input("Size", self, ptype="vec2")
        self.inputs["Color"] = Input("Color", self, ptype='vec3')
        self.inputs["Width"] = Input("Width", self, ptype=int)

        self.name = "Draw Rect"

    def func(self):
        position = self.inputs["Position"].value
        scale = self.inputs["Size"].value
        rect = pygame.Rect((self.pyNDL.parent.display.get_width() / 2 + position[0] - scale[0] / 2,self.pyNDL.parent.display.get_height() / 2 + position[1] - scale[1] / 2), scale)
        pygame.draw.rect(self.pyNDL.parent.display, self.inputs["Color"].value, rect,self.inputs["Width"].value)


class DrawCircle(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()

        self.inputs["Position"] = Input("Relative Position", self, ptype="vec2")
        self.inputs["Radius"] = Input("Radius", self, ptype=float)
        self.inputs["Color"] = Input("Color", self, ptype="vec3")
        self.inputs["Width"] = Input("Width", self, ptype=int)

        self.name = "Draw Circle"

    def func(self):
        position = self.inputs["Position"].value
        pygame.draw.circle(self.pyNDL.parent.display, self.inputs["Color"].value, (self.pyNDL.parent.display.get_width() / 2 + position[0],self.pyNDL.parent.display.get_height() / 2 + position[1]),self.inputs["Radius"].value, self.inputs["Width"].value)


class AddTag(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()

        self.inputs["Tag"] = Input("Tag", self, ptype=str)

        self.name = "Add Tag"

    def func(self):
        self.pyNDL.parent.add_tag(self.inputs["Tag"].value)


class IsCollidingWithSprite(PureNode, NodePrefab):
    def __init__(self):
        super().__init__()

        self.inputs["Sprite"] = Input("Sprite", self, ptype="sprite", is_dropdown=True, dropdown=SpritePicker)
        self.outputs["Result"] = Output("Result", self, ptype=bool)
        self.sprite = None
        self.name = "Is Colliding (Sprite)"

    def func(self):
        if not self.pyNDL.parent.shyne.game.first_frame:
            offset_x, offset_y = (self.sprite.rect.left - self.pyNDL.parent.rect.left), (self.sprite.rect.top - self.pyNDL.parent.rect.top)
            self.outputs["Result"].stored_value = self.pyNDL.parent.mask.overlap(self.sprite.mask, (offset_x, offset_y)) is not None
        else:
            self.outputs["Result"].stored_value = False

    def on_sprite_selected(self, sprite):
        self.sprite = sprite

    def on_load(self):
        if self.sprite:
            self.sprite = self.pyNDL.parent.shyne.get_sprite_with_id(self.sprite.id)


class IsCollidingWithTag(PureNode, NodePrefab):
    def __init__(self):
        super().__init__()

        self.inputs["Tag"] = Input("Tag", self, ptype=str)
        self.outputs["Result"] = Output("Result", self, ptype=bool)
        self.name = "Is Colliding (Tag)"

    def func(self):
        if not self.pyNDL.parent.shyne.game.first_frame:
            sprites = self.pyNDL.parent.shyne.game.tags.get(self.inputs["Tag"].value, None)
            if sprites is None:
                self.outputs["Result"].stored_value = False
                return
            for sprite in sprites:
                offset_x, offset_y = (sprite.rect.left - self.pyNDL.parent.rect.left), (sprite.rect.top - self.pyNDL.parent.rect.top)
                if self.pyNDL.parent.mask.overlap(sprite.mask, (offset_x, offset_y)) is not None:
                    self.outputs["Result"].stored_value = True
                    return
            self.outputs["Result"].stored_value = False
        else:
            self.outputs["Result"].stored_value = False


class CalculateCollisions(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.name = "Calculate Collisions"

    def func(self):
        self.pyNDL.parent.calculate_collisions = True

    def on_sprite_selected(self, sprite):
        self.sprite = sprite


class DrawImage(ImpureNode, NodePrefab):
    def __init__(self):
        super().__init__()
        self.name = "Draw Image"
        self.inputs["Name"] = Input("Name", self, ptype=str, text_box_width_mult=2)
        self.inputs["Position"] = Input("Relative Position", self, ptype="vec2")
        self.inputs["Size"] = Input("Size", self, ptype="vec2")

        self.image = None
        self.current_image_name = ""
        self.unpickle_vars.append("image")

    def func(self):
        position = self.inputs["Position"].value
        scale = self.inputs["Size"].value
        name = self.inputs["Name"].value
        if not self.image or name != self.current_image_name:
            self.image = pygame.image.load(self.pyNDL.parent.shyne.assets_path + name).convert_alpha()
            self.current_image_name = name
        self.pyNDL.parent.display.blit(pygame.transform.scale(self.image, scale), (self.pyNDL.parent.display.get_width() / 2 + position[0] - scale[0] / 2,self.pyNDL.parent.display.get_height() / 2 + position[1] - scale[1] / 2))

    def on_load(self):
        self.image = None
