# Pomodoro Timer

A simple Pomodoro timer application to boost your productivity using the Pomodoro Technique.

## About the Pomodoro Technique

The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. Each interval is known as a "pomodoro," from the Italian word for tomato, after the tomato-shaped kitchen timer that Cirillo used as a university student.

## Description

This Pomodoro Timer application helps you implement the Pomodoro Technique to boost your productivity and maintain focus. The application follows the standard Pomodoro workflow:

1. **Focus Session (25 minutes)**: Work on a task with full concentration
2. **Short Break (5 minutes)**: Take a brief break to rest your mind
3. **Repeat Steps 1-2**: Complete three more focus sessions with short breaks
4. **Long Break (15 minutes)**: After 4 completed Pomodoros, take a longer break

The application provides audio notifications when each session ends, allowing you to stay on track without constantly watching the clock. Currently available as a command-line application with a graphical interface planned for future releases.

### Why Use the Pomodoro Technique?

- **Improved Focus**: The time constraint helps maintain concentration
- **Reduced Mental Fatigue**: Regular breaks prevent burnout
- **Better Time Awareness**: Learn how long tasks actually take to complete
- **Increased Accountability**: Track your productivity throughout the day
- **Reduced Procrastination**: Breaking work into manageable chunks makes starting easier
- **Better Work-Life Balance**: Clear boundaries between focused work and rest

## Features

- 25-minute work intervals (pomodoros)
- 5-minute short breaks after each pomodoro
- 15-minute long breaks after every 4 pomodoros
- Sound notifications at the end of each interval
- Simple command-line interface

## Requirements

- Python 3.x
- Pygame library (for sound functionality)

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/pomodoro.git
cd pomodoro
```

2. Install required dependencies:
```
pip install pygame
```

3. Make sure you have sound files in a directory named `sounds` in the project root.

## Usage

Run the program with:
```
python main.py
```

Follow the prompts to start your Pomodoro sessions.

## Planned Features

- Graphical user interface
- Customizable time intervals
- Task tracking
- Statistics and progress visualization
- Multiple themes
- Desktop notifications

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.


