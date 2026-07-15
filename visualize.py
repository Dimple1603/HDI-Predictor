import os
import pandas as pd
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore

# Create output folder
os.makedirs("visualizations", exist_ok=True)

# Load dataset
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

# Select required columns
df = df[["HDI", "Life", "Expected", "Mean", "GNI"]]

# Replace missing values represented as ".."
df.replace("..", pd.NA, inplace=True)

# Convert to numeric
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove missing values
df.dropna(inplace=True)

print("Rows after cleaning:", len(df))

# ------------------------------------
# 1. Distribution Plot
# ------------------------------------
plt.figure(figsize=(8,5))
plt.hist(df["HDI"], bins=10)
plt.title("Distribution of HDI")
plt.xlabel("HDI")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("visualizations/distribution_plot.png")
plt.close()

# ------------------------------------
# 2. Scatter Plot
# ------------------------------------
plt.figure(figsize=(8,5))
plt.scatter(df["Life"], df["HDI"])
plt.title("Life Expectancy vs HDI")
plt.xlabel("Life Expectancy")
plt.ylabel("HDI")
plt.tight_layout()
plt.savefig("visualizations/scatter_plot.png")
plt.close()

# ------------------------------------
# 3. Strip Plot
# ------------------------------------
plt.figure(figsize=(8,5))
sns.stripplot(y=df["HDI"])
plt.title("HDI Strip Plot")
plt.tight_layout()
plt.savefig("visualizations/strip_plot.png")
plt.close()

# ------------------------------------
# 4. Correlation Heatmap
# ------------------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visualizations/correlation_heatmap.png")
plt.close()

# ------------------------------------
# 5. Correlation Matrix CSV
# ------------------------------------
corr = df.corr()
corr.to_csv("visualizations/correlation_matrix.csv")

print("\nVisualization files generated successfully!")
print("Saved in: visualizations/")