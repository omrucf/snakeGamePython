import pygame as pg
import menu

pg.init()

screen = pg.display.set_mode((500, 500))
pg.display.set_caption("Snake")
pg.display.set_icon(pg.image.load("Snake/icons/mainIcon.png"))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

font = "Chalkboard"
size = 15
color = black

Boarder = pg.Rect(100, 100, 300, 50)

screen.fill(black)


def BoarderIsClicked(boarder):
    if boarder:
        bgcol = red
        txtcol = black
        boarder = False
        text = "die when you hit the boarder"
    else:
        bgcol = green
        txtcol = white
        boarder = True
        text = "don't die when you hit the boarder"
    pg.draw.rect(screen, bgcol, Boarder)
    displayedText_1 = pg.font.SysFont(font, size).render(text, True, color)
    textBox_1 = displayedText_1.get_rect()
    textBox_1.center = (250, 125)
    screen.blit(displayedText_1, textBox_1)

    return boarder


def Options(boarder):
    boarder = BoarderIsClicked(not boarder)
    pg.draw.rect(screen, white, (100, 200, 300, 50))
    displayedText_2 = pg.font.SysFont(font, size).render("Back to menu", True, color)
    textBox_2 = displayedText_2.get_rect()
    textBox_2.center = (250, 225)
    screen.blit(displayedText_2, textBox_2)
    pg.draw.rect(screen, white, (100, 300, 300, 50))
    displayedText_3 = pg.font.SysFont(font, size).render("Quit", True, color)
    textBox_3 = displayedText_3.get_rect()
    textBox_3.center = (250, 325)
    screen.blit(displayedText_3, textBox_3)

    while True:
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pg.mouse.get_pos()
                    if pos[0] >= 100 and pos[0] <= 400:
                        if pos[1] >= 100 and pos[1] <= 150:
                            boarder = BoarderIsClicked(boarder)
                        elif pos[1] >= 200 and pos[1] <= 250:
                            menu.Menu(boarder)
                        elif pos[1] >= 300 and pos[1] <= 350:
                            pg.quit()
                            quit()
