# Student attributes
# Initial number of hours the student studied
student_hours = 16
# Initial number of assignments completed
student_assignment = 3
# Average test score of the student
student_testscore = 45

# Parameters for prediction calculations
# Threshold score for passing
threshold_score = 230
# Weight multiplier for study hours
study_weight = 10
# Weight multiplier for completed assignments
assignment_weight = 5
# Weight applied to test scores 
score_weight = 0.7

# Simulating changes in input data using compound assignment
# Increase study hours by 2
student_hours += 2
# Increment completed assignments by 1
student_assignment +=1
# Deduct 5.5 points due to a poor performance in a recent test
student_testscore -= 5.5

# Calculate the predicted score
predicted_score = (student_hours * study_weight) + (student_assignment * assignment_weight) + (student_testscore * score_weight)

# Display the calculated predicted score
print(f"The predicted score is: {predicted_score}")

# Determine if the student is predicted to pass
is_predicted_to_pass = predicted_score >= threshold_score

if not is_predicted_to_pass:
	print("\nPrediction: The student needs more preparation.")
else:
	print("\nPrediction: The student is likely to pass.")

