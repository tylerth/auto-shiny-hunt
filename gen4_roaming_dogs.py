import pyautogui
from PIL import Image
from util_functions import check_starter_shiny, perform_soft_reset, perform_countdown, get_num_soft_resets, write_num_soft_resets, increment_soft_reset, post_actions, validate_mode
import time, sys, os

def menu_spam():
    secs = 18
    while secs > 0:
        # print(secs)
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        secs -= 1
        time.sleep(0.5)

def burned_tower():
    # print('walking left')
    pyautogui.keyDown('Left')
    time.sleep(0.5)
    pyautogui.keyUp('Left')

    # print('waiting for cutscene')
    time.sleep(13)
    button_spam = 11

    while button_spam > 0:
        # print(button_spam)

        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        button_spam -= 1
        time.sleep(0.3)
    
    # print('opening bag')
    pyautogui.keyDown('y')
    pyautogui.keyUp('y')
    time.sleep(0.3)
    pyautogui.keyDown('Down')
    pyautogui.keyUp('Down')
    time.sleep(0.3)
    pyautogui.keyDown('Down')
    pyautogui.keyUp('Down')
    time.sleep(0.3)
    pyautogui.keyDown('a')  # open bag
    pyautogui.keyUp('a')
    time.sleep(1.6)
    # print('using escape rope')
    pyautogui.keyDown('a')
    pyautogui.keyUp('a')
    time.sleep(1.5)

    pyautogui.keyDown('a')
    pyautogui.keyUp('a')
    # print('escape rope used')
    time.sleep(11)
    
    # time.sleep(0.3)
    # pyautogui.keyDown('a')
    # pyautogui.keyUp('a')


def navigate_to_route():
    # print('bike')
    pyautogui.keyDown('x') # engage bike
    pyautogui.keyUp('x')

    pyautogui.keyDown('Down')
    time.sleep(0.5)
    pyautogui.keyUp('Down')


    pyautogui.keyDown('Right')
    time.sleep(0.87)
    pyautogui.keyUp('Right')

    pyautogui.keyDown('Down')
    time.sleep(4)
    pyautogui.keyUp('Down')

    # pyautogui.keyDown('Down')
    # time.sleep(1.5)
    # pyautogui.keyUp('Down')

def use_repel():

    print('using repel')
    # clear any textboxes
    pyautogui.keyDown('a')
    pyautogui.keyUp('a')

    pyautogui.keyDown('y')
    pyautogui.keyUp('y')
    time.sleep(0.3)
    pyautogui.keyDown('a')  # open bag
    pyautogui.keyUp('a')
    time.sleep(1)
   
    pyautogui.keyDown('a')
    pyautogui.keyUp('a')
    time.sleep(1)
    pyautogui.keyDown('a')
    pyautogui.keyUp('a')

    time.sleep(1)
    pyautogui.keyDown('a')
    pyautogui.keyUp('a')
    time.sleep(0.5)
    pyautogui.keyDown('a')
    pyautogui.keyUp('a')
    
    # print('exiting bag')
    pyautogui.keyDown('b')
    pyautogui.keyUp('b')
    time.sleep(1)
    pyautogui.keyDown('b')
    pyautogui.keyUp('b')
    time.sleep(1)
    pyautogui.keyDown('b')
    pyautogui.keyUp('b')
    time.sleep(1)
    pyautogui.keyDown('b')
    pyautogui.keyUp('b')

    # print('bag exited')
    # reorient down
    # print('reorienting down')
    pyautogui.keyDown('Down')
    time.sleep(2)
    pyautogui.keyUp('Down')


def attack():
    # print('attacking')
    pyautogui.keyDown('Up')
    pyautogui.keyUp('Up')

    pyautogui.keyDown('a')
    time.sleep(0.3)
    pyautogui.keyUp('a')

    pyautogui.keyDown('a')
    time.sleep(0.3)
    pyautogui.keyUp('a')

    time.sleep(9) # wait for health

    
    # print('clicking through xp')
    i = 13
    while i > 0:
        pyautogui.keyDown('a')
        pyautogui.keyUp('a')
        time.sleep(0.2)
        i -= 1
    
    # print('battle ended')
    # print('reorienting down')
    pyautogui.keyDown('Down')
    time.sleep(2)
    pyautogui.keyUp('Down')



def determine_state(filename, num_beasts_remaining, mode):


    if mode in ['-m', '-monitor']:
        # for repel textbox black right
        txt_x = 1408
        txt_y = 711
        txt_r, txt_g, txt_b = 97, 97, 105

        # for repel textbox white
        txtw_x = 1450
        txtw_y = 785
        txtw_r, txtw_g, txtw_b = 251, 251, 251

        # for entei
        e_x = 1258
        e_y = 425
        entei_r, entei_g, entei_b = 130, 81, 40
        entei_r2, entei_g2, entei_b2 = 170, 113, 81

        # for raikou
        # r_x = 1399
        # r_y = 433
        r_x = 1286
        r_y = 380
        raikou_r, raikou_g, raikou_b = 170, 97, 138

        # for mamoswine
        m_x = 920
        m_y = 641
        mamo_r, mamo_g, mamo_b = 113, 73, 65
    else:
        # for repel textbox black right
        txt_x = 772
        txt_y = 574
        txt_r, txt_g, txt_b = 97, 97, 105

        # for repel textbox white
        txtw_x = 658
        txtw_y = 588
        txtw_r, txtw_g, txtw_b = 251, 251, 251

        # for entei
        e_x = 622
        e_y = 290
        entei_r, entei_g, entei_b = 130, 81, 40
        entei_r2, entei_g2, entei_b2 = 170, 113, 81

        # for raikou
        r_x = 647
        r_y = 238
        raikou_r, raikou_g, raikou_b = 170, 97, 138

        # for mamoswine
        m_x = 275
        m_y = 494
        mamo_r, mamo_g, mamo_b = 113, 73, 65


    # print('checking screen')
    pyautogui.hotkey('shift', 'print')
    time.sleep(3)
    im = Image.open(filename)
    rgb_im = im.convert('RGB')

    # r, g, b = rgb_im.getpixel((x, y))
    # print(r,g,b, x, y)


    # check textbox
    r, g, b = rgb_im.getpixel((txt_x, txt_y))
    # print(r,g,b)
    

    if txt_r == r and txt_g == g and txt_b == b:
        # print('there is a text box')
        
        # check if entei
        check_e_r, check_e_g, check_e_b = rgb_im.getpixel((e_x, e_y))
        # print(check_e_r, check_e_g, check_e_b)
        # check if raikou
        check_r_r, check_r_g, check_r_b = rgb_im.getpixel((r_x, r_y))
        # print(check_r_r, check_r_g, check_r_b)

        # check if mamo, aka in a battle
        check_mamo_r, check_mamo_g, check_mamo_b = rgb_im.getpixel((m_x, m_y))
        
        if (entei_r == check_e_r and entei_g == check_e_g and entei_b == check_e_b) or (entei_r2 == check_e_r and entei_g2 == check_e_g and entei_b2 == check_e_b):
        # if entei_r2 == check_e_r and entei_g2 == check_e_g and entei_b2 == check_e_b:

            print('entei encountered')
            if num_beasts_remaining == 2: # attack if first one, reset if second and not shiny
                attack()
            return num_beasts_remaining - 1
            # do something, will need to keep track of entei or raikou encountered
        elif raikou_r == check_r_r and raikou_g == check_r_g and raikou_b == check_r_b:
            print('raikou encountered')
            if num_beasts_remaining == 2:
                attack()
            return num_beasts_remaining - 1
            # do something, will need to keep track of entei or raikou encountered
        else:

            if mamo_r == check_mamo_r and mamo_g == check_mamo_g and mamo_b == check_mamo_b:
                print('entei/raikou not detected, but battle detected')
                return "Shiny"
            else:
                # print('need to use repel')
                use_repel()
                return num_beasts_remaining
    
    

    



def look_for_roamer(image_file, num_beasts_remaining, mode):
    # print('looking for roamer')

    wait = 6
    while wait > 0:
        # print(wait)
        pyautogui.keyDown('Up')
        time.sleep(1.3)
        pyautogui.keyUp('Up')

        pyautogui.keyDown('Down')
        time.sleep(1.3)
        pyautogui.keyUp('Down')
        wait -= 1

    time.sleep(4) # give time in case roamer is encountered at last second?
    num_beasts_remaining = determine_state(image_file, num_beasts_remaining, mode)
    
    os.remove(image_file)
    
    return num_beasts_remaining



def main():


    # sr_file = 'lapras_resets.txt'
    sr_file = 'roamer_resets.txt'

    image_file = 'starter_check.png'
    try:
        os.remove(image_file)
    except:
        pass
    reset_per_session = 0

    soft_reset_count = get_num_soft_resets(sr_file)

    mode = sys.argv[1]
    validate_mode(mode)
    
    not_shiny = True
    beasts_remaining = True
    num_beasts_remaining = 2
    start = time.time()

    

    try:
        perform_countdown(image_file)
        while not_shiny:
            menu_spam()
            burned_tower()
            navigate_to_route()

            while num_beasts_remaining != 0:
                # print(f'beasts remaining: {num_beasts_remaining}')
                num_beasts_remaining = look_for_roamer(image_file, num_beasts_remaining, mode)
                if num_beasts_remaining == 'Shiny':
                    break
            if num_beasts_remaining == 'Shiny':
                break
            else:
                print('none shiny')
                num_beasts_remaining = 2
                soft_reset_count = increment_soft_reset(soft_reset_count, False)
                reset_per_session = increment_soft_reset(reset_per_session, True)
                perform_soft_reset()
            
            # trigger_encounter()
            # not_shiny = check_starter_shiny(nonshiny_r, nonshiny_g, nonshiny_b, x, y, image_file)
        post_actions(sr_file, soft_reset_count, reset_per_session, start)
    except KeyboardInterrupt:
        post_actions(sr_file, soft_reset_count, reset_per_session, start)
        exit

main()

