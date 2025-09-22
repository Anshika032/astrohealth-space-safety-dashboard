# src/debris_classify.py
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

MODEL_PATH = "models/debris_rf.joblib"

def train_classifier(csv_path="data/debris_dataset.csv", save_path=MODEL_PATH):
    df = pd.read_csv(csv_path).dropna()
    X = df.drop("label", axis=1)
    y = df["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    print(classification_report(y_test, preds))
    joblib.dump(clf, save_path)
    print("Saved model to", save_path)
    return clf

if __name__ == "__main__":
    train_classifier()
 
