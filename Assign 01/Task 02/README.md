# Logistic Regression Project

This project demonstrates the implementation of **Logistic Regression** using Python and scikit-learn.

---

## Project Structure
The project includes:
- Data loading
- Exploratory Data Analysis (EDA)
- Feature preprocessing (handling categorical and numerical variables)
- Logistic Regression modeling
- Model evaluation (accuracy)

---

## Logistic Regression: The Math Behind It

Logistic Regression is used for **binary classification** problems.  
Instead of predicting continuous values, it predicts the probability of a class.

### 1. Linear Combination  
We first compute a linear function:  

$$ z = w^T x + b $$

where:  
- $x$ = input features  
- $w$ = weights  
- $b$ = bias  

### 2. Sigmoid Function  
To map predictions to probabilities between 0 and 1, we use the sigmoid function:  

$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$

Thus, the probability of class 1 is:  

$$ P(y=1|x) = \sigma(w^T x + b) $$

### 3. Decision Boundary  
If $P(y=1|x) \geq 0.5$, predict class 1, else predict class 0.

### 4. Cost Function (Log Loss)  
The cost function is based on likelihood estimation:  

$$ J(w, b) = -\frac{1}{m} \sum_{i=1}^{m} \Big[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \Big] $$

where $\hat{y}^{(i)}$ is the predicted probability.

### 5. Gradient Descent Update  
Weights are updated to minimize the cost:  

$$ w := w - \alpha \frac{\partial J}{\partial w}, \quad b := b - \alpha \frac{\partial J}{\partial b} $$

---

# Result

Trained a Logistic Regression model on a clean loan approval dataset and achieved 89% accuracy test data.

---