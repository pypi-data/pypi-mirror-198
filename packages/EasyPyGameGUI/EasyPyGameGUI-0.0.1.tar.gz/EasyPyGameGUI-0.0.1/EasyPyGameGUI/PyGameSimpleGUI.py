import pygame
import time

pygame.init()

black = '#000000'
white = '#FFFFFF'
gray = '#dbdbdb'
green = '#25f505'

font = pygame.font.SysFont("Arial", 20)

class Button(pygame.rect.Rect):
    def __init__(self, window, text="", text_font=font, text_color=black, color=white, click_color=gray, x=0, y=0, width=100, height=20) -> None:
        super().__init__(x, y, width, height)
        self.window = window
        self.text = text
        self.font = text_font
        self.color = color
        self.hover_color = click_color
        self.text_color = text_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def get_pos(self):
        return (self.x, self.y)
    
    def draw(self):
        text = self.font.render(self.text, True, self.text_color, self.color)
        if text.get_size()[0] > self.width:
            self.width = text.get_size()[0] + 10
            self.x -= self.width//2 - 15
        elif text.get_size()[1] > self.height:
            self.height = text.get_size()[1] + 10
            self.y -= self.height//2 - 15
        pygame.draw.rect(self.window, self.color, [self.x, self.y, self.width, self.height])
        self.window.blit(text, (self.x + self.width//2 - text.get_size()[0]//2, self.y + self.height//2 - text.get_size()[1]//2))
        
    def is_over(self):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        old_color = self.color
        if self.x <= mouse_x <= self.x+self.width and self.y <= mouse_y <= self.y+self.height:
            self.color = self.hover_color
            self.draw()
            pygame.display.update()
            time.sleep(0.1)
            self.color = old_color
            return True   