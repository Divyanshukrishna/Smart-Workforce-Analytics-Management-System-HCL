from employee import Employee
from database import DatabaseManager
from analytics import AnalyticsEngine
from report import ReportGenerator


def main():
    db = DatabaseManager()

    # Sample data (run once)
    db.add_employee(Employee("Divyanshu", 21, "IT", 50000))
    db.add_employee(Employee("Rahul", 25, "HR", 40000))
    db.add_employee(Employee("Sneha", 23, "Finance", 45000))
    db.add_employee(Employee("Amit", 30, "IT", 60000))
    

    print("\nAll Employees:")
    for emp in db.get_all_employees():
        print(emp)

    # Analytics
    analytics = AnalyticsEngine(db)
    df = analytics.load_data()

    print("\nBasic Stats:")
    print(analytics.basic_stats(df))

    print("\nDepartment Analysis:")
    print(analytics.department_analysis(df))
    print("\nCorrelation:")
    print(analytics.correlation(df))

    # Reports
    report = ReportGenerator(df)
    report.bar_chart()
    report.scatter_plot()
    report.histogram()
    report.pie_chart()

    print("\nReports Generated Successfully!")


if __name__ == "__main__":
    main()
