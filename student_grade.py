# Function to get the average score of a student
def get_average_score(scores):
    # Compute the sum of scores
    total = sum(scores)

    # Get the number of subjects
    subject_count = len(scores)
    
    # Compute the average score
    average_score = total / subject_count
    
    return average_score

# Function to compute the grade based on the average score
def compute_grade(average_score):
    if average_score >= 80.0:
        grade = "A"
    elif average_score >= 60.0:
        grade = "B"
    elif average_score >= 50.0:
        grade = "C"
    else:
        grade = "F"
    
    return grade

# Student scores
student_scores = [55, 64, 75, 80, 65]

# Compute the average score
average_score = get_average_score(student_scores)

# Compute the grade
Grade = compute_grade(average_score)

# Print the results
print(f"Average Score: {average_score}")
print(f"Grade: {Grade}")

'''
Project Description
Suppose you are a teaching assistant at a university, and your task is to assign grades to students based on their average scores.

The scores obtained by a student in various subjects are stored in a list like this:

scores = [55, 64, 75, 80, 65]
Your job is to first compute the average score first.

Then, based on the average score, you need to compute the students' grade.

The grading rule is as follows:

1. Grade A: If the average score is equal to or above 80.
2. Grade B: If the average score is equal to or above 60 and less than 80.
3. Grade C: If the average score is equal to or above 50 and less than 60.
4. Grade F: If the average score is less than 50.

'''

