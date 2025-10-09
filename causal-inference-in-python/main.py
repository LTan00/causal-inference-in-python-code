import pandas as pd

# Write a function, generate_data(), that return a pandas dataframe with three columns, t, x, and y, and six rows with values of (0, 0, 200), (0, 0, 120), (0, 1, 300), (1, 0, 500), (1, 0, 600), and (1, 1, 800).
# Save it as main.py and submit to Gradescope
# Function signature:


def generate_data():
    data = {
        't': [0, 0, 0, 1, 1, 1],
        'x': [0, 0, 1, 0, 0, 1],
        'y': [200, 120, 300, 500, 600, 800]
    }
    df = pd.DataFrame(data)
    return df

generate_data()