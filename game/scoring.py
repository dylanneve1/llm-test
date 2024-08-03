# scoring.py
score = 0
high_scores = []

def save_score(score):
    high_scores.append(score)
    high_scores.sort(reverse=True)
    if len(high_scores) > 5:
        high_scores.pop()  # Keep only top 5 scores
    print('High Scores:', high_scores)
