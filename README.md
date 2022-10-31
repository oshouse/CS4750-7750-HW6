# CS4750-7750-HW6

### CS 4750 - 7750 Artificial Intelligence I Homework 6
#### Collaborators
    - Ryan Christopher
    - Olivia Shouse
    - Luke Schaefer

## Prompt 
#### Implement  forward  checking  and  backtracking  search  with  MRV  and  degree heuristic to solve 9x9 Sudoku puzzle (https://en.wikipedia.org/wiki/Sudoku). Run forward check after each assignment during backtracking search.  
#### When selecting which variable to be assigned values in backtracking search, break variable ties in the left to right (primary) and top to bottom (secondary) order. When selecting  the  values  to  be  assigned  to  a  variable,  break  value  ties  based  on  the increasing order of the values, i.e., 1, 2, etc.  
#### Run  your  program  on  the  following  three  instances  to  find  a  solution  for  each instance. Terminate your program if it runs for more than one hour. 

## Submission
a. (7  points)  A  description  of  your  CSP  problem  formulation  (define  the variables,  domains,  and  constrains)  and  implementation  of  forward 
checking and backtracking search with MRV and degree heuristic. If you use existing code, cite the sources. 

b. (8 points) For each of the three instances, print out the first 4 variable-value 
assignments in the backtracking search, including 
    - a) the variable selected, 
    - b) the domain size of the selected variable, 
    - c) the degree of the  selected variable, and 
    - d) the value assigned to the selected variable.   
    
c. (3 points) For each instance, report its solution and the corresponding CPU 
execution time in seconds. 
