# House Price Regression Project

A small beginner-friendly Multiple Linear Regression project.

## Files
- `house_price_regression.csv` — dataset
- `house_price_regression.ipynb` — complete notebook
- `predict.py` — terminal application that asks for house details and predicts price
- `requirements.txt` — Python packages

## 1. Install
```bash
pip install -r requirements.txt
```

## 2. Run the terminal predictor
```bash
python predict.py
```

Example:
```text
Area in square feet: 1800
Number of bedrooms: 3
House age in years: 5
Distance from city center (km): 6

=======================================================
                  REGRESSION OUTPUT
=======================================================
Area       : 1800 sqft
Bedrooms   : 3
Age        : 5.0 years
Distance   : 6.0 km
-------------------------------------------------------
Predicted Price: ₹XXX.XX lakhs
=======================================================
```

## 3. Run the notebook
```bash
jupyter notebook house_price_regression.ipynb
```

## What you learn
1. Load a dataset
2. Inspect and clean data
3. Select features and target
4. Split train/test data
5. Train LinearRegression
6. Understand coefficients
7. Evaluate using MAE, RMSE and R²
8. Predict a new value
