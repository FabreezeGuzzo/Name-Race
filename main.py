# Data In: PLayer Name, If player wants to continue or not
# Data Out: Score, Winner, Filled Spaces of Opponent(Computer), Filled Spaces of Player(name)
import random
#function used to either put the players name or opponents(computer) in a spot on the randomized list
#List simulates a dice roll
def dice_roll(name_list, user):
    die = random.randint(1, 6)
    print("you rolled a", die)
    die -= 1
    print(name_list[die])
    if name_list[die] == "empty":
        name_list[die] = user
    else:
        print("This spot has been taken")
#Function simulating a coin flip and assinging an outcome for the player and opponent(computer)
#Simulates a coin flip
def coin():
    coin_outcome = random.randint(1, 2)

    if coin_outcome == 1:
        print("You've won the coin flip, now its time to roll the die")

    else:
        print("You lost the toss, its your opponents turn")
    return coin_outcome
#Function using the other two functions(coin and dice_roll) inorder to fufill the games uses
def game():
    user_score = 0
    opponents_score = 0
# Error check
    prompt = str(input("Do you want to continue?")).lower().strip()
    while prompt != "yes" and prompt != "no":
        prompt = str(input("Do you want to continue?")).lower().strip()
    if prompt == "no":
        print("Your opponent won as a result of you forfeiting")
        opponents_score += 10
        return opponents_score
    name_of_user = str(input("Whats your name?"))
    while user_score < 10 and opponents_score < 10:
        spaces = ["empty", "empty", "empty", "empty", "empty", "empty"]
        user_spaces = 0
        opponent_spaces = 0
        end_the_round = False
        while (prompt == "yes") and (end_the_round == False):
            leftover_spaces = 0
            if coin() == 1:
                print("Its", name_of_user, "s turn")
                dice_roll(spaces, name_of_user)
            else:
                print("Its your opponents turn")
                dice_roll(spaces, "Opponents")

            for index in range(len(spaces)):
                if spaces[index] == "empty":
                    leftover_spaces += 1
            print(spaces)
#Scoring system for each round
            if leftover_spaces == 0:
                print("Round is over")
                for index in spaces:

                    if index == name_of_user:
                        user_spaces += 1
                    else:
                        opponent_spaces += 1
                print(user_spaces)
                print(opponent_spaces)
                if user_spaces > opponent_spaces:
                    user_score += 5
                    print("You Won this round: Your score:", user_score, "Opponents score:", opponents_score)
                    end_the_round = True
                elif opponent_spaces > user_spaces:
                    opponents_score += 5
                    print("Opponent Won this round: Your score:", user_score, "Opponents score:", opponents_score)
                    end_the_round = True
                else:
                    opponents_score += 1
                    user_score += 1
                    print("This round ended in a tie", "Your Score:", user_score, "Opponents Score:",
                          opponents_score)
                    end_the_round = True
            prompt = str(input("Do you want to continue?")).lower().strip()
            while prompt != "yes" and prompt != "no":
                prompt = str(input("Do you want to continue?")).lower().strip()
            if prompt == "no":
                print("Your opponent won as a result of you forfeiting")
                opponents_score += 10
                return opponents_score
#Final Outcome of the game
        if user_score > opponents_score:
            print(name_of_user, "Won the game", "Your score:", user_score)
        else:
            print("Opponent won", "Opponents score:", opponents_score)

def main():
    print(
        "Information about the game: Instead of alternating turns, a coin is flipped each time to determine who takes a turn. This rule means that one player may get multiple turns in a row, potentially achieving a win before the other play has a turn!")
    print(
        "There are 6 spots to be filled. On a player's turn they roll a 6 sided die to determine which spot they have the opportunity to write their name in. However, they can only write their name there if it is empty! They cannot overwrite the other player's name, or re-write their name if it is already there.")
    print(
        "The winner of a round is the player who has the most spots with their name in it at the end of the round. If both players have 3 spots filled, the round results in a tie.")
    print(
        "A human player can also give up after any turn. Before the game flips the coin to determine a turn, the user should be given a choice of whether another turn should be played or the game should end.")
    print(
        "A human player can also give up after any turn. Before the game flips the coin to determine a turn, the user should be given a choice of whether another turn should be played or the game should end.")
    print(
        "How to Win: Points are earned based on the outcome of a round; the first player to 10 points wins the game. At the end of a round, a tie results in each player earning 1 point; otherwise, the winner receives 5 points and the loser receives 0 points. If the human player chooses to quit, the computer player is awarded 10 points. The first player to earn at least 10 points wins the game, and the program ends at that time.")
    print(game())
    print("Thanks for playing!")


main()
