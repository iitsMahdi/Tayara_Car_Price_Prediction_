import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor  # Import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
data = pd.read_csv('C:/Users/ayari/NoteBook_Py/Py_Ensi/PS_Tayara/Prepared_voitures.csv')

# Separate features and target variable
X = data.drop('Prix', axis=1)
y = data['Prix']

# Create a column transformer with transformers for numerical and categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Kilometrage', 'Annee', 'Cylindre', 'Puissance', 'Age']),
        ('cat', OneHotEncoder(drop='first', sparse=False), ['Marque_voiture', 'Modele', 'Couleur', 'TypeBoite', 'Carburant'])
    ])

# Create a pipeline with the preprocessor and the XGBRegressor model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', XGBRegressor(random_state=42))  # Use XGBRegressor here
])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the pipeline on the entire dataset
model.fit(X, y)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("XGBRegressor Results:")
print('R² Score: ' + str(round(r2 * 100)) + "%" + ', Root Mean Squared Error: ' + str(rmse))

new_data = pd.DataFrame([[1.2, 5, 200000, 14, 'Essence', 'Manuelle', 'Seat', 'Gris', 'Ibiza', 2010]],
                        columns=['Cylindre', 'Puissance', 'Kilometrage', 'Age', 'Carburant', 'TypeBoite', 'Marque_voiture', 'Couleur', 'Modele', 'Annee'])

label_encoding_columns = ['Carburant', 'TypeBoite', 'Marque_voiture', 'Couleur', 'Modele']

# Convert categorical features to numerical using label encoding
for col in label_encoding_columns:
    new_data[col] = pd.factorize(new_data[col])[0] + 1

predicted_price = model.predict(new_data)
print(f"Predicted Price: {predicted_price[0]}")
