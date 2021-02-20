from termcolor import colored
'''termcolor module is used for colored error-message output
for further info visit : https://pypi.org/project/termcolor/
'''

try:
    import pygame
except ImportError:
    print(colored("Pygame library is essential for Fancyeq\nPlease install pygame", red))

def init(): #initiallize
    pygame.init()

'''equation class
this creates a equation that appears in a pygame screen

font : Font for equation
size : Size for the basic text ; it takes as Pt, and convert to Px, which is about 1.2px
*tokens : Input text tokens in the equation

__init__ : Initallize equation object
render : Render the curret equation and return as a pygame object
display : Display the equation renderd in render() function
pt_to_px : Convert pt to px
px_to_pt : Convert px to pt
'''
class equation(): 
    def __init__(self, font, size, color, *tokens):
        self.tokens = tokens
        self.size_pt = size
        self.size_px = self.pt_to_px(self.size_pt)
        self.color = color

        self.default_font = pygame.font.Font('{}.ttf'.format(font), self.size_pt)
        self.superscript_font = pygame.font.Font('{}.ttf'.format(font), int(self.size_pt / 2))
        self.subscript_font = pygame.font.Font('{}.ttf'.format(font), int(self.size_pt / 2))
    def pt_to_px(self, pt):
        return pt / 1.2
    def px_to_pt(self, px):
        return px * 1.2
    def render(self):
        rendered = [] #render result
        for token in self.tokens:
            if token["type"] == "default":
                rendered.append([self.default_font.render(token["text"], True, self.color), len(token["text"]), "default"])
            elif token["type"] == "superscript":
                rendered.append([self.superscript_font.render((token["text"]), True, self.color), len(token["text"]), "superscript"])
            elif token["type"] == "subscript":
                rendered.append([self.subscript_font.render((token["text"]), True, self.color), len(token["text"]), "subscript"])
        
        return rendered
    def display(self, screen, pos):
        rendered = self.render()
        position_x = pos[0]
        position_y = pos[1]
        for token_and_len_and_type in rendered:
            token = token_and_len_and_type[0]
            length = token_and_len_and_type[1]
            Type = token_and_len_and_type[2]
            if Type == "default":
                screen.blit(token, (position_x, position_y))
                position_x += length * self.size_px / 2
            elif Type == "superscript":
                screen.blit(token, (position_x, position_y - (self.size_px / 6)))
                position_x += length * self.size_px / 2
            elif Type == "subscript":
                screen.blit(token, (position_x, position_y + (self.size_px / 5 * 4)))
                position_x += length * self.size_px / 4
