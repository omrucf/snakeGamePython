# importing libraries
import pygame as pg
import time
import random as rand
import menu

speed = 15

# Window size
SW = 500
SH = 500

# defining colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brown = (165, 42, 42)

# Initialising pg
pg.init()

# Initialise game window
pg.display.set_caption("Snake")
pg.display.set_icon(pg.image.load("Snake/icons/mainIcon.png"))
screen = pg.display.set_mode((SH, SW))

# FPS (frames per second) controller
fps = pg.time.Clock()

# defining snake default position
snakePos = [100, 50]

# defining first 4 blocks of snake body
body = [[100, 50], [90, 50], [80, 50], [70, 50]]
# fruit position
fruitPos = [rand.randrange(1, (SW // 10)) * 10, rand.randrange(1, (SH // 10)) * 10]

fruitSpawn = True

# setting default snake drct towards
# right
drct = "R"
chngDrct = drct

# initial score
Score = 0


# displaying Score function
def score(font, color, size, Score, boarders):
    # creating font object Font
    Font = pg.font.SysFont(font, size)

    # create the display surface object
    # scoreDisplay
    scoreDisplay = Font.render("Score : " + str(Score), True, color)

    # create a rectangular object for the text
    # surface object
    scoreTextBox = scoreDisplay.get_rect()
    if boarders:
        scoreTextBox.midtop = (54, 7)

    # displaying text
    screen.blit(scoreDisplay, scoreTextBox)


# game over function
def endGame(font, color, size, Score, boarders):
    # creating font object Font
    Font = pg.font.SysFont(font, size)

    # creating a text surface on which text
    # will be drawn
    displayedText = Font.render("Your Score is : " + str(Score), True, color)

    # create a rectangular object for the text
    # surface object
    textBox = displayedText.get_rect()

    # setting position of the text
    textBox.midtop = (SW / 2, SH / 4)

    # blit will draw the text on screen
    screen.blit(displayedText, textBox)
    pg.display.flip()

    # after 2 seconds we will quit the program
    time.sleep(2)

    menu.Menu(boarders)


def setBoarders(flag):
    boarders = flag


def getChngDrct():
    return chngDrct


def getDrct():
    return drct


def getSnakePos():
    return snakePos


def getBody():
    return body


def getFruitPos():
    return fruitPos


def getFruitSpawn():
    return fruitSpawn


def getScore():
    return Score



# Main Function
def game(chngDrct, drct, snakePos, body, fruitPos, fruitSpawn, Score, boarders):
    snakePos = [100, 50]

    # defining first 4 blocks of snake body
    body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    
    Boarders = [[0, 0], [0, 500], [500, 0], [500, 500]]

    Score = 0

    # handling key events
    while True:
        
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP or event.key == pg.K_w:
                    chngDrct = "U"
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    chngDrct = "D"
                elif event.key == pg.K_LEFT or event.key == pg.K_a:
                    chngDrct = "L"
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    chngDrct = "R"
            elif event.type == pg.QUIT:
                pg.quit()
                quit()

        # If two keys pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        # Moving the snake
        if chngDrct == "U" and drct != "D":
            drct = "U"
            snakePos[1] -= 10
        elif chngDrct == "U" and drct == "D":
            drct = "D"
            snakePos[1] += 10
        elif chngDrct == "D" and drct != "U":
            drct = "D"
            snakePos[1] += 10
        elif chngDrct == "D" and drct == "U":
            drct = "U"
            snakePos[1] -= 10
        elif chngDrct == "L" and drct != "R":
            drct = "L"
            snakePos[0] -= 10
        elif chngDrct == "L" and drct == "R":
            drct = "R"
            snakePos[0] += 10
        elif chngDrct == "R" and drct != "L":
            drct = "R"
            snakePos[0] += 10
        elif chngDrct == "R" and drct == "L":
            drct = "L"
            snakePos[0] -= 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        body.insert(0, list(snakePos))
        if snakePos[0] == fruitPos[0] and snakePos[1] == fruitPos[1]:
            Score += 10
            fruitSpawn = False
        else:
            body.pop()

        if not fruitSpawn:
            fruitPos = [
                rand.randrange(1, (SW // 10)) * 10,
                rand.randrange(1, (SH // 10)) * 10,
            ]

        fruitSpawn = True
        screen.fill(black)

        if boarders:
            # drawing boarders
            pg.draw.rect(screen, brown, pg.Rect(0, 0, SW, 10))
            pg.draw.rect(screen, brown, pg.Rect(0, 0, 10, SH))
            pg.draw.rect(screen, brown, pg.Rect(0, SH - 10, SW, 10))
            pg.draw.rect(screen, brown, pg.Rect(SW - 10, 0, 10, SH))
        # drawing snake
        pg.draw.rect(screen, red, pg.Rect(body[0][0], body[0][1], 10, 10))
        for pos in range(1, len(body)):
            pg.draw.rect(screen, green, pg.Rect(body[pos][0], body[pos][1], 10, 10))
        pg.draw.rect(screen, white, pg.Rect(fruitPos[0], fruitPos[1], 10, 10))

        # Game Over conditions
        if snakePos[0] < 20:
            if boarders:
                endGame("Chalkboard", red, 20, Score, boarders)
            elif snakePos[0] < 0:
                snakePos[0] = SW - 10
        elif snakePos[0] > SW - 30:
            if boarders:
                endGame("Chalkboard", red, 20, Score, boarders)
            elif snakePos[0] > SW - 10:
                snakePos[0] = 0
        elif snakePos[1] < 20:
            if boarders:
                endGame("Chalkboard", red, 20, Score, boarders)
            elif snakePos[1] < 0:
                snakePos[1] = SH - 10
        elif snakePos[1] > SH - 30:
            if boarders:
                endGame("Chalkboard", red, 20, Score, boarders)
            elif snakePos[1] > SH - 10:
                snakePos[1] = 0

        # Touching the snake body
        for block in body[1:]:
            if snakePos[0] == block[0] and snakePos[1] == block[1]:
                endGame("Chalkboard", red, 20, Score, boarders)
        # displaying score continuously
        score("Chalkboard", white, 20, Score, boarders)

        # Refresh game screen
        pg.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(speed)

