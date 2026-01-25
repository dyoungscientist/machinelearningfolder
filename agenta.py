from sklearn.linear_model import LinearRegression
import numpy as np
# Prepare training data
print("Training AI model...")

# Hours studied vs Scores
hours = np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
scores = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print (f"Training with {len(hours)} examples...") 

# Train the model
model = LinearRegression()
model.fit(hours, scores)
print("Model trained successfully!")

# make predictions
hours_to_studied = float(input("Enter hours studied to predict score:"))

predicted_score = model.predict([[hours_to_studied]])
#print(f"Predicted score for studying {hours_to_studied} hours: {predicted_score[0][0]}")

# test with multiple values
print("prediction table")

#for h in [1, 3, 5, 7, 9, 10]:
  #  pred = model.predict([[h]])
   # print(f"{h} hours -> {pred[0]:.1f} score")

