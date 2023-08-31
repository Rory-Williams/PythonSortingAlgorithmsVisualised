import pygame
import random
from SortingAlgorithms import bubble_sort, \
    insertion_sort, selection_sort, merge_sort
from DrawMethods import DrawInfo, draw_lst, draw


def generate_start_lst(n, min_val, max_val):
    lst = []
    for _ in range(n):
        lst.append(random.randint(min_val, max_val))
    return lst


def main():
    run = True
    clock = pygame.time.Clock()
    n = 100  #number of bars
    min_val = 0  # min/max bar values (normalised regardless)
    max_val = 50
    lst = generate_start_lst(n, min_val, max_val)
    draw_info = DrawInfo(1000, 600, lst)
    sorting = False
    ascending = True

    sort_alg = bubble_sort  #choose sorting algorith
    sort_alg_name = 'Bubble Sort'
    sort_alg_gen = None     # used to perform algorithm

    while run:  # pygame main loop to handle game
        clock.tick(500)  # fps of clock, remove for max speed of CPU
        if sorting:
            try:
                next(sort_alg_gen)
            except StopIteration:  # error thrown when sorting is complete
                sorting = False
            except TypeError:
                sorting = False
        else:
            draw(draw_info, sort_alg_name, ascending)

        for event in pygame.event.get():  # get any event variables
            if event.type == pygame.QUIT:  # red x on window will trigget this event
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:  # reset bars
                lst = generate_start_lst(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and not sorting:  # start sorting
                sorting = True
                sort_alg_gen = sort_alg(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:  # start sorting
                ascending = True
            elif event.key == pygame.K_d and not sorting:  # start sorting
                ascending = False
            elif event.key == pygame.K_b and not sorting:  # start sorting
                sort_alg = bubble_sort
                sort_alg_name = 'Bubble Sort'
            elif event.key == pygame.K_i and not sorting:  # start sorting
                sort_alg = insertion_sort
                sort_alg_name = 'Insertion Sort'
            elif event.key == pygame.K_s and not sorting:  # start sorting
                sort_alg = selection_sort
                sort_alg_name = 'Selection Sort'
            elif event.key == pygame.K_m and not sorting:  # start sorting
                sort_alg = merge_sort
                sort_alg_name = 'Merge Sort'

    pygame.quit()


if __name__ == '__main__':
    main()





















