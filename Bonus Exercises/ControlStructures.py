## Control Structures:
## Imagine an alien was just shot down in a game. Create a variable called alien_color and
## assign it a value of 'green', 'yellow', or 'red'.
## •Write an if statement to test whether the alien’s color is green. If it is, print a message
## that the player just earned 5 points.
## •Write one version of this program that passes the if test and another that fails. (The
## version that fails will have no output.)

## Version that fails

alien_color = "yellow"                         ## Assigning incorrect alien color
actual_color = "green"                         ##  Assinging actual color

if alien_color == actual_color :
   print("Correct you have earned 5 points")                ## Print statement if color is correct 

## Version that passes

alien_color = "green"                           ## Assigning correct Alien color
actual_color = "green"

if alien_color == actual_color :
   print("Correct you have earned 5 points")
