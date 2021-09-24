"""A "buzzfeed style" quiz to determine which My Hero Academia character you are for my open ended programming project 00."""

from random import randint
player: str = "Player01"
points: int = 100
hero_score: int = 100
answer_choice: int = 100


ORANGES: str = "\U0001F34A"
OKRA_SORT_OF: str = "\U0001F966"
APPLE: str = "\U0001F34E"


def greet(player):
    # This is a function to greet the player and initialize the adventure.
    player = input("Enter your name, player! \n")
    print("")
    print(f"Welcome {player}!")
    return player

 
def hero_mentor(mentor_num):
    mentor_num = int(input("Enter a Number between 1 and 3 to select your mentor. "))
    print("Hero Score: ", hero_score)

    if mentor_num == 1:
        print("Hero Score: ", hero_score)
        print(f"Congratulations {player}! Your hero mentor is 'Endeavor', the Flame Hero")
        print("With the explosive power from his quirk 'Hellflame', Endeavor has forced his way into the number 2 hero spot in the world! He will be a great mentor.")
        mentor_num = 0
        mentor_num += 5
        print("Hero Score: ", hero_score)
        return mentor_num
    elif mentor_num == 2:
        print(f"Congratulations {player}! Your hero mentor is 'Snipe', the Homing Hero")
        print("Snipe is a great offensive mentor. His quirk allows him to make any projectile he launches chase a target for up to 600 m. He will be a good mentor.")
        mentor_num = 0
        mentor_num += 3
        return mentor_num
    elif mentor_num == 3:
        print(f"Congratulations {player}! Your hero mentor is 'Ectoplasm', the Cloning Hero")
        print("Ectoplasm is a very technical mentor. His quirk allows him to make up to 30 clones of himself at once! He will be a great mentor for training many-on-one scenarios.")
        mentor_num = 0
        mentor_num += 4
        return mentor_num
    else:
        print("Invalid Input, Try Again.")


def question_one(answer_choice, points, hero_score, player):
    # The first question of the quiz.  

    points = 0

    print("Scenario: It's your hero school entrance exam.")
    print("This is the physical exam to determine whether or not you will be accepted into the prestiges UA Academy, your dream school.")
    print("You and your fellow UA applicants have been tasked with fending off a horde of evil robots, that are attacking a mock city, using your unique quirks.")
    print("The robots are worth different numbers of points depending on how tough they are, and you get points deducted for unnecessary destruction of the city.")

    print("Halfway through your exam, you are kicking evil robot booty and doing well on points when you see a fellow hero trainee get knocked to the ground by a seriously large robot!")
    print("The robot then targets the stunned hero traineee with its terrifying lazer vision.")
    print("Nobody around seems to see what is about to happen, what do you do? ")

    print("\n1) Charge the monstrous metal maurader! You are a hero, heroes help the weak! ")
    print("2) Your quirk is perfect for this moment, you get the trainee to safety without getting shot by lasers! It may not be worth any points but it's what a real hero would do!")
    print("3) No one is watching and that's your competition on the ground...you give the robot a little help...")

    answer_choice = int(input("Make your choice: "))

    if answer_choice == 1:
        answer_choice == 0
        points += 10
        question_two(answer_choice, points, hero_score, player)
    elif answer_choice == 2:
        answer_choice == 0
        points += 20
        question_two(answer_choice, points, hero_score, player)
    elif answer_choice == 3:
        answer_choice == 0
        points -= 10
        villian_path()
    else:
        print("Improper value entered. Play again.")


def question_two(answer_choice, points, hero_score, player):
    # The second question of the quiz.
    print("\nCongratulations! Due to your bravery, you have been accepted into UA! After meeting all of your teachers, who is your role model hero?")

    print("\n1) 'Thirteen' the Rescue Training Specialist. This astronaught suit wearing hero can create blackholes out of her finger tips.")
    print("As destructive as this power would be in the wrong hands, no pun intended, Thirteen is famous for saving lives by keeping villians, projectiles, and debris away from civilians during times of emergency.")

    print("2) 'All Might' the Heroics Teacher. The number one hero in the world the most lives saved! All might uses his strength to overwhelm villians of any size at any time of the day or night.")

    print("3, 'Eraser Head' Your Home Room Teacher. Eraser Head can disable a villians quirk just by looking at them!")
    print("The effect lasts until he blinks. Along with his advanced martial arts ability, Eraser Head can shut down most any foe in one on one combat!") 

    answer_choice = int(input("Make your choice! "))

    if answer_choice == 1:
        answer_choice == 0
        points += 15
        question_three(answer_choice, points, hero_score, player)
    elif answer_choice == 2:
        answer_choice == 0
        points += 10
        question_three(answer_choice, points, hero_score, player)
    elif answer_choice == 3:
        answer_choice == 0
        points += 20
        question_three(answer_choice, points, hero_score, player)
    else:
        print("Improper value entered. Play again.")

    
def question_three(answer_choice, points, hero_score, player):
    # The third question of the quiz.
    print("\nLast Question: What food do you like the most?")

    print("\n1) Oranges. ", ORANGES)
    print("2) Okra. ", OKRA_SORT_OF)
    print("3) Apples. ", APPLE)

    answer_choice = int(input("Make your choice! "))

    if answer_choice == 1:
        answer_choice == 0
        points += 10
        results(answer_choice, points, hero_score, player)
    elif answer_choice == 2:
        answer_choice == 0
        points += 15
        results(answer_choice, points, hero_score, player)
    elif answer_choice == 3:
        answer_choice == 0
        points += 20
        results(answer_choice, points, hero_score, player)
    else:
        print("Improper value entered. Play again.")


def results(answer_choice, points, hero_score, player):
    # This function gives the players their results.
    courage: int = randint(1, 10)
    points += courage
    print("Hero Score: ", hero_score)

    if points <= 44:
        print(f"\nCongratulations {player}! You gained { courage } extra hero points for your courage and { hero_score } extra hero points from training with your mentor.")
        print(f"Your Hero score is { points }, you are defensive hero.")
        print("You got 'Cellophane', the Taping Hero!")
        print("His quirk is the ability to shoot tape from the dispensers in his elbows, his specialty is restraining villians and locking down areas with tape traps.")
        print("You may lack offensive capabilities but your usefullness in missions is only limited by your ability to come up with a plan. The sky is the limit with this grade A hero!")
    elif points >= 50:
        print(f"\nCongratulations {player}! You gained { courage } extra hero points for your courage and { hero_score } extra hero points from training with your mentor.")
        print(f"Your Hero score is { points }, you are well rounded hero!.")
        print("You got 'Jet Black', the Dark Shadow Hero!")
        print("With the body of a  man and the head of a raven, his quirk is the ability to control ""Dark Shadow"" a shadow beast that lives within him, the beast is a powerful offensive and defensive companion.")
        print("Dark Shadow may be strong but he can be weakened by bright light and if he is drawn out in the presence of the moon he is to strong for Jet Black to control!") 
    else:
        print(f"\nCongratulations {player}! You gained { courage } extra hero points for your courage and { hero_score } extra hero points from training with your mentor.")
        print(f"Your hero score is {points}, you are an offensive hero.")
        print("You got 'Pinky', the acid hero!")
        print("The name says it all, Pinky is instrumental on the battlefield. Her acid allows her to take out foes and melt through any obstacles in her teams way!")


def villian_path():
    # End the game, player is a villian.
    print("You are no hero! Evil will never previal!")
    print(f"Your hero score is { points }, your status is 'Villian'.")
    hero_score == 0
    exit()


def main() -> None:
    global points
    global hero_score
    global answer_choice
    global player

    points = 0
    hero_score = 0
    answer_choice = 0
    game_loop: int = 0

    player = greet(player)

    print("Enter '1' to take a quiz to find out which My Hero Academia character you are most like!")
    print("or")
    print("Enter '2' to randomly select a Hero Mentor for bonus points to your Hero Score!")

    procedure_or_function = int(input("Enter 1 or 2: "))
    mentor_num: int = 0

    if procedure_or_function == 1:

        question_one(answer_choice, points, hero_score, player)

        print("Try again?")
        print("1) Yes.")
        print("2) No.")

        while game_loop != 3:

            game_loop = int(input("Enter 1 or 2: "))

            if game_loop == 1:
                question_one(answer_choice, points, hero_score, player)

                print("Try again?")
                print("1) Yes.")
                print("2) No.")

            elif game_loop == 2:
                print("Would you like to pick a new mentor?")
                print("1) Yes.")
                print("2) No.")

                game_loop_2: int = int(input("Enter 1 or 2: "))

                if game_loop_2 == 1:

                    hero_score += hero_mentor(mentor_num)
                elif game_loop_2 == 2:
                    print("Thank you for your time.")
                    game_loop += 1
                else:
                    print("Invalid input, try again.")
            else:
                print("Invalid input, try again.")
        print("End")

    elif procedure_or_function == 2:
        print("Hero Score: ", hero_score)

        hero_score += hero_mentor(mentor_num)
        print("Hero Score: ", hero_score)

        print("Would you like to take the Hero Quiz now?")
        print("1) Yes.")
        print("2) No.")

        while game_loop != 3:
            game_loop = int(input("Enter 1 or 2: "))

            if game_loop == 1:
                print("Hero Score: ", hero_score)
                question_one(answer_choice, points, hero_score, player)
                print("Hero Score: ", hero_score)

                print("Try again?")
                print("1) Yes.")
                print("2) No.")

            elif game_loop == 2:

                choice_mentor_two: int = 0

                print("Would you like to pick a different mentor or exit the quiz?")
                print("1) Pick a new mentor")
                print("2) Exit the quiz")

                choice_mentor_two = int(input("Enter 1 or 2: "))

                if choice_mentor_two == 1:
                    
                    hero_score += hero_mentor(mentor_num)

                    print("Would you like to take the Hero Quiz now?")
                    print("1) Yes.")
                    print("2) No.")

                elif choice_mentor_two == 2:
                    print("Thank you for your time.")
                    game_loop += 1
                            
            else:
                print("Invalid Entry. Try Again.")
                print("Thank you for your time.")

    
if __name__ == "__main__":
    main()