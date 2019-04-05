# Techgig_challenges--Amdocs
Problem Statement-Tiger Shah and Battleships 

Tiger Shah has been hired to write a program to analyze strategic data for the Scandinavian Navy. His task is described below. 
There are L battleships represented as L points on the plane. The radius of a ship is defined to be the distance from that ship to the ship closest to it. The effective set for a ship is defined to be the set of all ships (excluding itself) which are at a distance from that ship of no more than twice its radius. The number of elements in the effective set of a ship is called the effective value of that ship. 
Tiger Shah needs to write a program to calculate the radius and the effective value of each battleship. This task is so tough that without your help, Tiger Shah could never finish it. Let's help him! 
Input Format:
The first line contains t, the number of test cases. Then t test cases follow. 
Each test case has the following form:
 The first line contains an integer L, the number of battleships. 
Each of the next L lines contains two integers X, Y (space separately) which represents the coordinates of a battleship. 

Note: There may be more than one ships located at the same place. 
Constraints 1<= t <=5 1 <= L <= 30000 0 <= X, Y <= 10000 

sample test case 1
Input
2
3
0 0
0 0
3 4
5
5 3
7 8
0 9
3 1
4 4

Output
0.00 1
0.00  1
5.00  2
1.41  2
5.00  4
6.40  4
2.83  2
1.41  1
