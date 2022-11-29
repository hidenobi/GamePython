import pygame
import sys
from Button import Button
import Default
import Data

CENTER_SCREEN_WIDTH = Default.SCREEN_WIDTH//2
CENTER_SCREEN_HEIGHT = Default.SCREEN_HEIGHT//2
ONE_OVER_FOUR_SCREEN_WIDTH = CENTER_SCREEN_WIDTH//2
ONE_OVER_FOUR_SCREEN_HEIGHT = CENTER_SCREEN_HEIGHT//2


# play backround music
Default.BG_MUSIC.play(loops=-1)

# print play game
def play_menu():

    # init button in menu
    BACK_BUTTON = Button(image=pygame.image.load("assets/img/close.png"), pos=(ONE_OVER_FOUR_SCREEN_WIDTH//2, CENTER_SCREEN_HEIGHT//3),
                         text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")

    while True:

        # check read all list
        if(Default.INDEX_LIST>=len(Data.LIST_DATA)):
            ketQua()

        # set background
        Default.SCREEN.blit(pygame.transform.scale(
        Default.BG, Default.SCREEN.get_size()), (0, 0))

        # render: render the text into an image with a given color
        MENU_TEXT = Default.get_font(64).render("Đây là gì", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(
        center=(CENTER_SCREEN_WIDTH, Default.SCREEN_HEIGHT//9))

        # set menu text to screen
        Default.SCREEN.blit(MENU_TEXT, MENU_RECT)

        #render score
        SCORE_TEXT = Default.get_font(52).render(
        "Điểm: {}".format(Default.SCORE), True, "#b68f40")
        SCORE_RECT = SCORE_TEXT.get_rect(
            center=(7*ONE_OVER_FOUR_SCREEN_WIDTH//2, Default.SCREEN_HEIGHT//9))
        Default.SCREEN.blit(SCORE_TEXT,SCORE_RECT)

        # get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # set button to screen
        for button in [BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(Default.SCREEN)

        THE_QUESTION = Data.LIST_DATA[Default.INDEX_LIST]
        THE_QUESTION_IMAGE = Button(image=pygame.image.load(THE_QUESTION[0]), pos=(CENTER_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT),
                                    text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White").update(Default.SCREEN)
        THE_ANSWER_1 = Button(image=pygame.transform.scale(pygame.image.load("assets/img/BG_white.jpg"), (120, 40)), pos=(CENTER_SCREEN_WIDTH-200, 7*ONE_OVER_FOUR_SCREEN_HEIGHT//2),
                              text_input=THE_QUESTION[1], font=Default.get_font(36), base_color="#b68f40", hovering_color="Black")
        THE_ANSWER_2 = Button(image=pygame.transform.scale(pygame.image.load("assets/img/BG_white.jpg"), (120, 40)), pos=(CENTER_SCREEN_WIDTH, 7*ONE_OVER_FOUR_SCREEN_HEIGHT//2),
                              text_input=THE_QUESTION[2], font=Default.get_font(36), base_color="#b68f40", hovering_color="Black")
        THE_ANSWER_3 = Button(image=pygame.transform.scale(pygame.image.load("assets/img/BG_white.jpg"), (120, 40)), pos=(CENTER_SCREEN_WIDTH+200, 7*ONE_OVER_FOUR_SCREEN_HEIGHT//2),
                              text_input=THE_QUESTION[3], font=Default.get_font(36), base_color="#b68f40", hovering_color="Black")

        for button in [THE_ANSWER_1, THE_ANSWER_2, THE_ANSWER_3]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(Default.SCREEN)
        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Back to menu")
                    main_menu()
                    break
                if THE_ANSWER_1.checkForInput(MENU_MOUSE_POS):
                    print("Click the answer 1")
                    clickTrue()
                    break
                if THE_ANSWER_2.checkForInput(MENU_MOUSE_POS):
                    print("Click the answer 2")
                    clickFalse()
                    break
                if THE_ANSWER_3.checkForInput(MENU_MOUSE_POS):
                    print("Click the answer 3")
                    clickFalse()
                    break
        pygame.display.update()

# print settings
def options():
    # render: render the text into an image with a given color
    MENU_TEXT = Default.get_font(64).render("Cài đặt", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(
        center=(CENTER_SCREEN_WIDTH, Default.SCREEN_HEIGHT//5))

    # init button in menu
    MUSIC_ON_BUTTON = Button(image=pygame.image.load("assets/img/music_on.png"), pos=(3*ONE_OVER_FOUR_SCREEN_WIDTH, 3*ONE_OVER_FOUR_SCREEN_HEIGHT),
                             text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")
    MUSIC_OFF_BUTTON = Button(image=pygame.image.load("assets/img/music_off.png"), pos=(ONE_OVER_FOUR_SCREEN_WIDTH, 3*ONE_OVER_FOUR_SCREEN_HEIGHT),
                              text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")
    BACK_BUTTON = Button(image=pygame.image.load("assets/img/close.png"), pos=(ONE_OVER_FOUR_SCREEN_WIDTH//2, CENTER_SCREEN_HEIGHT//3),
                         text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")

    # set background
    Default.SCREEN.blit(pygame.transform.scale(
        Default.BG, Default.SCREEN.get_size()), (0, 0))

    # set menu text to screen
    Default.SCREEN.blit(MENU_TEXT, MENU_RECT)

    while True:
        # get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # set button to screen
        for button in [MUSIC_ON_BUTTON, MUSIC_OFF_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(Default.SCREEN)

        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MUSIC_ON_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Music On")
                    musicOn()
                    break
                if MUSIC_OFF_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Music Off")
                    musicOff()
                    break
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Back to menu")
                    main_menu()
                    break
        pygame.display.update()

# print main menu
def main_menu():

    # set background
    Default.SCREEN.blit(pygame.transform.scale(
        Default.BG, Default.SCREEN.get_size()), (0, 0))
    # set menu text
    # render: render the text into an image with a given color
    SETTINGS_TEXT = Default.get_font(64).render(
        "Học tiếng Việt cùng bé", True, "#b68f40")
    SETTINGS_RECT = SETTINGS_TEXT.get_rect(
        center=(CENTER_SCREEN_WIDTH, Default.SCREEN_HEIGHT//5))
    # init button in menu
    PLAY_BUTTON = Button(image=pygame.image.load("assets/img/play.png"), pos=(CENTER_SCREEN_WIDTH+150, 3*ONE_OVER_FOUR_SCREEN_HEIGHT),
                         text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")
    OPTIONS_BUTTON = Button(image=pygame.image.load("assets/img/settings.png"), pos=(CENTER_SCREEN_WIDTH, 3*ONE_OVER_FOUR_SCREEN_HEIGHT),
                            text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/img/exit.png"), pos=(CENTER_SCREEN_WIDTH-150, 3*ONE_OVER_FOUR_SCREEN_HEIGHT),
                         text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")

    # set menu text to screen
    Default.SCREEN.blit(SETTINGS_TEXT, SETTINGS_RECT)

    while True:
        # get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # set button to screen
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(Default.SCREEN)

        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Play Game")
                    play_menu()
                    break
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Open options")
                    options()
                    break
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Exit Game")
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

# print answer screen
def ketQua():
     # set background
    Default.SCREEN.blit(pygame.transform.scale(
    Default.BG, Default.SCREEN.get_size()), (0, 0))

    # render: render the text into an image with a given color
    MENU_TEXT = Default.get_font(64).render("Chúc mừng bé đã hoàn thành trò chơi", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(
    center=(CENTER_SCREEN_WIDTH, Default.SCREEN_HEIGHT//9))

    # set menu text to screen
    Default.SCREEN.blit(MENU_TEXT, MENU_RECT)

    #render score
    SCORE_TEXT = Default.get_font(52).render(
    "Điểm: {}".format(Default.SCORE), True, "#b68f40")
    SCORE_RECT = SCORE_TEXT.get_rect(
        center=(CENTER_SCREEN_WIDTH, CENTER_SCREEN_HEIGHT))
    Default.SCREEN.blit(SCORE_TEXT,SCORE_RECT)

    # init button in menu
    BACK_BUTTON = Button(image=pygame.image.load("assets/img/close.png"), pos=(ONE_OVER_FOUR_SCREEN_WIDTH//2, CENTER_SCREEN_HEIGHT//3),
                         text_input="", font=Default.get_font(16), base_color="#d7fcd4", hovering_color="White")

    while True:
        

        # get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # set button to screen
        for button in [BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(Default.SCREEN)
        # check for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("Back to menu")
                    Default.INDEX_LIST = 0
                    Default.SCORE = 0
                    main_menu()
                    break
        pygame.display.update()

# turn on music
def musicOn():
    if (Default.STATUS_MUSIC == False):
        Default.STATUS_MUSIC = True
        Default.BG_MUSIC.play(loops=-1)

#turn off music
def musicOff():
    if (Default.STATUS_MUSIC == True):
        Default.STATUS_MUSIC = False
        Default.BG_MUSIC.stop()

def clickUp():
    if(Default.INDEX_LIST<len(Data.LIST_DATA)):
        Default.INDEX_LIST+=1
def clickTrue():
    clickUp()
    Default.SCORE += 10
def clickFalse():
    clickUp()    


# Create by Vo Huu Tuan - B20DCCN622
