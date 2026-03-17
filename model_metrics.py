import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load dataset
df = pd.read_csv("data/drug_side_effect_dataset_5000_enhanced.csv")

# Input features
X = df[["Age","WBC","Eosinophils","Creatinine","ALT","AST","Hemoglobin","Platelets"]]

# Target variable
y = df["Severity"]

# Split dataset
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train,y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
accuracy = accuracy_score(y_test,y_pred)
precision = precision_score(y_test,y_pred,average="weighted")
recall = recall_score(y_test,y_pred,average="weighted")
f1 = f1_score(y_test,y_pred,average="weighted")

print("Accuracy:",accuracy*100)
print("Precision:",precision)
print("Recall:",recall)
print("F1 Score:",f1)
