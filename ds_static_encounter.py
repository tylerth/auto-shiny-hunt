import pyautogui
from PIL import Image
from util_functions import check_starter_shiny, perform_soft_reset, perform_countdown, get_num_soft_resets, write_num_soft_resets, increment_soft_reset, post_actions, validate_mode
import time, sys


def trigger_articuno():

    secs = 21
    while secs > 0:
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        secs -= 1
        time.sleep(1)


def main():

    articuno_leftwing_x_monitor = 1210
    articuno_leftwing_y_monitor = 290
    articuno_leftwing_x_deck = 0
    articuno_leftwing_y_deck = 0
    articuno_nonshiny_r = 121
    articuno_nonshiny_g = 162
    articuno_nonshiny_b = 255

    sr_file = 'articuno_resets.txt'
    image_file = 'starter_check.png'
    reset_per_session = 0

    soft_reset_count = get_num_soft_resets(sr_file)

    mode = sys.argv[1]
    validate_mode(mode)

    if mode in ['-m', '-monitor']:
        x = articuno_leftwing_x_monitor
        y = articuno_leftwing_y_monitor
    else:
        x = articuno_leftwing_x_deck
        y = articuno_leftwing_y_deck
    
    not_shiny = True
    start = time.time()
    try:
        perform_countdown(image_file)
        pyautogui.keyDown('.')
        while not_shiny:
            trigger_articuno()
            not_shiny = check_starter_shiny(articuno_nonshiny_r, articuno_nonshiny_g, articuno_nonshiny_b, x, y, image_file)
            soft_reset_count = increment_soft_reset(soft_reset_count, False)
            reset_per_session = increment_soft_reset(reset_per_session, True)
        post_actions(sr_file, soft_reset_count, reset_per_session, start)
        pyautogui.keyUp('.')
    except KeyboardInterrupt:
        pyautogui.keyUp('.')
        post_actions(sr_file, soft_reset_count, reset_per_session, start)
        exit

main()

