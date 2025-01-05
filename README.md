TASK 1:-
Fibonacci Series in Python
This program generates the Fibonacci series, a sequence of numbers where each number is the sum of the two preceding numbers. The sequence begins with 0 and 1. For example, the first 10 Fibonacci numbers are:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

How the Program Works
1. Understanding the Fibonacci Series
The Fibonacci sequence is defined by the recurrence relation:
F(n) = F(n-1) + F(n-2),
with the initial conditions:
F(0) = 0 and F(1) = 1.

2. Algorithm
To generate the series up to n terms:
Start with the initial values a = 0 and b = 1.
Use a loop to calculate the next term as a + b while updating a and b.
Append each term to a list for storage.
Stop after n terms.

4. Code Implementation

# Function to generate Fibonacci series
def fibonacci_series(n):
    # Initial two numbers of the series
    a, b = 0, 1
    series = []  # List to store the series
    
    # Generate series up to n terms
    for _ in range(n):
        series.append(a)  # Add the current term to the list
        a, b = b, a + b   # Update 'a' and 'b' for the next term
    
    return series

# Input from the user
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series up to {num_terms} terms:")
    print(fibonacci_series(num_terms))
4. Detailed Explanation
Function fibonacci_series(n)
Inputs:
n (integer) - The number of terms in the Fibonacci series.

Logic:
Start with two variables: a = 0 and b = 1, which represent the first two terms of the Fibonacci sequence.
Create an empty list series to store the generated numbers.
Use a for loop that runs n times. During each iteration:
Append the value of a to series.
Calculate the next Fibonacci number by updating a to b and b to a + b.
Return the list series containing the Fibonacci sequence.

Input Validation
Before calling the fibonacci_series function, the program checks if the input (num_terms) is greater than 0. If not, it prints an error message and exits.
Input and Output

The user is prompted to enter the number of terms.
If the input is valid, the program calculates and prints the Fibonacci sequence.

5. Sample Outputs
Example 1:
Enter the number of terms for the Fibonacci series: 7
Output:
Fibonacci series up to 7 terms:
[0, 1, 1, 2, 3, 5, 8]

Example 2:
Enter the number of terms for the Fibonacci series: -5
Please enter a positive integer.

6. Key Features
User Input Validation: Ensures the user enters a valid positive integer.
Dynamic Series Generation: The program can generate the Fibonacci series for any positive number of terms.
Scalability: The code can easily be extended to handle larger numbers using techniques like memoization or generators.

How to Run the Program
Install Python (if not already installed) from python.org.
Copy the above code into a Python file, e.g., fibonacci.py.
Open a terminal or command prompt, navigate to the file's directory, and run the program:
python fibonacci.py
Enter the number of terms as prompted.



Task 2 Voice Assitant 
🎙️ Voice Assistant using Python
This project implements a voice assistant using Python. The assistant can recognize speech, respond to simple commands, provide the current time, perform web searches, set reminders, and gracefully exit upon request.

🔧 Features
Speech Recognition: Converts spoken words into text.
Text-to-Speech: Responds verbally using a speech engine.
Current Time: Provides the current system time.
Web Search: Searches the web using Google.
Reminders: Sets and reminds tasks after a short delay.
Exit Command: Stops the program gracefully.

🛠️ Setup Instructions

Clone the Repository:
git clone https://github.com/your-repo-name/voice-assistant.git
cd voice-assistant

Install Dependencies: This program uses the following Python libraries:
speech_recognition: For speech-to-text.
pyttsx3: For text-to-speech.
datetime: For fetching the current time.
webbrowser: To open web pages.
time: For handling delays.

Install dependencies using pip:
pip install speechrecognition pyttsx3

Run the Program: Execute the script using Python:
python voice_assistant.py

📝 Code Explanation

1. Initializing the Speech Engine
engine = pyttsx3.init()
Initializes the text-to-speech engine.

3. Text-to-Speech Function
python
Copy code
def speak(text):
    engine.say(text)
    engine.runAndWait()
Converts the provided text into speech.

4. Speech Recognition Function
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
Captures audio from the microphone and converts it into text using Google’s Speech Recognition API.

5. Main Voice Assistant Logic
def voice_assistant():
    speak("Hello! How can I assist you today?")
    while True:
        text = recognize_speech()
        if "hello" in text:
            speak("Hello! How can I assist you today?")
        elif "time" in text:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}")
        elif "search" in text:
            query = text.split("search")[-1].strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query} on Google.")
        elif "remind me" in text:
            reminder = text.split("remind me")[-1].strip()
            speak(f"Reminder set for {reminder}")
            time.sleep(10)  # Example: Waits for 10 seconds
            speak(f"Reminder: {reminder}")
        elif "exit" in text:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I did not understand that command.")
Greeting: Starts with a welcome message.

Command Parsing: Listens for specific commands and performs corresponding actions:
"hello": Greets the user.
"time": Announces the current system time.
"search": Opens a Google search for the provided query.
"remind me": Sets a reminder and announces it after a 10-second delay.
"exit": Ends the program.

🔍 Sample Outputs
Example 1: Greeting
User: Hello
Assistant: Hello! How can I assist you today?

Example 2: Time Query
User: What is the time?
Assistant: The current time is 14:30.

Example 3: Web Search
User: Search Python programming
Assistant: Searching for Python programming on Google.
(Opens a browser tab with Google search results for "Python programming".)

Example 4: Reminder
User: Remind me to drink water
Assistant: Reminder set for drink water.
(After 10 seconds)
Assistant: Reminder: drink water.

Example 5: Exit
User: Exit
Assistant: Goodbye!

⚙️ Future Enhancements
Add more commands (e.g., weather updates, opening applications).
Improve speech recognition for noisy environments.
Integrate with APIs for advanced features like calendar events or emails.
Add a GUI for better user interaction.
💬 Contribute
Feel free to fork the repository and suggest improvements. Let’s make this assistant smarter together! 🚀

📜 License
This project is open-source and available under the MIT License.

🌟 Acknowledgments
Special thanks to the creators of the speech_recognition and pyttsx3 libraries for making this project possible.



Task 3
# Tic-Tac-Toe Game in Python

This repository contains a Python implementation of the classic Tic-Tac-Toe game, where a user can play against another user or the computer.

## Features

- **Interactive Gameplay**: Players take turns to place their marks (X or O) on a 3x3 grid.
- **Winning Logic**: The game detects when a player wins or if the game ends in a draw.
- **User-Friendly Interface**: The board is displayed in a clear and concise format.

## How to Play

1. The game begins with an empty 3x3 board.
2. Players alternate turns to place their marks (X or O) in an empty cell.
3. A player wins if they align three marks horizontally, vertically, or diagonally.
4. If all cells are filled without a winner, the game ends in a draw.

## Code Overview

### Key Functions

- **`print_board(board)`**: Displays the current state of the board.
- **`check_winner(board, player)`**: Checks if the specified player has won the game.
- **`is_draw(board)`**: Determines if the game is a draw.
- **`play_turn(board, player)`**: Manages a player's move.

### Sample Board Display
```
 X | O | X
---+---+---
 O | X | O
---+---+---
 X |   | O
```

## Requirements

- Python 3.x

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/tictactoe-python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tictactoe-python
   ```
3. Run the game script:
   ```bash
   python Task3.py
   ```

## Customization

You can modify the game logic or add features, such as:
- Allowing a single-player mode against an AI opponent.
- Enhancing the board display with a graphical user interface (GUI).

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

## Contribution

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

---

Enjoy the game and happy coding! 🎮
