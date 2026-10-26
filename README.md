# 🐍 LeetCode Python Practice Projects (131–135)

## 📌 About This Repository

Welcome to my **LeetCode Python Practice Projects** repository! This repository contains five beginner-friendly Python programs designed to improve my programming skills, logical thinking, and problem-solving abilities.

Each program focuses on a different Python concept, including string manipulation, lists, built-in functions, and conditional statements.

## 🎯 Objectives

* Improve Python programming skills.
* Practice basic data structures and algorithms.
* Develop logical thinking and problem-solving abilities.
* Understand Python built-in functions and methods.
* Learn input validation and exception handling.
* Build a consistent coding practice portfolio on GitHub.

## 📂 Projects Included

| No. | Project Name                                | Description                                              | Main Concept        |
| --- | ------------------------------------------- | -------------------------------------------------------- | ------------------- |
| 131 | Largest Digit in a Number                   | Finds the largest digit in a positive integer.           | `max()`, strings    |
| 132 | Sum of Numbers in a List                    | Calculates the sum of numbers entered by the user.       | Lists, `sum()`      |
| 133 | Check Whether a String Contains Only Digits | Checks whether a string contains only numeric digits.    | `isdigit()`         |
| 134 | Find Frequency of a Number in a List        | Counts how many times a target number appears in a list. | `count()`           |
| 135 | Find Second Largest Distinct Number         | Finds the second-largest distinct number in a list.      | `set()`, `sorted()` |

---

## 🔢 Project 131: Largest Digit in a Number

### Description

This program finds the largest digit in a positive integer entered by the user.

### Python Code

```python
number = input("Enter a positive integer: ")

if not number.isdigit():
    print("Please enter a positive integer.")
else:
    largest = max(number)
    print("Largest digit:", largest)
```

### Example Output

```text
Enter a positive integer: 58321
Largest digit: 8
```

### Concepts Learned

* User input
* String validation
* The `max()` function
* Conditional statements

---

## ➕ Project 132: Sum of Numbers in a List

### Description

This program calculates the sum of multiple integers entered by the user.

### Python Code

```python
try:
    numbers = list(map(
        int,
        input("Enter numbers separated by spaces: ").split()
    ))

    total = sum(numbers)
    print("Sum of numbers:", total)

except ValueError:
    print("Invalid input! Please enter integers only.")
```

### Example Output

```text
Enter numbers separated by spaces: 10 20 30 40
Sum of numbers: 100
```

### Concepts Learned

* Python lists
* `split()` and `map()`
* Integer conversion
* The `sum()` function
* Exception handling

---

## 🔍 Project 133: Check Whether a String Contains Only Digits

### Description

This program checks whether a string contains only digits.

### Python Code

```python
text = input("Enter a string: ")

if text and text.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
```

### Example Output

```text
Enter a string: 12345
The string contains only digits.
```

### Concepts Learned

* String manipulation
* The `isdigit()` method
* Boolean conditions
* `if` and `else` statements

---

## 🔢 Project 134: Find Frequency of a Number in a List

### Description

This program counts how many times a specific number appears in a list.

### Python Code

```python
try:
    numbers = list(map(
        int,
        input("Enter numbers separated by spaces: ").split()
    ))

    target = int(input("Enter the number to count: "))
    frequency = numbers.count(target)

    print("Frequency of", target, ":", frequency)

except ValueError:
    print("Invalid input! Please enter integers only.")
```

### Example Output

```text
Enter numbers separated by spaces: 1 2 3 2 2 4
Enter the number to count: 2
Frequency of 2 : 3
```

### Concepts Learned

* Lists
* The `count()` method
* User input
* Integer conversion
* Exception handling

---

## 🥈 Project 135: Find Second Largest Distinct Number

### Description

This program finds the second-largest distinct number in a list of integers.

### Python Code

```python
try:
    numbers = list(map(
        int,
        input("Enter numbers separated by spaces: ").split()
    ))

    unique_numbers = sorted(set(numbers))

    if len(unique_numbers) >= 2:
        print("Second largest number:", unique_numbers[-2])
    else:
        print("There is no second largest distinct number.")

except ValueError:
    print("Invalid input! Please enter integers only.")
```

### Example Output

```text
Enter numbers separated by spaces: 10 20 40 30 40
Second largest number: 30
```

### Concepts Learned

* Python lists
* The `set()` function
* Removing duplicate values
* The `sorted()` function
* List indexing
* Conditional statements

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Code Editor:** Visual Studio Code
* **Version Control:** Git
* **Repository Hosting:** GitHub

## 💻 Installation and Setup

### Step 1: Install Python

Download Python from the official website:

https://www.python.org/downloads/

### Step 2: Install Visual Studio Code

Download Visual Studio Code:

https://code.visualstudio.com/

### Step 3: Clone the Repositories

Clone each project repository separately using its GitHub URL.

For example:

```bash
git clone https://github.com/aishuaishu45793-gif/leetcode-python-131.py.git
```

Change into the downloaded folder:

```bash
cd leetcode-python-131.py
```

Repeat for the other repositories by replacing `131` with `132`, `133`, `134`, or `135`.

### Step 4: Run a Python Program

Run the corresponding Python file from the VS Code terminal.

For example:

```bash
python 131.py
```

Use the correct filename if your Python file has a different name or is inside a subfolder.

## 📚 Overall Skills Practiced

Through these five projects, I practiced:

* Python syntax and variables
* User input and output
* String manipulation
* Lists and collections
* Built-in functions such as `max()`, `sum()`, and `sorted()`
* List methods such as `count()`
* Sets and duplicate removal
* Conditional statements
* Input validation
* Exception handling
* Basic problem-solving techniques

## 🌱 Learning Outcomes

These projects helped me understand how to solve simple programming problems using Python. They also strengthened my understanding of strings, lists, built-in functions, and conditional logic.

## 👩‍💻 Author

**Aishwarya**

GitHub: https://github.com/aishuaishu45793-gif

## ⭐ Conclusion

This collection represents my continued journey in learning Python and practicing coding problems inspired by LeetCode.

I will continue adding more projects as I improve my programming, algorithmic thinking, and problem-solving skills.

**Happy Coding! 🐍💻**
