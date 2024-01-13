# main.py
from TayaraScraper import TayaraScraper
from Preparing import PreparingData
from RandomForestRegressorModel import RandomForestRegressorModel
from DecisionTreeRegressorModel import DecisionTreeRegressorModel
from LinearRegressionModel import LinearRegressionModel
import pandas as pd
from sklearn.model_selection import train_test_split

from Visualisation import DataVisualizer


def main():
    try:
        # # Scraping
        # scraper = TayaraScraper()
        # scraper.scrape_links()
        # scraper.scrape_cars()
        # scraper.export_to_csv("C:/Users/ayari/NoteBook_Py/Py_Ensi/PS_Tayara/voitures.csv")
        #
        # # Preparing
        # preparer = PreparingData()
        #
        # preparer.drop_duplicates()
        # preparer.drop_nan_columns()
        # preparer.drop_columns_by_year()
        # preparer.cleaning_model_column()
        # preparer.clean_cylindre_column()
        # preparer.clean_carburant_column()
        # preparer.clean_type_boite_column()
        # preparer.filter_marque_and_couleur_columns()
        # preparer.clean_and_filter_puissance_column()
        # preparer.add_age_column()
        # preparer.filter_valid_year_column()
        # preparer.clean_prix_column()
        # preparer.convert_kilometrage_column()
        # prepared_data = preparer.df
        # prepared_data.to_csv('C:/Users/ayari/NoteBook_Py/Py_Ensi/PS_Tayara/Cleaned_voitures.csv', index=False)

        data_visualizer = DataVisualizer()
         # Create a boxplot
        data_visualizer.create_boxplot(x_col='Marque_voiture', y_col='Prix', figsize=(15, 7))
        #
        # # Create a swarmplot
        data_visualizer.create_swarmplot(x_col='Annee', y_col='Prix', figsize=(20, 10))
        #
        # # Create a relplot
        data_visualizer.create_relplot(x_col='Kilometrage', y_col='Prix', height=7, aspect=1.5)
        #
        # # Create a fuel_type boxplot
        data_visualizer.create_fuel_boxplot(figsize=(14, 7))
        #
        # # Create a mixed relplot
        data_visualizer.create_mixed_relplot(figsize=(15, 7))

        # preparer.encode_type_boite_column()
        # preparer.encode_type_carburant()
        # preparer.encode_marque_column()
        # preparer.encode_couleur()
        # preparer.encode_modele()
        #
        #
        #
        # prepared_data = preparer.df
        # prepared_data.to_csv('C:/Users/ayari/NoteBook_Py/Py_Ensi/PS_Tayara/Prepared_voitures.csv', index=False)

        # Split the data into training and testing sets
        data = pd.read_csv('C:/Users/ayari/NoteBook_Py/Py_Ensi/PS_Tayara/Prepared_voitures.csv')
        X_train, X_test, y_train, y_test = train_test_split(data.drop('Prix', axis=1), data['Prix'], test_size=0.2, random_state=42)

        # Car Price Prediction
        RFRM = RandomForestRegressorModel()
        RFRM.train_model()

        DTRM = DecisionTreeRegressorModel()
        DTRM.train_model()  # Updated line for training

        LRM = LinearRegressionModel()
        LRM.train_model()

        # Evaluate the models
        RFRM.evaluate_model(X_test, y_test)
        LRM.evaluate_model(X_test, y_test)
        DTRM.evaluate_model(X_test, y_test)

        # Save the trained model
        RFRM.save_model()

        # Load the model
        RFRM.load_model()

        # New data for prediction
        new_data = pd.DataFrame([[1.0, 4, 72000, 4, 'Essence', 'Manuelle', 'Suzuki', 'Bleu', 'Celerio', 2020]],
                                columns=['Cylindre', 'Puissance', 'Kilometrage', 'Age', 'Carburant', 'TypeBoite', 'Marque_voiture', 'Couleur', 'Modele', 'Annee'])

        # Predict the price for new data
        predicted_price = RFRM.predict_price(new_data)  # Updated line for prediction
        print(f"Predicted Price (Decision Tree): {predicted_price}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
