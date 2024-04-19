import pyautogui
from PIL import Image
import os, sys, time
# import pyscreeze

# map button names to keys
a = 's'
b = 'a'
start = 'enter'
soft_reset = '/'

# init some variables
nonshiny_r, nonshiny_g, nonshiny_b = 0, 0, 0
bulb_color_coordinate_nonshiny_x = 0
bulb_color_coordinate_nonshiny_y = 0


# utility functions

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

# action functions

def select_starter():
    # selecting starter
    pyautogui.keyDown(a)
    time.sleep(17)
    pyautogui.keyUp(a)

    # decline nickname
    pyautogui.keyDown(b)
    time.sleep(7)
    pyautogui.keyUp(b)

    # print('Starter selected. Moving to battle')

def walk_to_battle():

    # walk into Oak
    pyautogui.keyDown('Left')
    time.sleep(1)
    pyautogui.keyUp('Left')

    # walk down to battle
    pyautogui.keyDown('Down')
    time.sleep(2)
    pyautogui.keyUp('Down')

def progress_battle():
    pyautogui.keyDown(b)
    # time.sleep(21) # to get past oak lecture
    time.sleep(14) # to get into oak lecture
    pyautogui.keyUp(b)

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
        pyautogui.keyUp(a)
        not_shiny = False
        return not_shiny

# monitor .422 diff
# - width: 2560 (.4648)
# - height: 1080 (.52)

# deck .375 diff
# - width: 1280 (.4289)
# - height: 800 (.5275)
def autodetect_x_y():

    PIXEL_LOC_WIDTH = .46 #ratio of where the pixel to check is on screen
    PIXEL_LOC_HEIGHT = .52

    screen_size = pyautogui.size()
    x = screen_size.width * PIXEL_LOC_WIDTH
    y = screen_size.height * PIXEL_LOC_HEIGHT

    return {'x' : x, 'y' : y} 


def main():

    image_file = 'starter_check.png'
    sr_file = 'softresets.txt'
    soft_reset_count = get_num_soft_resets(sr_file)
    reset_per_session = 0

    # bulbasaur backsprite at coordinate 45, 30 (back of head)
    # nonshiny_r, nonshiny_g, nonshiny_b = 99, 210, 165 # during battle
    nonshiny_r, nonshiny_g, nonshiny_b = 49, 105, 82 # during oak lecture

    mode = sys.argv[1]
    validate_mode(mode)

    # coords = autodetect_x_y()
    # print(coords)
    # bulb_color_coordinate_nonshiny_x = coords['x']
    # bulb_color_coordinate_nonshiny_y = coords['y']
    if mode in ['-m', '-monitor']:
        bulb_color_coordinate_nonshiny_x = 1190
        bulb_color_coordinate_nonshiny_y = 562
    else:
        bulb_color_coordinate_nonshiny_x = 549
        bulb_color_coordinate_nonshiny_y = 422

    not_shiny = True
    start = time.time()
    try:
        # print(soft_reset_count)
        perform_countdown(image_file)
        pyautogui.keyDown('leftbracket') # speed up, or leftbracket
        while not_shiny:
            select_starter()
            walk_to_battle()
            progress_battle()
            not_shiny = check_starter_shiny(nonshiny_r, nonshiny_g, nonshiny_b, bulb_color_coordinate_nonshiny_x, bulb_color_coordinate_nonshiny_y, image_file)
            soft_reset_count = increment_soft_reset(soft_reset_count, False)
            reset_per_session = increment_soft_reset(reset_per_session, True)
        pyautogui.keyUp('leftbracket') # speed up
        post_actions(sr_file, soft_reset_count, reset_per_session, start)
    except KeyboardInterrupt:
        post_actions(sr_file, soft_reset_count, reset_per_session, start)
        exit

main()

