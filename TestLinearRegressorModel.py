import unittest
import pandas as pd
from sklearn.model_selection import train_test_split
from LinearRegressionModel import LinearRegressionModel
class TestLinearTreeRegressorModel(unittest.TestCase):
    def setUp(self):
        # Load the prepared data for testing
        data = pd.read_csv('C:/Users/ayari/NoteBook_Py/Py_Ensi/PS_Tayara/Prepared_voitures.csv')

        # Split the data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            data.drop('Prix', axis=1), data['Prix'], test_size=0.2, random_state=42)

        # Initialize the DecisionTreeRegressorModel
        self.LRM = LinearRegressionModel()

    def test_train_model(self):
        # Test if the model can be trained without errors
        self.LRM.train_model()

    def test_evaluate_model(self):
        # Train the model
        self.LRM.train_model()

        # Evaluate the model on the test set
        self.LRM.evaluate_model(self.X_test, self.y_test)

    def test_predict_price(self):
        # Train the model
        self.LRM.train_model()

        # Create new data for prediction
        new_data = pd.DataFrame([[1.2, 5, 200000, 14, 'Essence', 'Manuelle', 'Seat', 'Gris', 'Ibiza', 2010]],
                                columns=['Cylindre', 'Puissance', 'Kilometrage', 'Age', 'Carburant', 'TypeBoite', 'Marque_voiture', 'Couleur', 'Modele', 'Annee'])

        # Predict the price for new data
        predicted_price = self.LRM.predict_price(new_data)
        self.assertIsInstance(predicted_price, float, "Predicted price should be a float.")

if __name__ == '__main__':
    unittest.main()
