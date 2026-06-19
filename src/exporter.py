import pandas as pd

def export_data(df, analysis):
    try:
        df.to_csv("output/cleaned_data.csv", index = False)
        print("Cleaned data saved successfully")
    except FileNotFoundError:
        print("File not found")

    with open("output/report.txt", "w") as file:
        file.write("====== Employee Analytics Report ======\n\n")
        file.write(f"Total Employees: {len(df)}\n")
        file.write("\n")
        file.write(f"Average Salary: {analysis["average_salary"]}\n")
        file.write("\n")
        file.write(f"Highest Salary: {analysis["highest_salary"]}\n")
        file.write("\n")
        file.write(f"Lowest Salary: {analysis["lowest_salary"]}\n")
        file.write("\n")
        file.write(f"Average Rating: {analysis["average_rating"]}\n")
        file.write("\n")
        file.write(f"Average Leaves: {analysis["average_leaves"]}\n")
        file.write("\n")
        file.write(f"Average Overtime: {analysis["average_overtime"]}\n")
        file.write("\n")
        file.write("Department-wise Employee Count:\n")
        file.write(analysis["department_employee_count"].to_string())
        file.write("\n\n")
        file.write("Department-wise Average Salary:\n")
        file.write(analysis["department_average_salary"].to_string())
        file.write("\n\n")
        file.write("Top Performer:\n")
        file.write(analysis["top10"].to_string())
        file.write("\n\n")
        file.write("Bottom Performer:\n")
        file.write(analysis["bottom10"].to_string())
        file.write("\n\n")
        
