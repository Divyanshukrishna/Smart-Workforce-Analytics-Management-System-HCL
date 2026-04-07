import pandas as pd
import numpy as np

class AnalyticsEngine:
    def __init__(self, db_manager):
        self.conn = db_manager.conn

    def load_data(self):
        return pd.read_sql_query("SELECT * FROM employees", self.conn)

    def basic_stats(self, df):
        salaries = df['salary'].values
        return {
            "mean": np.mean(salaries),
            "median": np.median(salaries),
            "std": np.std(salaries)
        }

    def department_analysis(self, df):
        return df.groupby("department")["salary"].mean()

    def correlation(self, df):
        return df.corr(numeric_only=True)


    def normalize_salary(self, df):
        salaries = df['salary'].values
        return (salaries - np.mean(salaries)) / np.std(salaries)