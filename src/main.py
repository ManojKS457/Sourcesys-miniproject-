import numpy as np


def generate_data():
    np.random.seed(42)
    marks = np.random.randint(35, 100, size=(100, 5))
    return marks



def apply_weights(marks):
    weights = np.array([0.2, 0.15, 0.25, 0.2, 0.2])
    weighted_marks = marks * weights   # Broadcasting
    return weighted_marks



def compute_total(weighted_marks):
    return np.sum(weighted_marks, axis=1)



def normalize(scores):
    return (scores - np.min(scores)) / (np.max(scores) - np.min(scores))



def assign_grades(norm_scores):
    return np.where(norm_scores > 0.8, 'A',
           np.where(norm_scores > 0.6, 'B',
           np.where(norm_scores > 0.4, 'C',
           np.where(norm_scores > 0.2, 'D', 'F'))))



def analyze(marks, totals, grades):
    subject_avg = np.mean(marks, axis=0)
    toppers = np.where(grades == 'A')[0]

    print("\n--- ANALYSIS ---")
    print("Subject Averages:", subject_avg)
    print("Topper Indices:", toppers[:10])



def main():
    marks = generate_data()
    np.savetxt("../data/student_marks.csv", marks, delimiter=",", fmt="%d")
    weighted = apply_weights(marks)
    totals = compute_total(weighted)
    ranks = np.argsort(-totals)
    print("Top 5 Students:", ranks[:5])
    normalized = normalize(totals)
    grades = assign_grades(normalized)

    print("Sample Marks:\n", marks[:5])
    print("Sample Grades:", grades[:5])

    analyze(marks, totals, grades)


if __name__ == "__main__":
    main()