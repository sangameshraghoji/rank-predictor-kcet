import scipy.stats as stats

def predict_rank(board_marks, kcet_marks):
    total_marks = (board_marks/300)*50 + (kcet_marks/180)*50
    total_students = 220000
    z_score = (total_marks - 50) / 10
    predicted_rank = round(total_students * (1 - stats.norm.cdf(z_score)))
    return predicted_rank