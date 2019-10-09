# Programmers:  [Erin McAvoy]
# Course:  CS151.05, Dr. Isaacman
# Date: [10/8/19]
# Programming Assignment:  [PA3]
# Problem Statement:  [calculates the score of a quiddich game]
# Data In: [number of goals, number of times snitch was caught]
# Data Out:  [total score]

def quiddich_score():
    print("This program will calculate your score from a quiddich game.")
    goals = int(input("How many goals did you make?"))*10
    snitch_catches = int(input("How many times did you catch the snitch?"))*30
    quiddich_score = goals + snitch_catches
    print("Your quiddich score is", quiddich_score, "points.")
    print("Thank you.")
quiddich_score()




