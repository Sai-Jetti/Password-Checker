Password Strength Checker

This is a simple Python command-line tool that checks how strong a password is and estimates how long it would take to brute-force guess it.

What It Does:
1. Takes a password as input from the user
2. Checks the password against basic strength criteria:
    - Minimum length (8+ characters)
    - Contains uppercase letters
    - Contains lowercase letters
    -  Contains digits
    - Contains special characters (!@#$%^&*)
3. Scores the password based on how many criteria it meets
4. Gives an overall strength verdict: Weak, Medium, or Strong
5. Estimates the number of brute-force attempts it would take to guess the password
6. Converts that estimate into a readable time estimate (seconds, minutes, hours, or years)
   
How It Works:

The tool calculates a "character pool" based on which types of characters are used in the password (lowercase, uppercase, digits, special characters). It then raises that pool size to the power of the password's length to estimate the total number of possible combinations an attacker would need to try in a worst-case brute-force scenario. That number is converted into an estimated crack time using an assumed guessing speed.

How to run the program: 

Follow the prompt to enter a password, and the program will print out the strength verdict and estimated crack time. You'll be asked if you want to check another password before the program exits.


This project was a way for me to practice:
1. Working with user input and string methods
2. Using conditionals and loops
3. Writing reusable functions
4. Applying basic math/logic (combinatorics) to a real-world concept like password entropy

Future Improvements:
1. Colored terminal output for strength verdicts
2. Specific tips based on which criteria failed (e.x., "add a special character")
3. Checking against a list of commonly leaked passwords
4. A password generator feature
5. A simple GUI using Tkinter
