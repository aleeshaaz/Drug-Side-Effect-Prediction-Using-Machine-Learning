
import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Path setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "drug_side_effect_dataset_5000_enhanced.csv")
MODEL_DIR = os.path.join(BASE_DIR, "model")

# Create model folder if not exists
os.makedirs(MODEL_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH)

# Features and target
X = df[["Age","WBC","Eosinophils","Creatinine","ALT","AST","Hemoglobin","Platelets"]]
y = df["Severity"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
model = joblib.load("model/side_effect_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")
mlb = joblib.load("model/label_binarizer.pkl")

print("✅ Model trained and saved successfully!")
