# Pandas Challenge: Analyzing Student Grades

This challenge will help you practice filtering, sorting, and grouping data using Pandas.  
You will work with a CSV file called `grades.csv` containing student grades.

## Example Data

Your `grades.csv` file should look like this:

```
Name,Subject,Score,Year
Alice,Math,85,2024
Bob,Math,78,2024
Alice,English,92,2024
Bob,English,88,2024
Charlie,Math,90,2024
Charlie,English,85,2024
```

---

## Part 1: Load the Data

- Import pandas and load the `grades.csv` file into a DataFrame.
- Print the first 5 rows.

---

## Part 2: Filtering

- Filter the DataFrame to show only the rows where the `Score` is greater than 85.
- Print the result.

---

## Part 3: Sorting

- Sort the DataFrame by `Score` in descending order.
- Print the top 3 rows.

---

## Part 4: Grouping and Aggregation

- Group the data by `Name` and calculate the average score for each student.
- Print the result.

---

## Part 5: Challenge Extension

- Which student has the highest average score? Print their name and average score.

---

**Tip:**  
You may want to use these Pandas methods:  
- `.read_csv()`  
- `.loc[]`  
- `.sort_values()`  
- `.groupby()`  
- `.mean()`

Good luck!