import random

def main():
    score = 0 # Initialized the score locally instead of globally

    # Dictionary to map edge colors with their respective letter pair
    edge_pieces = {

        # This is the dictionary assuming the front face side is green and the top side is white
        # White
        ('WHITE', 'BLUE'): 'AQ',
        ('WHITE', 'RED'): 'BM',
        ('WHITE', 'GREEN'): 'CI',
        ('WHITE', 'ORANGE'): 'DE',
        # Orange
        ('ORANGE', 'WHITE'): 'ED',
        ('ORANGE', 'GREEN'): 'FL',
        ('ORANGE', 'YELLOW'): 'GX',
        ('ORANGE', 'BLUE'): 'HR',
        # Green
        ('GREEN', 'WHITE'): 'IC',
        ('GREEN', 'RED'): 'JP',
        ('GREEN', 'YELLOW'): 'KU',
        ('GREEN', 'ORANGE'): 'LF',
        # Red
        ('RED', 'WHITE'): 'MB',
        ('RED', 'BLUE'): 'NT',
        ('RED', 'YELLOW'): 'OV',
        ('RED', 'GREEN'): 'PJ',
        # Blue
        ('BLUE', 'WHITE'): 'QA',
        ('BLUE', 'ORANGE'): 'RH',
        ('BLUE', 'YELLOW'): 'SV',
        ('BLUE', 'RED'): 'TN',
        # Yellow
        ('YELLOW', 'GREEN'): 'UK',
        ('YELLOW', 'RED'): 'VO',
        ('YELLOW', 'BLUE'): 'WS',
        ('YELLOW', 'ORANGE'): 'XG',

    }

    print("I will give you two colors, and you tell me their pair name.")
    print("Type 'exit' at any time to quit. 'exit' in lowercase! \n")

    # here, it's making a list of just the keys of the dictionary we created above and assigning it to color_pairs
    color_pairs = list(edge_pieces.keys())

    while True:
        # randomly select a color pair (Pair in this case refers to two. Remember, this is for edges not corner practice.)
        color1, color2 = random.choice(color_pairs) # randomly pick out of the list we created above and assign it to the variables
        print(f"Edge Piece: {color1}, {color2.lower()}. What's their name?")
        # I made the second color lowercase to match with speedcubing notation

        # Here's the logic for user input
        correct_name = edge_pieces[(color1, color2)]
        # This line will refer to the dictionary we made
        user_input = input("Your answer: ")
        if user_input.lower().strip() == 'exit':
            print("Bye!")
            break
        elif user_input.upper() == correct_name or user_input.upper() == correct_name[0]: # this is the scoring
            print("Correct!")
            score += 1 # if you want to get more points (5 points instead of 1), change this number
            print("Your score:", f"{score}\n")
        else:
            print(f"Wrong! The correct name is: {correct_name}")
            print("Your score:", f"{score}\n") # this will print the current score you have - you do not get a point off for an incorrect answer


if __name__ == "__main__":
    main()