from pyNDL.Components import Selector, Viewer


class SpritePicker(Selector):
    def __init__(self, display, pos, size):
        from Shyne import Shyne
        super().__init__(display, pos, size, "Select a sprite", Shyne.instance.data.sprites, SpritePViewer)
        self.text_box.is_active = True
        self.is_visible = False
        self.current_text_box = None

    def on_clicked(self, viewer):
        self.is_visible = False
        self.current_text_box.value = viewer.sprite
        self.current_text_box.set_text(viewer.text)
        self.current_text_box.parent.node.on_sprite_selected(viewer.sprite)

    def set_active(self, text_box):
        self.is_visible = True
        self.text_box.set_text("")
        self.current_text_box = text_box
        self.skip_next = True

    def on_unfocus(self):
        self.is_visible = False


class SpritePViewer(Viewer):
    def __init__(self, pyNDL, display, item, pos, delta_pos, size):
        super().__init__(pyNDL, display, pos, delta_pos, size)
        self.sprite = item
        self.text = self.sprite.name
        self.show_delete_btn = False

class FuncPicker(Selector):
    def __init__(self, display, pos, size):
        super().__init__(display, pos, size, "Select a function", [], FuncPViewer)
        self.text_box.is_active = True
        self.is_visible = False
        self.current_text_box = None

    def on_clicked(self, viewer):
        self.is_visible = False
        self.current_text_box.value = viewer.func
        self.current_text_box.set_text(viewer.text)
        self.current_text_box.parent.node.on_func_selected(viewer.func)


    def set_active(self, text_box):
        self.is_visible = True
        self.text_box.set_text("")
        self.current_text_box = text_box
        self.skip_next = True
        self.items = self.current_text_box.parent.node.sprite.pyNDL.get_main_data().functions
        self.search()

    def on_unfocus(self):
        self.is_visible = False


class FuncPViewer(Viewer):
    def __init__(self, pyNDL, display, item, pos, delta_pos, size):
        super().__init__(pyNDL, display, pos, delta_pos, size)
        self.func = item
        self.text = self.func.name
        self.show_delete_btn = False

