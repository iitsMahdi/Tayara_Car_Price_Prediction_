import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class DataVisualizer:
    def __init__(self):
        self.data = pd.read_csv('C:/Users/ayari/NoteBook_Py/Py_Ensi/projet_tayara/cleaned_voitures.csv')

    def create_boxplot(self, x_col, y_col, figsize=(15, 7), **kwargs):
        plt.subplots(figsize=figsize)
        ax = sns.boxplot(x=x_col, y=y_col, data=self.data, **kwargs)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha='right')
        plt.show()

    def create_swarmplot(self, x_col, y_col, figsize=(20, 10), **kwargs):
        plt.subplots(figsize=figsize)
        ax = sns.swarmplot(x=x_col, y=y_col, data=self.data, **kwargs)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha='right')
        plt.show()

    def create_relplot(self, x_col, y_col, height=7, aspect=1.5, **kwargs):
        sns.relplot(x=x_col, y=y_col, data=self.data, height=height, aspect=aspect, **kwargs)
        plt.show()

    def create_fuel_boxplot(self, figsize=(14, 7), **kwargs):
        plt.subplots(figsize=figsize)
        sns.boxplot(x='Carburant', y='Prix', data=self.data, **kwargs)
        plt.show()

    def create_mixed_relplot(self, figsize=(15, 7), **kwargs):
        ax = sns.relplot(x='Marque_voiture', y='Prix', data=self.data, hue='Carburant', height=7,
                         aspect=2, **kwargs)
        ax.set_xticklabels(rotation=40, ha='right')
        plt.show()