import pandas as pd
import datetime


class PreparingData:
    def __init__(self):
        dfS = pd.read_csv('C:/Users/ayari/NoteBook_Py/Py_Ensi/PS_Tayara/voitures.csv')
        self.df = dfS if dfS is not None else pd.DataFrame()

    def drop_duplicates(self):
        self.df = self.df.drop_duplicates()

    def drop_nan_columns(self):
        self.df = self.df.dropna()
        self.df = self.df[~self.df.apply(lambda row: any(row == 'Autres'), axis=1)]
        self.df = self.df[~self.df.apply(lambda row: any(row == 'Autre'), axis=1)]

    def cleaning_model_column(self):
        model_pattern = r'\d+\.\d+L'  # Pattern to match models like "1.0L"
        mask = self.df['Modele'].str.match(model_pattern, na=False, case=False)
        self.df = self.df[~mask]

    def drop_columns_by_year(self):
        c = pd.to_datetime(self.df['Annee'], errors='coerce')
        current_year = datetime.datetime.now().year
        self.df = self.df[c.dt.year <= current_year]

    def clean_cylindre_column(self):
        self.df['Cylindre'] = self.df['Cylindre'].astype(str).str.replace('[<>L]', '', regex=True)
        self.df['Cylindre'] = pd.to_numeric(self.df['Cylindre'], errors='coerce')

    def clean_carburant_column(self):
        self.df = self.df[self.df['Carburant'].isin(['Diesel', 'Essence'])]

    def clean_type_boite_column(self):
        self.df = self.df[self.df['TypeBoite'].isin(['Manuelle', 'Automatique'])]

    def filter_marque_and_couleur_columns(self):
        self.df = self.df[~self.df['Marque_voiture'].str.isnumeric()]
        self.df = self.df[~self.df['Couleur'].str.contains('143.000|Avec kilométrage', na=False, case=False)]
        self.df = self.df[~self.df['Couleur'].str.isnumeric()]

    def clean_and_filter_puissance_column(self):
        def clean_and_filter_puissance(value):
            try:
                numeric_value = int(value)
                return numeric_value if 1 <= numeric_value <= 100 else 0
            except ValueError:
                return 0

        self.df['Puissance'] = self.df['Puissance'].apply(clean_and_filter_puissance)
        self.df = self.df[self.df['Puissance'] != 0]

    def filter_valid_year_column(self):
        valid_year_pattern = r'^\d{4}$'
        self.df["Annee"] = self.df["Annee"].astype(str)  # Convert to string
        self.df = self.df[self.df['Annee'].str.match(valid_year_pattern)]
        self.df["Annee"] = self.df["Annee"].astype(int)

    def add_age_column(self):
        c = pd.to_datetime(self.df['Annee'], errors='coerce')
        current_year = datetime.datetime.now().year
        self.df['Age'] = current_year - c.dt.year

    def clean_prix_column(self):
        self.df["Prix"] = self.df["Prix"].replace(',', '').astype(int)

        def add_zeros_to_prix(value):
            if len(str(value)) in range(1, 4):
                return str(value) + "000"
            else:
                return value

        self.df['Prix'] = self.df['Prix'].apply(add_zeros_to_prix)
        self.df["Prix"] = self.df["Prix"].astype(int)
        self.df = self.df[(self.df['Prix'] <= 9999999) & (self.df['Prix'] >= 0)]

    def convert_kilometrage_column(self):
        self.df['Kilometrage'] = pd.to_numeric(self.df['Kilometrage'], errors='coerce')
        self.df['Kilometrage'] = self.df['Kilometrage'].fillna(0).round().astype(int)
        self.df = self.df[self.df['Kilometrage'] >= 0]

    def encode_type_boite_column(self):
        # Convert 'TypeBoite' to binary (1 for automatic and 0 for manual)
        self.df['TypeBoite'] = (self.df['TypeBoite'] == 'Automatique').astype(int)

    def encode_type_carburant(self):
        # Convert 'Carburant' to binary (1 for Diesel and 0 for Essence)
        self.df['Carburant'] = (self.df['Carburant'] == 'Diesel').astype(int)

    def encode_marque_column(self):
        # Encode 'Marque_voiture' with numerical values starting from 1
        self.df['Marque_voiture'] = pd.factorize(self.df['Marque_voiture'])[0] + 1

    def encode_couleur(self):
        self.df['Couleur'] = pd.factorize(self.df['Couleur'])[0] + 1

    def encode_modele(self):
        self.df['Modele'] = pd.factorize(self.df['Modele'])[0] + 1
        self.df.fillna(0, inplace=False)
