import pygame, sys
import time
import random  # so I can wait a random length of time


class Person:  # class for the people taking the test
    def __init__(self, name, age, gender):
        self.age = age
        self.gender = gender
        self.name = name

        self.scores = []
        self.average_score = None


class ReactionTime:   # test for reaction and also data analysis

    @staticmethod
    def reaction_time_test(participant: Person):  # make it so they have to input a Person as the participant (also scores will only count if the person completes all 5 reaction tests)

        goes_for_average = 5

        scores = []  # track each time it takes for person to react

        pygame.init()  # initialising

        green = (0, 205, 0)  # rgb values for green background
        red = (130, 0, 0)  # rgb values for red background
        blue = (8, 96, 168)  # rgb values for blue
        white = (255, 255, 255)  # rgb value for white

        # Setting Values

        screen = pygame.display.set_mode((1920, 1020))  # set size of the screen and make a screen object
        pygame.display.set_caption("Reaction Time Test")  # set caption for the game
        my_font = pygame.font.SysFont('comicsansms', 60)  # large font
        font2 = pygame.font.SysFont('comicsansms', 10)  # smaller version of other font
        font3 = pygame.font.SysFont('comicsansms', 25)  # medium size font
        font4 = pygame.font.SysFont('comicsansms', 15)  # small / medium size font

        # Making variables for colours

        black = (0, 0, 0)  # rgb values for black
        green = (0, 205, 0)  # rgb values for green background
        red = (130, 0, 0)  # rgb values for red background
        blue = (8, 96, 168)  # rgb values for blue
        white = (255, 255, 255)  # rgb value for white

        def turn():  # function to have the user take a turn the append that value to scores

            # Making the waiting screen for before screen turns green
            screen.fill(red)
            text = my_font.render("Left-Click When The Background Turns Green", True, white)
            screen.blit(text, (270, 212))
            pygame.display.update()

            # Picking the amount of time to wait for and doing that while still allowing the program to be closed
            delay = random.randint(1000, 7000)  # / 1000 to make it have a decimal so its not 1, 2, 3 if did random between 1, 7 without dividing  (this waits a random time between 1 and 7 seconds)
            time_delayed = 0
            while time_delayed < delay:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # give option to quit
                        sys.exit()
                time.sleep(0.001)
                time_delayed += 1

            # Making the screen for the green
            screen.fill(green)
            text = my_font.render("Click!", True, white)
            screen.blit(text, (850, 400))
            pygame.display.update()

            # Tracking how long until left_click is pressed

            left_click_pressed = False
            time_taken = 0    # in milliseconds

            while left_click_pressed is False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # give option to quit
                        sys.exit()

                if pygame.mouse.get_pressed(3)[0] is True:
                    left_click_pressed = True

                time.sleep(0.001)
                time_taken += 1

            scores.append(time_taken)

            # Make screen blue and tell them how long they took to react and then ask them to continue by pressing left-click

            #   if len(scores) != goes_for_average:  # on the 5th one I want it to skip straight to the average  ( un comment and tab to switch back
            screen.fill(blue)
            text = my_font.render(str(time_taken) + ' ms', True, white)
            text2 = font2.render("Click to continue", True, white)
            screen.blit(text, (845, 400))
            screen.blit(text2, (900, 520))
            pygame.display.update()

            continue_button_clicked = False

            while pygame.mouse.get_pressed(3)[0] is True:   # delay until mouse is released so it doesn't just go onto the next one straight away (it would do this because the mouse would be pressed after the green and it needs to be released and pressed again to continue)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # give option to quit
                        sys.exit()
                time.sleep(0.001)

            # ask the person to press left click to continue
            while not continue_button_clicked:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # give option to quit
                        sys.exit()
                if pygame.mouse.get_pressed(3)[0] is True:
                    continue_button_clicked = True

        def display_average(lst):

            # calc average

            total = 0
            for value in lst:
                total += value

            average = round(total / len(scores))

            # display average on the screen

            screen.fill(white)
            text = font3.render("Your average reaction time was " + str(average) + ' ms', True, black)
            text2 = font4.render("click to exit", True, black)
            screen.blit(text, (700, 400))
            screen.blit(text2, (900, 520))
            pygame.display.update()

            # click to end option

            end_button_clicked = False

            while pygame.mouse.get_pressed(3)[0] is True:  # delay until mouse is released so it doesn't just go onto the next one straight away (it would do this because the mouse would be pressed after the green and it needs to be released and pressed again to continue)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # give option to quit
                        sys.exit()
                time.sleep(0.001)

            # ask the person to press left click to continue
            while not end_button_clicked:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # give option to quit
                        sys.exit()
                if pygame.mouse.get_pressed(3)[0] is True:
                    end_button_clicked = True

            return average  # return average so it can be given to the person

        # GAME LOOP

        running = True  # running variable to make it so to stop the game I don't have to sys.exit()
        while len(scores) <= goes_for_average and running:  # make 5 goes happen then stop the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # give option to quit
                    running = False
            if len(scores) < goes_for_average:
                turn()
            else:

                # add values to participant
                participant.scores = scores
                participant.average_score = display_average(scores)

                # end the test
                running = False


# Example of how to use this

joe = Person("Joe", 23, "Male")

s = ReactionTime()

s.reaction_time_test(joe)

print(joe.scores, joe.average_score)


