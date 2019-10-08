# CS151 PROGRAMMING ASSIGNMENT #3  
60  POINTS   (10pts design, 50pts final)  
DESIGN DUE: 10/09/19  
FINAL DUE: 10/16/19  

## PROBLEM 
Create a program that will calculate various sports statistics for the user, based on the user’s choice of statistic. 

## PURPOSE OF THE ASSIGNMENT
The purpose of this assignment is to give you practice with

1. input & output
2. decision making
3. function design and implementation
4. error checking

## REQUIREMENTS ANALYSIS
The first stage in your programming assignment is the requirements analysis stage.  You need to make sure you understand the below requirements for what your program needs to do. Your program will give the user the option of calculating statistics relevant to three sports. You must do the calculations for the following sports in your program in the way that is described here: 

* Quarterback rating in American football:
  * The quarterback rating determines how good a quarterback is in passing (throwing) a football. A perfect passer rating in the NFL is considered to be a 158.3.  
  * QB rating = 100 * [5(completions/attempts – 0.3) + 0.25(passing_yards/attempts-3) + 20(touchdown_passes/attempts) + 2.375 – (25 * interceptions/attempts)]/6
  * Note that attempts means the number of passing attempts made, and is the same number used throughout the equation. Completions is the number of completed passing attempts. Touchdown passes is the number of passes for a touchdown, and interceptions are the number of times the ball was intercepted.  
  * You should tell the user whether or not the quarterback is a perfect passer.  
  
* Calculate the score for a team in a game of Quidditch as described by the [International Quidditch Association](http://www.iqasport.com/): 
  * A goal is scored by propelling the quaffle through a hoop. The team earns 10 points per goal.
  * If the team has caught the snitch, the team earns an additional 30 points 
  
* Calculate the final score for a gymnast on any apparatus:
  * Assume there are 6 scores (we’re simplifying slightly from the real world). One score is on difficulty. The other 5 scores are on execution. All scores are between 0 and 10. Of the execution scores, the highest and lowest are dropped. The final score is acquired by adding the difficulty score to the average of the execution scores.

In your program, you must do some basic error checking: check if you are going to divide by zero when relevant, and don’t do the calculation if that’s the case; and before typecasting input to an int, check that it is only digits, and don’t typecast or do the calculation otherwise. In any case where an error is detected, output that it was an error, and don’t continue the calculation – you may output a zero for the result of the calculation. 

## DESIGN

1. Determine the tasks being accomplished in your program. Each of these should be a function. If you find yourself writing the same steps in many places, that is usually a good sign that those steps should be in their own function.
2. Remember that the user is only going to do ONE of the sports statistics calculations, although your program can do all three of them. They choose which one to do.
3. Write an algorithm for each function. This algorithm includes parameters, calculations, and returned values. In general your function will NOT output anything, except perhaps error messages when invalid input is given; your main program should do all of the output of results. Results from functions should be returned instead.
4. **WRITE THE CODE** for your Quiddich function(). The function code should include comments documenting the function: parameters, what they represent, return value. There should not be any output inside the Quidditch function (and later, the other sport functions), other than reporting a possible error.
5. **WRITE THE CODE** for a main function that will call the Quidditch function at least 3 times with three different sets of values.

You may find it helpful the first time to start on your algorithm first, and then break it up into functions later. But you need to have it written in terms of functions for the design submission. 

### DESIGN SUBMISSION: 10/09/19

Submit to GitHub:    
  * the algorithm for your program in designInitial.txt. The general format for a function is given. You can copy/paste the starting point (name, parameters, return, algorithm headers) for as many functions as you need to define for your problem.    
  * PA2.py containing your Quiddich() function and a main() function   


***Remember to double check on github.com that your files pushed. If they didn’t, you need to push them. I can only see what is on github.com, not what is only on your computer.***


## EXTRA CREDIT (only if everything else works)
If you choose to do extra credit, it must be submitted in a separate file with “extraCredit” in the file name. 

Each of the following extra credit options will earn you extra credit. You can do either or both of them:
1.	Add error checking to the gymnastics calculation so that the calculation is only done if the score is between 0 and 10.
2.	Design a function that allows the user to keep trying to input an int when an int was asked for, until they do so. Use this function wherever you checked for an int in the original program.

## REFLECTION
Write a short reflection about the programming assignment in reflection.txt: what did you learn, what would you do differently next time, what was difficult, how were functions useful?  This should be no more than a page.

## FINAL SUBMISSION   
* To GitHub:
  * Your .py file
  * Your extra credit .py file if you did the extra credit (make sure “extraCredit” is in the filename)
  * Your reflection of the programming assignment in reflection.txt
  * Your final algorithm, including the changes you made based on the design feedback in designFinal.txt
* To Moodle:
  * A pdf of a flowchart of your program as described above, with control paths labeled (pdf or image file).
  * Your test cases based on your flowchart in testcases.xlsx. You should have at least 1 test case per control path, using boundary values (see Notes #7). Be sure to take advantage of Excel's formula calculation abilities for calculating expected mathematical output.

***Remember to double check on github.com that your files pushed. If they didn’t, you need to push them. I can only see what is on github.com, not what is only on your computer.***
