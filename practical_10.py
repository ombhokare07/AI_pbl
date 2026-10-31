# Lab Title	Training a Decision Tree Classifier on the Iris Dataset using scikit-learn

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

# Step 1: Load the dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Feature names:", iris.feature_names)
print("Class names:", [str(name) for name in iris.target_names])
print("Dataset shape:", X.shape, "\n")

# Step 2: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
print(f"Training samples: {len(X_train)} Testing samples: {len(X_test)}\n")

# Step 3: Create and train the Decision Tree Classifier
model = DecisionTreeClassifier(
    criterion="entropy", max_depth=3, random_state=42
)
model.fit(X_train, y_train)

# Step 4: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on test data: {accuracy * 100:.2f}%\n")

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred), "\n")

print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Step 6: Print the learned tree as readable if-else rules
print("Decision Tree Rules:")
print(export_text(model, feature_names=list(iris.feature_names)))

# Step 7: Classify one brand-new flower measurement
sample = [[5.0, 3.4, 1.5, 0.2]]  # sepal length, sepal width, petal length, petal width
prediction = model.predict(sample)[0]
print(
    f"Prediction for new sample {sample[0]}:"
    f" {iris.target_names[prediction]}"
)