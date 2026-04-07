import matplotlib.pyplot as plt

class ReportGenerator:
    def __init__(self, df):
        self.df = df

    def bar_chart(self):
        self.df.groupby("department")["salary"].mean().plot(kind='bar')
        plt.title("Avg Salary by Department")
        plt.savefig("bar_chart.png")
        plt.clf()

    def scatter_plot(self):
        plt.scatter(self.df["age"], self.df["salary"])
        plt.xlabel("Age")
        plt.ylabel("Salary")
        plt.title("Age vs Salary")
        plt.savefig("scatter_plot.png")
        plt.clf()

    def histogram(self):
        plt.hist(self.df["salary"])
        plt.title("Salary Distribution")
        plt.savefig("histogram.png")
        plt.clf()

    def pie_chart(self):
        self.df["department"].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title("Department Distribution")
        plt.savefig("pie_chart.png")
        plt.clf()