# [Find the middle element](middle_element_ex1)

Given a singly linked list, find the middle element of the list in
O(n) time complexity, where
n is the number of nodes in the linked list.

- If the number of nodes is odd, return the value of the middle node.
- If the number of nodes is even, return the value of the first of the two middle nodes.

# [Student Marks](student_marks)

You are provided with a CSV file that contains student data with the following columns:

`gender`: The gender of the student (either "Male" or "Female").

`maths`: The student's score in Maths.

`english`: The student's score in English.

## Your task is to:

### 1. Read the CSV File:

Use Python's built-in `open()` function to read the CSV file without relying on any additional libraries (such as pandas or csv).

### 2. Visualize Gender Distribution:

- Create a pie chart to show the distribution of students based on gender.

### 3. Pass/Fail Classification:

- A student is considered to have passed if the sum of their Maths and English scores is greater than 40, otherwise, they have failed.
- Create a pie chart to represent the distribution of students who have passed and failed.

# [Matrix Multiplication of Two 3x3 Matrices from CSV Files](matrix_multiplication)

This project reads two CSV files containing 3x3 matrices, multiplies them, and writes the result to a new CSV file using Python's built-in `open()` function.

## Your task is to:

### 1. Read CSV Files

Use Python’s built-in `open()` function to read two CSV files, where each file contains a 3x3 matrix.

### 2. Matrix Multiplication

Perform matrix multiplication on the two 3x3 matrices.

### 3. Store the Result

Write the result of the matrix multiplication to a new CSV file using Python's `open()` function.

# [List Manipulation and Comprehension](List_Manipulation_and_Comprehension)

You are provided with a text file containing a list of names.

## Your task is to:

### 1. Read the File:

Read the contents of the text file and store each line (representing a name) in a 2D list.

### 2. Perform Column-Major Transformation:

Transform the 2D list of names into column-major order, where characters are read vertically, column by column.

### 3. Count the Characters:

Calculate the total number of characters after the transformation, excluding any padding spaces added during the process.

### 4. Store the Result:

Write the transformed names into a new text file in a single continuous line, with no line breaks.

# [Calories](calories)

You are required to implement a function that performs calorie analysis based on a date range. The function will take two inputs: **'from date'** and **'to date'**, and perform the following tasks:

### 1. Average Calorie Calculation:

Calculate the average calorie intake per day within the given date range.

### 2. Standard Deviation:

Compute the standard deviation of the calorie intake within the date range to measure the variation.

### 3. Highest Calorie Day:

Identify the day with the highest calorie intake within the specified date range.

### 4. Highest Calorie per Meal:

Determine the meal with the highest calorie intake within the date range.

## Constraints

You are not allowed to use the `datetime` library.

# [MySql MongoDB](mysql_mongodb)

You are required to develop a Python script that transfers data from an SQL database to a MongoDB database. The script should accomplish the following tasks:

### 1. Fetch Data:

Retrieve data from the specified tables in the SQL database. You may choose to fetch data from one or multiple tables as needed.

### 2. Transform Data:

If necessary, transform the data into a format suitable for storage in MongoDB. This may include converting data types or reshaping data structures.

### 3. Insert Data into MongoDB:

Insert the retrieved data into the corresponding MongoDB collections. Ensure that the data is stored efficiently and maintains the relationships as needed.

# [Longest String of 1s](longest_string_1s)
You are tasked with finding the longest contiguous sequence of 1s in a 3D matrix. 
The function should identify and return the longest sequence of 1s that appears in any horizontal or vertical slice of the matrix. Additionally, the function should return the positions of the elements in this sequence.

# [Flight Ticket](flight_ticket)
You are tasked with developing a pricing mechanism for a Passenger Management System. 
## The system will perform the following tasks:

### 1. Fetch Ticket Information: 
Retrieve ticket information from a MongoDB database that contains details about the customer's visited destinations.

### 2. Determine Last Visited Destination: 
Identify the last destination the customer visited from the retrieved ticket information.

### 3. Calculate Visa Price: 
Based on the last visited destination, find the visa price using a provided JSON file provided

# [Review - Sentiment Analysis](review_sentiment_analysis)
You are tasked with classifying and summarizing product reviews. The system should perform the following tasks:

### 1. Classify Reviews:
Analyze and classify the reviews into one of three categories: positive, negative, or neutral.

### 2. Store Reviews by Class:
Store each class of reviews (positive, negative, and neutral) in separate text files.

### 3. Plot Review Distribution:
Plot a graph showing the count of reviews in each class (positive, negative, neutral).

### 4. Summarize Reviews:
Using only the NLTK library, generate a summary for each class of reviews (positive, negative, neutral).
