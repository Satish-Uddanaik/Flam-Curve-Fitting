# Flam Curve Fitting Assignment

## Overview

This project is a solution for the **Flam Curve Fitting Assessment**.

The objective is to estimate the unknown parameters **θ (Theta)**, **M**, and **X** of a given parametric curve using the provided dataset of 1500 sampled points.

The solution reads the dataset, generates the mathematical curve, optimizes the unknown parameters using SciPy, and visualizes the actual and predicted curves.

---

## Problem Statement

The given parametric equations are:

\[
x = t\cos(\theta) - e^{M|t|}\sin(0.3t)\sin(\theta) + X
\]

\[
y = 42 + t\sin(\theta) + e^{M|t|}\sin(0.3t)\cos(\theta)
\]

### Unknown Parameters

- θ (Theta)
- M
- X

### Parameter Constraints

| Parameter | Range |
|-----------|----------------|
| θ | 0° to 50° |
| M | -0.05 to 0.05 |
| X | 0 to 100 |
| t | 6 to 60 |

---

## Project Structure

```
Flam-Curve-Fitting/
│
├── data/
│   └── UVCE_BTech_Flam_Resource.csv
│
├── output/
│   └── final_result.png
│
├── src/
│   ├── curve.py
│   ├── optimizer.py
│   ├── plot.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python 3.x
- NumPy
- Pandas
- SciPy
- Matplotlib

---

## Approach

### Step 1

Load the dataset using Pandas.

### Step 2

Explore the dataset.

- Number of points
- Missing values
- Data types
- Statistical summary

### Step 3

Visualize the actual curve using a scatter plot.

### Step 4

Implement the provided mathematical equations in `curve.py`.

### Step 5

Define an L1 Loss function.

### Step 6

Use **SciPy's L-BFGS-B optimizer** to estimate:

- Theta
- M
- X

### Step 7

Generate the predicted curve.

### Step 8

Visualize the actual and predicted curves together.

---

## Optimization Method

The optimization minimizes the **Mean L1 Distance** between the actual points and the generated curve.

Optimization Algorithm:

- L-BFGS-B

---

## Current Output

Example output:

```
Optimization Complete

Theta (degrees): 28.1185
M: 0.021390
X: 54.900576

L1 Loss: 25.243396
```

---

## Visualization

The program generates a comparison graph showing:

- Blue Points → Actual Dataset
- Red Curve → Predicted Curve

The output image is saved in:

```
output/final_result.png
```

---

## How to Run

### 1. Clone Repository

```bash
git clone <your_repository_url>
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run

```bash
cd src

python main.py
```

---

## Results

The application performs the following tasks:

- Reads the dataset
- Generates the mathematical curve
- Optimizes unknown parameters
- Computes L1 Loss
- Displays comparison graph
- Saves the final visualization

---

## Future Improvements

- Improve parameter optimization to reduce the L1 Loss.
- Experiment with multiple optimization algorithms.
- Improve point correspondence between sampled and generated curves.
- Add interactive parameter tuning.
- Export optimized parameters to a JSON file.

---

## Author

**Satish Uddanaik**

Information Science & Engineering

GitHub:(https://github.com/Satish-Uddanaik)
