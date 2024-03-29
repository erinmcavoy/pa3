# Programmers:  [Erin McAvoy]
# Course:  CS151.05, Dr. Isaacman
# Date: [10/8/19]
# Programming Assignment:  [PA3]
# Problem Statement:  [calculates the score of a quiddich game, calculates qb rating, calculates gymnast score]
# Data In: [completions, attempts, passing yards, touchdown passes, interceptions, number of goals, snitch catch, difficulty score, execution scores]
# Data Out:  [perfect passer or not perfect passer, quiddich score, final score]

# Main Function Defined
def main():
    # QB Rating
    print("This program will tell you if the QB is a perfect passer.")
    completions = int(input("Enter the number of completions:"))
    attempts = int(input("Enter the number of attempts:"))
    passing_yards = float(input("Enter the number of passing yards:"))
    touchdown_passes = int(input("Enter the number of touchdown passes:"))
    interceptions = int(input("Enter the number of interceptions:"))
    qbr = football(completions, attempts, passing_yards, touchdown_passes, interceptions)
    perfect_passer(qbr)

    # Quiddich Game
    print("This program will calculate your score from a quiddich game.")
    goals = int(input("Enter the number of goals made:"))
    snitch = str(input("Was the snitch caught?"))
    if snitch.strip().lower() == "yes":
        snitch = True
    elif snitch.strip().lower() == "no":
        snitch = False
    else:
        print("Error")
    quiddich(goals, snitch)
    snitch_points = 30
    final_quiddich_score = goals * 10
    score_with_snitch = final_quiddich_score + snitch_points

    # Gymnast Score
    print("This program will calculate the score of a gymnast.")
    difficulty_score = float(input("Enter the difficulty score:"))
    execution1 = input("Enter the first execution score:")
    if execution1.isdigit() and float(execution1) >= 0 and float(execution1) <= 10:
        execution1 = float(execution1)
    else:
        print("Score must be between 0 and 10.")
    execution2 = input("Enter the second execution score:")
    if execution2.isdigit() and float(execution2) >= 0 and float(execution2) <= 10:
        execution2 = float(execution2)
    else:
        print("Score must be between 0 and 10.")
    execution3 = input("Enter the third execution score:")
    if execution3.isdigit() and float(execution3) >= 0 and float(execution3) <= 10:
        execution3 = float(execution3)
    else:
        print("Score must be between 0 and 10.")
    execution4 = input("Enter the fourth execution score:")
    if execution4.isdigit() and float(execution4) >= 0 and float(execution4) <= 10:
        execution4 = float(execution4)
    else:
        print("Score must be between 0 and 10.")
    execution5 = input("Enter the fifth execution score:")
    if execution5.isdigit() and float(execution5) >= 0 and float(execution5) <= 10:
        execution5 = float(execution5)
    else:
        print("Score must be between 0 and 10.")
    gymnastics(execution1, execution2, execution3, execution4, execution5, difficulty_score)


def gymnastics(execution1, execution2, execution3, execution4, execution5, difficulty_score):
    max_score = max(execution1, execution2, execution3, execution4, execution5)
    min_score = min(execution1, execution2, execution3, execution4, execution5)
    dropped_scores = max_score + min_score
    other_scores = execution1 + execution2 + execution3 + execution4 + execution5
    final_execution = other_scores - dropped_scores
    average_execution = final_execution / 3
    final_score = difficulty_score + average_execution
    print("The final score is", str(final_score), "points.")

# Function for QB Rating
def perfect_passer(qb_calc):
    perfect_passer = 158.3
    if qb_calc >= perfect_passer:
        print("Your QB is a perfect passer!")
    else:
        print("Your QB is not a perfect passer.")

# Function for Quiddich Score
def quiddich(goals, snitch):
    if snitch == True:
        points = goals * 10 + 30
        print("The score of the Quiddich game is,", str(points), "points.")
    elif snitch == False:
        points = goals * 10
        print("The score of the quiddich game is", str(points), "points.")

def football(completions, attempts, passing_yards, touchdown_passes, interceptions):
    qb_calc = 100 * (5 * (completions / attempts - 0.3) + 0.25 * (passing_yards / attempts - 3) + 20 * (touchdown_passes / attempts) + 2.375 - (25 * interceptions / attempts) / 6)
    return qb_calc



main()







