import pygame
import pygame_gui

class Gui:
  def __init__(self, screen):
    self.screen = screen
    self.manager = pygame_gui.UIManager(screen.get_size())
    self.texts = {
        'test': ''
    }

    self.button_restart_mountains = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 20), (140, 50)),
                       text='restart mountains',
                       manager=self.manager)

    self.button_restart_clouds = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 70), (140, 50)),
                       text='restart clouds',
                       manager=self.manager)

    self.button_restart_trees = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 120), (140, 50)),
                       text='restart trees',
                       manager=self.manager)

    self.font = pygame.font.Font(pygame.font.get_default_font(), 18)

  def update(self, time_delta):
    self.manager.update(time_delta)
    self.manager.draw_ui(self.screen)

    text_surface = self.font.render(self.texts['test'], True, (255, 255, 255))
    self.screen.blit(text_surface, dest=(10,180))

  def process_event(self, event):
    self.manager.process_events(event)

  def set_text(self, key: str, value: str):
      self.texts[key] = value
