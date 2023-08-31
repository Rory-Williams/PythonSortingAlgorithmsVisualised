import pygame
from math import floor

pygame.init()


class DrawInfo:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = [128, 128, 128]
    BACKGROUND_COLOUR = WHITE
    SIDE_PAD = 100  #100px side padding total
    TOP_PAD = 200  #for header
    MIN_BAR_HEIGHT = 10
    FONT = pygame.font.SysFont('comicsans', 30)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)
    BAR_GRADIENTS = [
        GREY,
        [i * 1.25 for i in GREY],
        [i * 1.5 for i in GREY]
    ]

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualisation")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)
        self.bar_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.bar_height = floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOUR)
    title_txt = draw_info.LARGE_FONT.render(
    f'{algo_name} - {"Ascending" if ascending else "Descending"}',
    1, draw_info.BLACK)
    draw_info.window.blit(title_txt, (draw_info.width/2 - title_txt.get_width()/2, 5))

    control_txt = draw_info.FONT.render(
        'R - Reset ¦ SPACE - Start Sorting ¦ A - Ascending ¦ D - Descending',
        1, draw_info.GREY)
    draw_info.window.blit(control_txt, (draw_info.width/2 - control_txt.get_width()/2, 55))

    sort_txt = draw_info.FONT.render(
        'I - Insertion ¦ B - Bubble ¦ S - Selection ¦ M - Merge Sort',
        1, draw_info.GREY)
    draw_info.window.blit(sort_txt, (draw_info.width / 2 - sort_txt.get_width() / 2, 90))

    draw_lst(draw_info)
    pygame.display.update()


def draw_lst(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2,
                          draw_info.TOP_PAD-draw_info.MIN_BAR_HEIGHT,
                          draw_info.width-draw_info.SIDE_PAD,
                          draw_info.height-draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOUR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.bar_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.bar_height - draw_info.MIN_BAR_HEIGHT  #minus 10 to add some visability always
        colour = draw_info.BAR_GRADIENTS[i % 3]
        # colour = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

        if i in color_positions:
            colour = color_positions[i]

        pygame.draw.rect(draw_info.window, colour, (x, y, draw_info.bar_width, draw_info.height))

    if clear_bg:
        pygame.display.update()


