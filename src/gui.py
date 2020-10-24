import pygame
import pygame_gui

class Gui:
  def __init__(self, screen):
    self.screen = screen
    self.manager = pygame_gui.UIManager(screen.get_size())
    self.texts = {
        'test': ''
    }

    self.button_test_one = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 20), (100, 50)),
                       text='test 1',
                       manager=self.manager)

    self.button_test_two = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 70), (100, 50)),
                       text='test 2',
                       manager=self.manager)

    self.button_init_trees = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 120), (100, 50)),
                       text='init trees',
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
