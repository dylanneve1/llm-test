# leaderboard.py
from game.scoring import high_scores

def display_score(attempts):
    global score
    score += max(0, 100 - attempts * 10)  # Simple scoring system
    print(f'Your current score is: {score}')
    save_score(score)
