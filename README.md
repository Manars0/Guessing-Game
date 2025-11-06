# Guessing Game

A simple **number guessing game** built using the `Tkinter` library in Python.  
The user tries to guess a random number between **1 and 100**, receiving hints like *COLD*, *WARM*, *COLDER*, or *WARMER* depending on their guesses.

## How It Works
1. The program generates a random number between 1 and 100.
2. The player enters their guess in the input box.
3. Based on the guess:
   - If the guess is **more than 10 away** from the number → "COLD"
   - If the guess is **within 10** of the number → "WARM"
   - If the guess is **closer** than the previous guess → "WARMER"
   - If the guess is **farther** → "COLDER"
4. When the correct number is guessed, a congratulatory message appears.

## GUI Overview
- Built with **Tkinter**
- Input box for guesses
- Submit button
- Popup messages showing feedback (*WARM, COLD, WARMER, COLDER, or WINNER*)

## Features
- Interactive GUI interface  
- Random number generation  
- Intelligent feedback based on proximity to the correct number  
- Simple and fun gameplay loop  

## Technologies Used
- **Python 3.x**
- **Tkinter** (GUI)
- **Random** module

## Example Output
`````
guess a random number in range 1 to 100 correctly:
If your guess is more than 10 away from my number, I'll tell you you're COLD
If your guess is within 10 of my number, I'll tell you you're WARM
If your guess is farther than your most recent guess, I'll say you're getting COLDER
If your guess is closer than your most recent guess, I'll say you're getting WARMER

LET'S PLAY!
`````
## Author
**Manar Salem**  
Programming and Database Student  
[https://github.com/Manars](https://github.com/Manars)
