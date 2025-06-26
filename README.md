# mental-health-prediction-app
A simple machine learning model to predict if a person has a healthy mental state based on their routine.

## Jupyter Notebook
Contains sections for checking the type of each column to see if they are numerical, splitting data into X and y, creating model with logistic regression, and testing the model performance.

## Main.py
Creates the web app using streamlist that uses the model to perform a prediction based on the input from the user.

## How to run

Create a virtual environment then:

```bash
pip install -r requirements.txt
```

Run:
```bash
streamlit run main.py
```