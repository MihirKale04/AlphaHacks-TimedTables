import time
import pygame
from math_class import Math
math = Math()


def main():
    pygame.init()
    pygame.display.set_caption("minimal program")
    win = pygame.display.set_mode((500, 500))

    # initialize questions
    myfont = pygame.font.SysFont('Ariel', 50)
    myfont2 = pygame.font.SysFont('Ariel', 25)
    num1 = math.getnums()[0]
    num2 = math.getnums()[1]
    question = str(num1) + " X " + str(num2)+" =  ?"

    # initialize vars
    active = True
    text = ''
    correct = 0
    wrong = 0
    scene = "game"
    skipcalc = False
    barlength = 0
    startTime = pygame.time.get_ticks()
    bestTime = ""
    FirstRun = True
    run = True
    barlength2 = 0
    bartimestart = False
    barcount = 0

    def barupdate():
        barlength2 += 1.5

    while run:
        win.fill((0, 0, 0))
        # game scene
        if scene == "game":
            # set percent calc on
            skipcalc = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            if text.isnumeric():
                                if int(text) == num1*num2:
                                    correct += 1
                                    barlength += 15
                                else:
                                    wrong += 1
                                num1 = math.getnums()[0]
                                num2 = math.getnums()[1]
                                question = str(num1) + " X " + str(num2)+" = ?"
                                textsurface = myfont.render(
                                    question, False, (250, 250, 250))
                            else:
                                print("invalid input")
                            text = ''

                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            if correct == 10:
                scene = "end"
                # time of round
                totaltime = pygame.time.get_ticks()-startTime
                FirstRun = False
            if not FirstRun:
                # bartimecomp
                if not bartimestart:
                    barStart = time.time()
                    bartimestart = True

                if bartimestart and bestTime != "" and barcount <= 100:
                    if time.time() - barStart > (int(bestTime)/1000)/100:
                        barlength2 += 1.5
                        barcount += 1
                        bartimestart = False

                # competing rect
                pygame.draw.rect(win, (250, 0, 0), [30, 100, 20, 150])
                pygame.draw.rect(win, (0, 250, 0), [
                    30, 251-barlength2, 20, barlength2])

                # best bar text
                BestLabel = myfont2.render(
                    "Best", False, (250, 250, 250))
                win.blit(BestLabel, (20, 70))

            # your bar text
            currentLabel = myfont2.render(
                "Pogress", False, (250, 250, 250))
            win.blit(currentLabel, (410, 70))
            # pogress rect
            pygame.draw.rect(win, (250, 0, 0), [450, 100, 20, 150])
            pygame.draw.rect(win, (0, 250, 0), [
                             450, 251-barlength, 20, barlength])

            # wrong text
            wrongLabel = myfont.render(
                "Wrong: "+str(wrong), False, (250, 250, 250))
            win.blit(wrongLabel, (50, 400))
            # correct text
            correctLabel = myfont.render(
                "Correct: "+str(correct), False, (250, 250, 250))
            win.blit(correctLabel, (290, 400))
            # anwser text
            font = pygame.font.Font(None, 32)
            input_box = pygame.Rect(250, 270, 100, 32)
            anwser = font.render(text, True, (250, 250, 0))
            width = max(100, anwser.get_width()+10)
            input_box.w = width
            input_box = pygame.Rect(250-(input_box.w)/2, 270, input_box.w, 32)
            win.blit(anwser, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(win, (250, 250, 250), input_box, 2)
            # question text
            textsurface = myfont.render(question, False, (250, 250, 250))
            win.blit(textsurface, (250-(textsurface.get_width())/2, 150))
        # end scene
        if scene == "end":
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if the mouse is clicked on the
                    # button the game is terminated
                    if 150 <= mouse[0] <= 350 and 225 <= mouse[1] <= 325:
                        # reset vars
                        active = True
                        skipcalc = True
                        barlength = 0
                        text = ''
                        correct = 0
                        wrong = 0
                        scene = "game"
                        total = 0
                        percent = 0
                        startTime = pygame.time.get_ticks()
                        barlength2 = 0
                        barcount = 0
            # update best time
            if bestTime == "":
                bestTime = totaltime
            elif bestTime > totaltime:
                bestTime = totaltime

            # button changes collor on hover
            if 150 <= mouse[0] <= 350 and 225 <= mouse[1] <= 325:
                pygame.draw.rect(win, (250, 250, 170), [150, 225, 200, 100])

            else:
                pygame.draw.rect(win, (100, 100, 100), [150, 225, 200, 100])

            # correct text
            correctLabel = myfont.render(
                "Correct: "+str(correct), False, (250, 250, 250))
            win.blit(correctLabel, (290, 400))
            # wrong text
            wrongLabel = myfont.render(
                "Wrong: "+str(wrong), False, (250, 250, 250))
            win.blit(wrongLabel, (50, 400))
            # % correct
            if not skipcalc:
                total = correct + wrong
                percent = round((correct/total)*100, 2)
            # accuracy text
            accLabel = myfont.render(
                "You got " + str(percent) + "%  correct ", False, (250, 250, 250))
            win.blit(accLabel, (250-(accLabel.get_width()/2), 150))
            # button text
            smallfont = pygame.font.SysFont('Corbel', 35)
            buttontext = smallfont.render('PLAY AGAIN', True, (0, 0, 0))
            win.blit(buttontext, (250-(buttontext.get_width()/2), 260))
            # time text
            timetext = myfont.render(
                'Current time: '+str(round(totaltime/1000, 1))+" seconds", False, (250, 250, 250))
            win.blit(timetext, (250-(timetext.get_width()/2), 50))
            # best time text
            besttimetext = myfont.render(
                'Best time: '+str(round(bestTime/1000, 1))+" seconds", False, (250, 250, 250))
            win.blit(besttimetext, (250-(besttimetext.get_width()/2), 100))
        pygame.display.update()


main()
