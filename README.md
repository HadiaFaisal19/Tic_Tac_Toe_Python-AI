# Tic_Tac_Toe_Python-AI
A Tic-Tac-Toe game built in Python, where the user plays against an AI agent. The AI tries to block the user and win with game.
## Features
- User and Agent play turns to place "O" and "X" on the 3x3 grid.
- The user inputs the row and column where they want to place their "O".
- The agent intelligently tries to win or block the user using basic logic, and places "X".
- The game ends when a player wins or the grid is full (tie).
- Clean and simple command-line interface.

##Game Logic
The agent first checks if it can win in its next move.
If not, the agent checks if the user is one move away from winning and blocks it.
If no immediate win or block is required, the agent places its mark randomly.

## How to Play
1. Clone or download the repository.
2. Run the `tic-tac-toe.py` script in a Python environment.
3. The user will be prompted to input the row and column to place their "O".
4. The agent will make its move automatically.
5. The game continues until either the user or the agent wins, or the game ends in a tie.

## Requirements
- Python 3.x

## Running the Game
1. Clone the repository:
   ```bash
   git clone [https://github.com/HadiaFaisal19/Tic_Tac_Toe_Python-AI].git
   cd tic-tac-toe-python-ai

2. Run the game:
   ```bash
   python tic-tac-toe.py

#Contributions
Feel free to fork the repository and submit pull requests for improvements, bug fixes, or additional features.

