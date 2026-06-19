import matplotlib.pyplot as plt
import pandas as pd

def visualize_data(df):
    department = df["Department"].value_counts()
    plt.bar(department.index, department.values)
    plt.xticks(rotation=35)
    plt.xlabel("Department")
    plt.ylabel("Department Count")
    plt.title("Employees by Department")
    plt.tight_layout()
    plt.savefig("output/charts/department_count.png")
    plt.close()

    performance_dist = df["Performance_Score"]
    plt.hist(performance_dist, bins=20, alpha=0.5, label='Dataset 1', color='blue')
    plt.legend()
    plt.xlabel("Performance Score")
    plt.ylabel("Number of Employees")
    plt.title("Performance Score Distribution")
    plt.tight_layout()
    plt.savefig("output/charts/department_count.png")
    plt.close()

    salary = df["Salary"]
    plt.hist(salary, bins = 20, color = 'teal')
    plt.savefig("output/charts/salary_record.png")
    plt.close()

    rating = df["Rating"]
    plt.hist(rating, bins=10, color='royalblue')
    plt.title("Rating of Employees")
    plt.savefig("output/charts/Employees-rating.png")
    plt.close()

    department_salary = df.groupby("Department")["Salary"].mean()
    plt.bar(department_salary.index, department_salary.values)
    plt.savefig("output/charts/department-salary.png")
    plt.close()

    top10 = df.sort_values("Performance_Score", ascending=False).head(10)
    plt.barh(top10["Name"], top10["Performance_Score"])
    plt.xlabel("Performance Score")
    plt.ylabel("Employee Name")
    plt.title("Top 10 Performers")
    plt.tight_layout()
    plt.savefig("output/charts/top10.png")
    plt.close()
