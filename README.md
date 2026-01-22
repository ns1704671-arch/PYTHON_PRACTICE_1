# 🐍 Python Data Structures & Algorithms Exercises

Welcome to the *Python Data Structures & Algorithms* repository!  
This repository contains exercises for practicing *lists, **basic operations, and **algorithmic thinking* in Python.

---

## 🗓️ Day 1: List Manipulation Exercises (Yesterday)

*Topics Covered:*
- append() – Add elements at the end of the list
- insert() – Insert element at a specific position
- remove() – Remove element by value

### 🔹 Examples

```python
# Creating a list
numbers = [5, 10, 15, 20]

# Append a number
numbers.append(25)
print(numbers)  # Output: [5, 10, 15, 20, 25]

# Insert a number at index 2
numbers.insert(2, 12)
print(numbers)  # Output: [5, 10, 12, 15, 20, 25]

# Remove a number by value
numbers.remove(15)
print(numbers)  # Output: [5, 10, 12, 20, 25]
