import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle

class RandomForestRegressorModel:
    def __init__(self):
        # Initialize the model pipeline
        self.model = self._create_pipeline()

    def _create_pipeline(self):
        # Create a column transformer with transformers for numerical and categorical features
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), ['Kilometrage', 'Annee', 'Cylindre', 'Puissance', 'Age']),
                ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'),
                 ['Marque_voiture', 'Modele', 'Couleur', 'TypeBoite', 'Carburant'])
            ])

        # Create a pipeline with the preprocessor and the model
        model_pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('regressor', RandomForestRegressor())])

        return model_pipeline

    def train_model(self):
        # Load the data
        data = pd.read_csv('C:/Users/ayari/NoteBook_Py/Py_Ensi/PS_Tayara/Prepared_voitures.csv')

        # Separate features and target variable
        X = data.drop('Prix', axis=1)
        y = data['Prix']

        # Fit the pipeline on the entire dataset
        self.model.fit(X, y)

    def evaluate_model(self, X_test, y_test):
        # Make predictions on the test set
        y_pred = self.model.predict(X_test)

        # Evaluate the model
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)

        print("Random Forest Regressor Results:")
        print('R² Score: ' + str(round(r2 * 100)) + "%" + ' , Root Mean Squared Error :' + str(rmse))

    def predict_price(self, new_data):
        # Define the list of columns to encode
        label_encoding_columns = ['Carburant', 'TypeBoite', 'Marque_voiture', 'Couleur', 'Modele']

        # Convert categorical features to numerical using label encoding
        for col in label_encoding_columns:
            new_data[col] = pd.factorize(new_data[col])[0] + 1

        # Make predictions
        predicted_price = self.model.predict(new_data)

        return predicted_price[0]

    def save_model(self, filename='RandomForestRegressorModel.pkl'):
        # Save the model using pickle
        with open(filename, 'wb') as file:
            pickle.dump(self.model, file)

    def load_model(self, filename='RandomForestRegressorModel.pkl'):
        # Load the model using pickle
        with open(filename, 'rb') as file:
            self.model = pickle.load(file)
