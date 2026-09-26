# Student Management System

A Python-based Student Management System project designed to demonstrate Object-Oriented Programming (OOP) concepts, including inheritance, polymorphism, encapsulation, and method overriding.

## 📌 Task Description

Create a Student Management System using Python OOP concepts.

The project consists of a base `Student` class and two derived classes: `UndergraduateStudent` and `GraduateStudent`.

## 📂 Required Classes

```text
Student
  |
  ├── UndergraduateStudent
  |
  └── GraduateStudent
```

### 1. Student Class

Create a `Student` class with the following attributes:

* `name`
* `student_id`
* `email`
* `age`
* `department`

**Required Methods:**

* `display_info()` – Displays student information.
* `calculate_result()` – Calculates the student's result.
* `get_student_type()` – Returns the type of student.

### 2. UndergraduateStudent Class

Inherit from the `Student` class.

**Additional Attribute:**

* `semester`

**Method Overriding:**

* Override at least one parent method, such as `get_student_type()`.

### 3. GraduateStudent Class

Inherit from the `Student` class.

**Additional Attribute:**

* `research_topic`

**Method Overriding:**

* Override at least one parent method, such as `get_student_type()`.

## 🎯 Required OOP Concepts

The project must demonstrate the following Object-Oriented Programming concepts:

| Concept            | Requirement                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| Class & Object     | Create objects from the classes.                                                                             |
| Attributes         | Use student-related attributes.                                                                              |
| Methods            | Implement methods for student operations.                                                                    |
| Inheritance        | `UndergraduateStudent` and `GraduateStudent` inherit from `Student`.                                         |
| Polymorphism       | Call the same method on different student objects and get different behavior.                                |
| Method Overriding  | Override a parent method in child classes.                                                                   |
| Method Overloading | Use default arguments, `*args`, or `**kwargs` to allow a method to work with different numbers of arguments. |
| Encapsulation      | Use a private attribute such as `__email` or `__marks`.                                                      |

## 🛠️ Technologies Used

* Python
* Object-Oriented Programming (OOP)

## 📚 Learning Objectives

* Understand and implement Python classes and objects.
* Practice inheritance and method overriding.
* Demonstrate polymorphism using different student types.
* Apply encapsulation to protect sensitive student data.
* Implement flexible methods using default arguments, `*args`, or `**kwargs`.

---

**Project:** Student Management System
**Language:** Python
**Purpose:** Practice and demonstrate Object-Oriented Programming concepts.
