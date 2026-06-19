# Employee Performance Analytics Dashboard

## 📌 Overview

The **Employee Performance Analytics Dashboard** is a Python-based data analytics project that processes employee datasets to generate meaningful business insights. The application performs data cleaning, analyzes employee performance metrics, visualizes trends using charts, and exports reports.

This project demonstrates practical use of Python for data analysis and is designed to showcase skills relevant to Python and Data Analytics internships.

---

## ✨ Features

* Load employee data from CSV files
* Remove duplicate records
* Handle missing values
* Validate and clean invalid data
* Calculate employee performance scores
* Analyze salary and department statistics
* Identify top-performing employees
* Generate multiple data visualizations
* Export cleaned datasets
* Generate an analytics report

---

## 🛠️ Tech Stack

* Python
* Pandas
* Matplotlib

---

## 📂 Project Structure

```text
employee-performance-dashboard/
│
├── data/
│   └── employees.csv
│
├── output/
│   ├── cleaned_data.csv
│   ├── report.txt
│   └── charts/
│       ├── department_count.png
│       ├── department_salary.png
│       ├── performance_distribution.png
│       ├── rating_distribution.png
│       ├── salary_distribution.png
│       └── top10.png
│
├── src/
│   ├── loader.py
│   ├── cleaner.py
│   ├── analyzer.py
│   ├── visualizer.py
│   ├── exporter.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## 📊 Analytics Performed

* Total Employees
* Average Salary
* Highest Salary
* Lowest Salary
* Average Employee Rating
* Average Leaves
* Average Overtime Hours
* Department-wise Employee Count
* Department-wise Average Salary
* Top 10 Employees by Rating
* Bottom 10 Employees by Rating
* Performance Score Calculation
* Top 10 Performers

---

## 📈 Visualizations

The project generates the following charts:

* Department-wise Employee Count
* Average Salary by Department
* Salary Distribution
* Rating Distribution
* Performance Score Distribution
* Top 10 Performers

All charts are automatically saved in the `output/charts/` directory.

---

## 🧮 Performance Score Formula

The employee performance score is calculated using:

```text
Performance Score =
(Tasks Completed × 2)
+ (Working Hours × 0.5)
+ (Rating × 20)
− (Leaves × 5)
+ (Overtime Hours × 1.5)
```

---

## 🎯 Learning Outcomes

Through this project, I strengthened my understanding of:

* Data Cleaning with Pandas
* Data Analysis
* Data Visualization using Matplotlib
* CSV File Handling
* Modular Python Programming
* Exception Handling
* Project Structure and Code Organization

---

## 👨‍💻 Author

**Shubham Singh**

If you found this project useful or have suggestions for improvement, feel free to connect or share your feedback.
