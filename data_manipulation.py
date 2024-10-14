A script that loads a CSV file and performs basic data cleaning (handling missing values, filtering).

2. **Create `data_manipulation.py`:**
   - Create a new file named `data_manipulation.py`.
   - Add the following content:

```python
# data_manipulation.py
import pandas as pd

# Load the CSV file
df = pd.read_csv('sample_data.csv')

# Display the first few rows of the DataFrame
print("Initial Data:")
print(df.head())

# Handling missing values
print("\nHandling Missing Values:")
print("Before:")
print(df.isnull().sum())
df.fillna(method='ffill', inplace=True)  # Forward fill to handle missing values
print("After:")
print(df.isnull().sum())

# Filtering data (example: filter rows where a specific column meets a condition)
filtered_data = df[df['column_name'] > threshold_value]  # Replace with actual column name and value
print("\nFiltered Data:")
print(filtered_data)

