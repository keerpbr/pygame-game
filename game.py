import pygame
import time

# Init
pygame.init()

# Display settings
display_width = 800
display_height = 600

# RGB
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# Car width
car_width = 117;

# Display
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Jogo de teste')
clock = pygame.time.Clock()

# Loading the car sprite
carImg = pygame.image.load('carSprite.png')


def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text, repeat):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	if repeat == True:
		pygame.display.update()
		time.sleep(2)
		game_loop()
	else:
		pygame.display.update()
		time.sleep(1)

def crash():
	message_display("Você bateu.", True)
def game_loop():

	# Setting X & Y coordinates.
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    # Use to move the car
    x_change = 0

    gameExit = False
    oneTimeSay = True
    
    welcome = "Hello. This is a game developed with Python and Pygame."
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                py.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                	message_display("Oi", False)
            if oneTimeSay:
            	print(welcome)
            	oneTimeSay = False

        x += x_change

        # Setting the background color to white
        gameDisplay.fill(white)
        # Spawning the car in the X & Y coordinates
        car(x,y)

        if x > display_width - car_width or x < 0:
            crash()
        
        pygame.display.update()
        clock.tick(60)
        
game_loop()
pygame.quit()
quit()
