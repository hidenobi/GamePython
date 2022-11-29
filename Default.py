import pygame


# size of game
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 680

# get text font and size
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font/fontText.otf", size)

pygame.init()
default_left = False
default_right = False

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Học tiếng Việt cùng bé")

# set background image
BG = pygame.image.load("assets/img/backGroundMainScreen.jpg")

# set music song
BG_MUSIC = pygame.mixer.Sound("assets/sound/BG_music.wav")
pygame.mixer.set_num_channels(3)
channel2 = pygame.mixer.Channel(2)

# status music
STATUS_MUSIC = True 

# index list
INDEX_LIST = 0

# score
SCORE = 0

# Create by Vo Huu Tuan - B20DCCN622