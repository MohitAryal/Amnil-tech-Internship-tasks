
# Linear Regression Project

This project demonstrates the implementation of **Linear Regression** using Python.

## Project Overview
The notebook explores the concept of linear regression, fits a model, and evaluates its performance using metrics.

## Math Behind Linear Regression

Linear regression tries to model the relationship between a dependent variable **y** and one or more independent variables **x** by fitting a linear equation:

$$
y = \beta_0 + \beta_1 x + \epsilon
$$

Where:
- $y$ = dependent variable (target)
- $x$ = independent variable (feature)
- $\beta_0$ = intercept
- $\beta_1$ = slope (coefficient)
- $\epsilon$ = error term

### Objective
We want to minimize the **Residual Sum of Squares (RSS):**

$$
RSS = \sum_{i=1}^{n} (y_i - (\beta_0 + \beta_1 x_i))^2
$$

### Solution
To find the optimal parameters, we use the **Ordinary Least Squares (OLS)** method. The closed-form solution for coefficients is:

$$
\hat{\beta} = (X^T X)^{-1} X^T y
$$

Where:
- $X$ = feature matrix (with a column of ones for intercept)
- $y$ = target vector
- $\hat{\beta}$ = estimated coefficients

This ensures that the fitted line minimizes the squared differences between actual and predicted values.

## Requirements
- Python
- Pandas
- Matplotlib
- Scikit-learn

---
