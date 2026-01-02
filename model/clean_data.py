import pandas as pd

data = pd.read_csv(
    '../dataset/food_nutrition_dataset.csv',
    on_bad_lines='skip'
)

# Remove missing & duplicates
data = data.dropna()
data = data.drop_duplicates()

data = data.rename(columns={
    'Food_Item': 'Food',
    'Calories (kcal)': 'Calories',
    'Protein (g)': 'Protein',
    'Carbohydrates (g)': 'Carbs',
    'Fat (g)': 'Fat',
    'Fiber (g)': 'Fiber',
    'Sugars (g)': 'Sugars',
    'Cholesterol (mg)': 'Cholesterol'
})

# Keep only required columns
data = data[['Food', 'Calories', 'Protein', 'Carbs', 'Fat', 'Fiber', 'Sugars', 'Cholesterol']]

# Clean text
data['Food'] = data['Food'].str.lower()

# Convert numeric columns
cols = ['Calories', 'Protein', 'Carbs', 'Fat', 'Fiber', 'Sugars', 'Cholesterol']
for col in cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Remove rows with conversion errors
data = data.dropna()

# Save cleaned data
data.to_csv('../dataset/cleaned_food_data.csv', index=False)

print("Cleaning completed successfully!")
print(data.head(10))
print("Final shape:", data.shape)
