import pyautogui
from PIL import Image
import os, sys, time

def perform_soft_reset():
    pyautogui.keyDown('/') # reset, change in retroarch hotkeys
    pyautogui.keyUp('/')

def perform_countdown(filename):
    if os.path.exists(filename):
        os.remove(filename)
    print('Starting program takeover in')
    countdown = 5

    while 0 != countdown:
        print(countdown)
        time.sleep(1)
        countdown -= 1
    
    perform_soft_reset()

def get_num_soft_resets(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            cumulative_srs = f.read()
        return cumulative_srs if cumulative_srs != '' else 0
    else:
        return 0

def write_num_soft_resets(filename, soft_resets):   
    with open(filename, 'w+') as f:
        f.write(str(soft_resets))

def increment_soft_reset(soft_resets, is_session_reset):
    count = int(soft_resets) + 1
    if not is_session_reset:
        print(f'Reset #: {count}')
    return count

def post_actions(sr_file, soft_reset_count, session_resets, start):
    write_num_soft_resets(sr_file, soft_reset_count)
    end = time.time()
    elapsed = end - start
    print(f'Time elapsed: {round(elapsed/60)} mins and {round(elapsed % 60)}s')
    print(f'Total resets this session: {session_resets}')


def validate_mode(arg):
    valid_args = ['-m', '-monitor', '-d', '-deck-only']
    if arg not in valid_args:
        raise Exception(f'Supplied argument not in valid arguments: {valid_args}')

def check_starter_shiny(n_r, n_g, n_b, x, y, filename):
    pyautogui.hotkey('shift', 'print')
    time.sleep(2)
    im = Image.open(filename)
    rgb_im = im.convert('RGB')

    r, g, b = rgb_im.getpixel((x, y))
    # print(r,g,b, x, y)    

    # print(n_r, n_g, n_b, x, y)
    if n_r == r and n_g == g and n_b == b:
        print('Not shiny')
        # original Filename screenshot default at /home/deck/Pictures/: Screenshot_%Y%M%D_%H%m%S
        os.remove(filename)

        not_shiny = True

        perform_soft_reset()

        return not_shiny
    else:
        print('SHINY')
        pyautogui.keyUp('a')
        not_shiny = False
        return not_shiny


        