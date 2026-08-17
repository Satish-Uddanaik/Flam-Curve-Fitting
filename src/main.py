import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from curve import generate_curve
import numpy as np
import matplotlib.pyplot as plt

from plot import plot_results

from optimizer import optimize_parameters
# Read CSV
# df = pd.read_csv("../data/UVCE_BTech_Flam_Resource.csv")

df = pd.read_csv(
    "../data/UVCE_BTech_Flam_Resource.csv",
    sep="\t",
    header=None,
    names=["x", "y"]
)



# Basic Information
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.describe())

# Convert to NumPy arrays
x_actual = df["x"].to_numpy()
y_actual = df["y"].to_numpy()

# Plot
plt.figure(figsize=(8,6))
plt.scatter(x_actual, y_actual, s=8)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Actual Curve Points")
plt.grid(True)
plt.show()



#-----
# mathematical model

# Sample values for testing
theta = np.deg2rad(25)
M = 0.01
X = 80

# Generate t values
t = np.linspace(6, 60, 1000)

# Generate curve
x_pred, y_pred = generate_curve(theta, M, X, t)

# Plot generated curve
plt.figure(figsize=(8,6))

plt.plot(x_pred, y_pred, color="red", label="Generated Curve")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Generated Curve from Equation")

plt.grid(True)
plt.legend()

plt.show()


result = optimize_parameters(x_actual, y_actual)

print("\nOptimizer Information")
print("---------------------")
print("Success :", result.success)
print("Message :", result.message)
print("Iterations :", result.nit)
print("Function Evaluations :", result.nfev)

theta, M, X = result.x

print("Optimization Complete")
print("----------------------")

print(f"Theta (degrees): {np.rad2deg(theta):.4f}")
print(f"M: {M:.6f}")
print(f"X: {X:.6f}")
print(f"L1 Loss: {result.fun:.6f}")



# Generate predicted curve using optimized parameters
t = np.linspace(6, 60, len(x_actual))

x_pred, y_pred = generate_curve(theta, M, X, t)

# Plot Actual vs Predicted
plt.figure(figsize=(8,6))

plt.scatter(
    x_actual,
    y_actual,
    s=8,
    color="blue",
    label="Actual Data"
)

plt.plot(
    x_pred,
    y_pred,
    color="red",
    linewidth=2,
    label="Predicted Curve"
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Actual vs Predicted Curve")
plt.grid(True)
plt.legend()

plt.savefig("../output/actual_vs_predicted.png", dpi=300)
plt.show()




t = np.linspace(6, 60, len(x_actual))

x_pred, y_pred = generate_curve(theta, M, X, t)

plot_results(
    x_actual,
    y_actual,
    x_pred,
    y_pred
)