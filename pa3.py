# Programmers:  [Erin McAvoy]
# Course:  CS151.05, Dr. Isaacman
# Date: [10/8/19]
# Programming Assignment:  [PA3]
# Problem Statement:  [calculates the score of a quiddich game]
# Data In: [number of goals, number of times snitch was caught]
# Data Out:  [total score]

# Main Function Defined
def main():
    # QB Rating
    print("This program will tell you if the QB is a perfect passer.")
    completions = int(input("Enter the number of completions:"))
    attempts = int(input("Enter the number of attempts:"))
    passing_yards = float(input("Enter the number of passing yards:"))
    touchdown_passes = int(input("Enter the number of touchdown passes:"))
    interceptions = int(input("Enter the number of interceptions:"))
    qb_calc = 100* [5(completions/attempts-0.3) + 0.25(passing_yards/attempts-3) + 20(touchdown_passes/attempts) + 2.375 – (25*interceptions/attempts)]/6
    perfect_passer = 158.3

    # Quiddich Game
    print("This program will calculate your score from a quiddich game.")
    goals = int(input("Enter the number of goals made:"))
    snitch = str(input("Was the snitch caught?"))
    snitch_points = 30
    final_quiddich_score = goals * 10
    score_with_snitch = final_quiddich_score + snitch_points

    # Gymnast Score
    print("This program will calculate the score of a gymnast.")
    difficulty_score = float(input("Enter the difficulty score:"))
    execution1 = float(input("Enter the first execution score:"))
    execution2 = float(input("Enter the second execution score:"))
    execution3 = float(input("Enter the third execution score:"))
    execution4 = float(input("Enter the fourth execution score:"))
    execution5 = float(input("Enter the fifth execution score:"))
    max_score =
    min_score =
    dropped_scores = max_score + min_score
    other_scores =
    final_execution = other_scores - dropped_scores
    average_execution = final_execution / 3
    final_score = difficulty_score + average_execution

# Function for QB Rating
def perfect_passer(qb_calc):
    if qb_calc >= perfect_passer:
        print("Your QB is a perfect passer!")
    else:
        print("Your QB is not a perfect passer.")

# Function for Quiddich Score
def quiddich_score(snitch_points, final_quiddich_score, score_with_snitch):
    if snitch == "yes":
        print("The score of the Quiddich game is," (score_with_snitch), "points.")
    elif snitch == "no":
        print("The score of the quiddich game is", (final_quiddich_score), "points.")

# Function for Gymnast Score
def final_score(difficulty_score, execution1, execution2, execution3, execution4, execution5, max_score, min_score,dropped_scores, other_scores,final_execution, average_execution,final_score)


main()







