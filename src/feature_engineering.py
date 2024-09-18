import pandas as pd

def preprocess_data(data):
    data['Monthly Income'] = data['Income'].resample('M').sum()
    data['Monthly Expenses'] = data['Expenses'].resample('M').sum()
    data['Balance'] = data['Monthly Income'] - data['Monthly Expenses']
    return data

def feature_engineering(data):
    data['Savings Rate'] = data['Balance'] / data['Monthly Income']
    data['Projected Savings'] = data['Savings Rate'] * 12
    return data
