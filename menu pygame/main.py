import pygame
import sys

class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.pos = pos
        self.text_input = text_input
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        if self.image:
            self.rect = self.image.get_rect(center=self.pos)
        else:
            text_surface = self.font.render(self.text_input, True, (0, 0, 0))
            self.rect = text_surface.get_rect(center=self.pos)
    
    def changeColor(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hovering_color
        else:
            self.color = self.base_color

    def update(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
            text_surface = self.font.render(self.text_input, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            text_surface = self.font.render(self.text_input, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.bg = pygame.image.load("assets/Background.png")
        self.menu_font = self.get_font(100)
        self.buttons = [
            Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                   text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White"),
            Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                   text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White"),
            Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                   text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
        ]

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def run(self):
        while True:
            self.screen.blit(self.bg, (0, 0))
            menu_mouse_pos = pygame.mouse.get_pos()
            menu_text = self.menu_font.render("MAIN MENU", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=(640, 100))
            self.screen.blit(menu_text, menu_rect)

            for button in self.buttons:
                button.changeColor(menu_mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.rect.collidepoint(menu_mouse_pos):
                            if button.text_input == "PLAY":
                                return "game_selection"
                            elif button.text_input == "OPTIONS":
                                return "options"
                            elif button.text_input == "QUIT":
                                pygame.quit()
                                sys.exit()

            pygame.display.update()

class GameSelection:
    def __init__(self, screen):
        self.screen = screen
        self.selection_font = self.get_font(45)
        self.buttons = [
            Button(image=None, pos=(640, 250), text_input="PACMAN", font=self.get_font(75),
                   base_color="#d7fcd4", hovering_color="White"),
            Button(image=None, pos=(640, 400), text_input="TETRIS", font=self.get_font(75),
                   base_color="#d7fcd4", hovering_color="White"),
            Button(image=None, pos=(640, 550), text_input="SNAKE", font=self.get_font(75),
                   base_color="#d7fcd4", hovering_color="White")
        ]

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def run(self):
        while True:
            selection_mouse_pos = pygame.mouse.get_pos()
            self.screen.fill("white")
            selection_text = self.selection_font.render("SELECT A GAME", True, "Black")
            selection_rect = selection_text.get_rect(center=(640, 100))
            self.screen.blit(selection_text, selection_rect)

            for button in self.buttons:
                button.changeColor(selection_mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.rect.collidepoint(selection_mouse_pos):
                            if button.text_input == "PACMAN":
                                return "play_pacman"
                            elif button.text_input == "TETRIS":
                                return "play_tetris"
                            elif button.text_input == "SNAKE":
                                return "play_snake"

            pygame.display.update()

class PlayPacman:
    def __init__(self, screen):
        self.screen = screen
        # Initialize Pacman game here

    def run(self):
      
        pass

class PlayTetris:
    def __init__(self, screen):
        self.screen = screen
        # Initialize Tetris game here

    def run(self):
        # Run Tetris game loop here
        pass

class PlaySnake:
    def __init__(self, screen):
        self.screen = screen
        # Initialize Snake game here

    def run(self):
        # Run Snake game loop here
        pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")
    current_screen = "main_menu"

    while True:
        if current_screen == "main_menu":
            menu = MainMenu(screen)
            current_screen = menu.run()
        elif current_screen == "game_selection":
            game_selection = GameSelection(screen)
            current_screen = game_selection.run()
        elif current_screen == "play_pacman":
            play_pacman = PlayPacman(screen)
            current_screen = play_pacman.run()
        elif current_screen == "play_tetris":
            play_tetris = PlayTetris(screen)
            current_screen = play_tetris.run()
        elif current_screen == "play_snake":
            play_snake = PlaySnake(screen)
            current_screen = play_snake.run()

if __name__ == "__main__":
    main()
