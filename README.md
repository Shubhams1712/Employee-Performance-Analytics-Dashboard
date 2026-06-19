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

## 📈 Charts

<img width="320" height="240" alt="Department wise employee count" src="https://github.com/user-attachments/assets/b53ca3b5-27cd-47cd-bd4b-ef484aa0e4b7" />
<img width="320" height="240" alt="Department wise salary count" src="https://github.com/user-attachments/assets/68e435c3-3cf3-4cf9-a0b2-9878f031245c" />
<img width="320" height="240" alt="Employees Rating" src="https://github.com/user-attachments/assets/cd151060-2a0b-4eb1-aed6-55d8a677865b" />
<img width="320" height="240" alt="Salary Record" src="https://github.com/user-attachments/assets/6da8c4fb-0461-4f5b-9c66-9cf47aff4c29" />
<img width="320" height="240" alt="Top 10 Employees" src="https://github.com/user-attachments/assets/a1b9ebee-c21b-44fb-88ec-e17b46bad034" />


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
