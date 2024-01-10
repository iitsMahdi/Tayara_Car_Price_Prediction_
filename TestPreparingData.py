import unittest
import pandas as pd
from datetime import datetime
from Preparing import PreparingData

class TestPreparingData(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        data = {
            'Annee': [2010, 2020, 2030],
            'Cylindre': ['2L', '3L', '4L'],
            'Carburant': ['Essence', 'Diesel', 'Hybrid'],
            'TypeBoite': ['Manuelle', 'Automatique', 'Manuelle'],
            'Marque_voiture': ['Toyota', 'Honda', 'Toyota'],
            'Couleur': ['Rouge', 'Bleu', 'Gris'],
            'Puissance': [100, '120', '30'],
            'Kilometrage': [50000, '60000', '70000'],
            'Prix': [15000, 20000, 25000]
        }
        self.df = pd.DataFrame(data)
        self.preparer = PreparingData(self.df)

    def test_clean_cylindre_column(self):
        self.preparer.clean_cylindre_column()
        self.assertTrue(pd.api.types.is_numeric_dtype(self.preparer.df['Cylindre']))  # Check if 'Cylindre' is converted to numeric

    def test_clean_carburant_column(self):
        self.preparer.clean_carburant_column()
        self.assertTrue(self.preparer.df['Carburant'].isin(['Diesel', 'Essence']).all())  # Check if only 'Diesel' and 'Essence' are kept

    def test_clean_type_boite_column(self):
        self.preparer.clean_type_boite_column()
        self.assertTrue(self.preparer.df['TypeBoite'].isin(['Manuelle', 'Automatique']).all())  # Check if only 'Manuelle' and 'Automatique' are kept

    def test_filter_marque_and_couleur_columns(self):
        self.preparer.filter_marque_and_couleur_columns()
        self.assertTrue(~self.preparer.df['Marque_voiture'].str.isnumeric().all())  # Check if numeric values are removed from 'Marque_voiture'
        self.assertTrue(~self.preparer.df['Couleur'].str.isnumeric().all())  # Check if numeric values are removed from 'Couleur'

    def test_clean_and_filter_puissance_column(self):
        self.preparer.clean_and_filter_puissance_column()
        invalid_values = self.preparer.df['Puissance'][~self.preparer.df['Puissance'].between(1, 100)]
        self.assertTrue(invalid_values.empty, f"Invalid values found: {invalid_values}")

    # Add more test methods for other functions

if __name__ == '__main__':
    unittest.main()
