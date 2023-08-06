import pygame

from pyNDL.Components import Button
from Shyne.Assets import images
from pyNDL.TextBox import TextBox
from Shyne.Sprite import Sprite

title_font = pygame.font.SysFont('arial', 25)


class SpriteSelector:
    BACKGROUND_COLOR = (66, 66, 66)

    def __init__(self, shyne, display, pos, size):
        self.shyne = shyne
        self.main_display = display

        self.display = pygame.Surface(size)

        self.pos = pos
        self.size = size

        self.nb_per_column = 4
        self.delta = 5

        self.sprite_size = self.size[0] // self.nb_per_column - self.delta - self.delta // self.nb_per_column, \
                           self.size[0] // self.nb_per_column - self.delta - self.delta // self.nb_per_column

        self.sprites = []

        self.sprite_viewers = []

        self.y_delta = 0

        self.add_sprite_btn = AddSpriteButton(self.shyne, self.display, (self.size[0] - 55, self.size[1] - 75),
                                              (50, 50))
        self.add_sprite_btn.parent_pos = self.pos

    def update(self):
        self.sprite_viewers = []
        for sprite in self.sprites:
            self.sprite_viewers.append(
                SpriteViewer(self.shyne, self.display, self.pos, self.pos, self.sprite_size, sprite))

    def frame(self, events, mouse_pos):
        self.display.fill(self.BACKGROUND_COLOR)

        if self.is_hovered(mouse_pos):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.y_delta += 5
                        if self.y_delta > 0:
                            self.y_delta = 0
                    elif event.button == 5:
                        self.y_delta -= 5

        for i, sprite_viewer in enumerate(self.sprite_viewers):
            y = i // self.nb_per_column
            x = i - (y * self.nb_per_column)
            sprite_viewer.pos = (
                x * self.sprite_size[0] + self.delta * (x + 1),
                y * self.sprite_size[1] + self.delta * (y + 1) + self.y_delta)
            sprite_viewer.frame(events, mouse_pos)

        self.add_sprite_btn.frame((0, 0), events, mouse_pos)

        self.main_display.blit(self.display, self.pos)

    def is_hovered(self, mouse_pos):
        if self.pos[0] <= mouse_pos[0] <= self.pos[0] + self.size[0] and self.pos[1] <= mouse_pos[1] <= self.pos[1] + \
                self.size[1]:
            return True
        return False


class SpriteViewer:

    def __init__(self, shyne, display, pos, parent_pos, size, sprite):
        self.shyne = shyne
        self.display = display
        self.parent_pos = parent_pos
        self.pos = pos
        self.size = size

        self.sprite = sprite

        self.color = (200, 200, 200)
        self.hovered_color = (80, 80, 80)
        self.selected_color = (245, 229, 86)

    def frame(self, events, mouse_pos):
        hovered = self.is_hovered(mouse_pos)
        if hovered:
            rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
            pygame.draw.rect(self.display, self.hovered_color, rect, 0, 10)
        rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        pygame.draw.rect(self.display, self.selected_color if self.shyne.current_sprite is self.sprite else self.color,
                         rect, 3, 10)

        name = title_font.render(self.sprite.name, True, (255, 255, 255))

        self.display.blit(name, (
            self.pos[0] + self.size[0] / 2 - name.get_rect().width / 2,
            self.pos[1] + self.size[1] / 2 - name.get_rect().height / 2))

        if hovered:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.on_click()

    def is_hovered(self, mouse_pos):
        pos = self.pos[0] + self.parent_pos[0], self.pos[1] + self.parent_pos[1]
        if pos[0] <= mouse_pos[0] <= pos[0] + self.size[0] and pos[1] <= mouse_pos[1] <= pos[1] + \
                self.size[1]:
            return True
        return False

    def on_click(self):
        self.shyne.select_sprite(self.sprite)


class AddSpriteButton(Button):
    def __init__(self, shyne, display, pos, size):
        super().__init__(display, pos, size, self.add_sprite)
        self.center = False

        self.shyne = shyne

        self.add = images["add"]
        self.add = pygame.transform.scale(self.add, self.size)

        self.add_hovered = self.get_hovered_image(self.add)

    def add_sprite(self):
        self.shyne.add_new_sprite()

    def blit(self):
        self.display.blit(self.add, (self.pos[0], self.pos[1]))

    def blit_hovered(self):
        self.display.blit(self.add_hovered, (self.pos[0], self.pos[1]))


class SpriteNameSetter:
    BACKGROUND_COLOR = (51, 51, 51)
    title_font = pygame.font.SysFont('arial', 20)

    def __init__(self, display, shyne):
        self.display = display
        self.shyne = shyne

        self.size = (350, 83)
        self.pos = (self.display.get_size()[0] / 2 - self.size[0]/2, self.display.get_size()[1] / 2 - self.size[1]/2)

        self.text_box = TextBox(self.display, self.on_changed, size=(self.size[0], 40))

        self.shyne.set_focus_blocked(True)

    def frame(self, events, pos):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        pygame.draw.rect(self.display, self.BACKGROUND_COLOR, rect, 0, 5)  # Background
        title = self.title_font.render("Set Sprite Name", True, (255, 255, 255))
        self.display.blit(title, (self.pos[0] + self.size[0] / 2 - title.get_rect().width / 2, self.pos[1] + 10))
        self.text_box.pos = (self.pos[0], self.pos[1] + title.get_rect().height + 20)
        self.text_box.frame((0, 0), events, pos)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:
                    if not self.is_hovered(pos):
                        self.disable()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.disable()

    def on_changed(self):
        pass

    def is_hovered(self, mouse_pos):
        if self.pos[0] <= mouse_pos[0] <= self.pos[0] + self.size[0] and self.pos[1] <= mouse_pos[1] <= self.pos[1] + \
                self.size[1]:
            return True
        return False

    def disable(self):
        if self.text_box.text != "":
            name = self.text_box.text.replace(" ", "_")
            for sprite in self.shyne.data.sprites:
                if sprite.name == name:
                    return
            new_sprite = Sprite(self.shyne, name)
            self.shyne.add_new_sprite(new_sprite)
        self.shyne.set_focus_blocked(False)
        del self
