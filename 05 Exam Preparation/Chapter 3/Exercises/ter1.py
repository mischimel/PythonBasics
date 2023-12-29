"""
ter1. Rewriting grader.py
Rewrite grader.py (see chapter 3 programs) by using
• Version 1: the elif statement
• Version 2: the match / case statement (is a “switch”-like statement available from v3.10 on)
"""

# ORIGINAL
# This program (grader.py) gets a numeric test score from the user and displays the corresponding letter grade.

# Variables to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))

# Determine the grade.
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')

# WITH ELIF STATEMENT
if score >= A_score:
    print('Your grade = A.')
elif score >= B_score:
    print('Your grade = B.')
elif score >= C_score:
    print('Your grade = C.')
elif score >= D_score:
    print('Your grade = D.')
else:
    print('Your grade = F.')


# WITH MATCH/CASE ("SWITCH") STATEMENT
match score:
    case int(score) if score >= A_score:
        print('Your grade: A.')
    case int(score) if score >= B_score:
        print('Your grade: B.')
    case int(score) if score >= C_score:
        print('Your grade: C.')
    case int(score) if score >= D_score:
        print('Your grade: D.')
    case _:
        print('Your grade: F.')
