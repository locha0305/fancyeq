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
        self.font = pygame.font.Font('{}.ttf'.format(font), self.size_pt)
    def pt_to_px(self, pt):
        return pt / 1.2
    def px_to_pt(self, px):
        return px * 1.2
    def render(self):
        rendered = [] #render result
        for token in self.tokens:
            if token["type"] == "default":
                rendered.append([self.font.render(token["text"], self.size_pt, self.color), len(token["text"]), "default"])
            elif token["type"] == "superscript":
                pass
        return rendered
    def display(self, screen, pos):
        rendered = self.render()
        position_x = pos[0]
        position_y = pos[1]
        for token_and_len in rendered:
            token = token_and_len[0]
            length = token_and_len[1]
            
            screen.blit(token, (position_x, position_y))
            position_x += length * self.size_px / 2
        




    
    
        
    
screen = pygame.display.set_mode((500, 500)) #화면 크기 설정


init()

    
eq = equation('C:\WINDOWS\FONTS\TIMES', 20, (255, 255, 255), {"text" : "(x + y)^2 = ", "type":"default"}, {"text" : "x^2 + ", "type":"default"}, {"text" : "2xy + ", "type":"default"}, {"text":"y^2", "type":"default"})
eq.display(screen, (100, 0))
pygame.display.update()

input()

