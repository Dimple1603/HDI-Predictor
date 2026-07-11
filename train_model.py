import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load Dataset
df = pd.read_csv(
    "dataset/Human Development Index and Components.csv",
    encoding="latin1"
)

# Clean column names
df.columns = df.columns.str.strip()

# Rename columns
df.rename(columns={
    "Human Development Index (HDI)": "HDI",
    "Life expectancy at birth": "Life",
    "Expected years of schooling": "Expected",
    "Mean years of schooling": "Mean",
    "Gross national income (GNI) per capita": "GNI"
}, inplace=True)

# Keep only required columns
df = df[["Life", "Expected", "Mean", "GNI", "HDI"]]

# Replace '..' with NaN
df.replace("..", pd.NA, inplace=True)

# Convert everything to numeric
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove missing values
df.dropna(inplace=True)

print(df.head())
print("\nRows after cleaning:", len(df))

# Features
X = df[["Life", "Expected", "Mean", "GNI"]]

# Target
y = df["HDI"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)

print("\nR2 Score:", round(r2_score(y_test, pred), 4))

# Save model
joblib.dump(model, "model/hdi_model.pkl")

print("\nModel Saved Successfully!")
