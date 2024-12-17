# 3x3 Rubik Cube Blindfold Practice [Edges Only: Pochmann Method]

This repository contains a Python script designed to help speedcubers memorize edge pairings for the Old Pochmann method of solving a 3x3 Rubik's Cube blindfolded. The program randomly selects edge color pairs and prompts the user to input their corresponding letter pair notation, assisting in learning and practicing the mapping of colors to letters.

## Features

Basically a Python quizlet for speedcubers. But since other cubers might use different notation, letters, or buffers, this is 10x easier to customize to your technique by editing the Python dictionary. Whether you are a beginner or Charlie Eggins, this program practices your memorization and speed so that you can feel confident using blindfold edge mnemonics. The edge color pairings and their letter mappings are defined in the aforementioned dictionary, which means you can easily modify the code to feature your own preferences or extend it to include other pieces. I recommend commenting out the colors you are not practicing (for example, if you only want to practice the yellow edges, comment out red, green, blue, white, and orange).

Score Tracking: Tracks and displays your score to keep you motivated as you practice.

Make sure to **type exit to quit the program.**

UPDATE [12/17/24]: To get started, **CLICK HERE** for the updated `.py` file: [NEW 3x3 BLD Practice in Python [Edges]](https://github.com/shalynbarrios/3x3-Rubik-Cube-Blindfold-Practice/blob/main/NEW_3x3_practice.py)

## How it Works

The program contains a dictionary mapping color pairs (e.g., ('WHITE', 'BLUE')) to letter pairs (e.g., 'AQ'). However, since you don't need to know both letters for one edge piece, you can just type the letter you need (e.g., 'A').

A random color pair is selected, and the user is prompted to provide the corresponding letter pair.

The program checks the input. If correct, the score increases. If your answer is incorrect, you won't be taken away any points, only the correct letter pair is displayed. This quiz continues until the user types exit.

## Prerequisites

1. Basic knowledge of Old Pochmann's Method. (I recommend Charlie Eggins' videos on Youtube.)

2. Python 3 or later

## Other Notes

This project is available in two formats: a Jupyter Notebook file and a standard Python `.py` file. While both versions work, I recommend using the `.py` file as it is more accessible, follows standard coding practices, and is easier to run in most environments. Happy cubing!

**UNDER MIT LICENSE**
