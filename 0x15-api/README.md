# 0x15. API

---

### What Bash Scripting Should Not Be Used For

Bash scripting is ideal for automating simple tasks on Unix-like systems but has its limitations. It should not be used for:

- **Complex Logic**: Extensive control flow or algorithms are better handled by languages like Python or Java.
- **Performance-Intensive Tasks**: Computationally heavy tasks are inefficient in Bash. Use C++ or Python for better performance.
- **Large-Scale Applications**: For applications with GUIs or heavy networking, use languages like Java or C#.
- **Cross-Platform Compatibility**: Bash scripts are tied to Unix-like systems. For cross-platform scripts, consider Python or Node.js.
- **Robust Error Handling**: Bash has basic error handling. Languages like Python offer more comprehensive exception handling.

### What is an API

An API (Application Programming Interface) is a set of rules that allows different software entities to communicate with each other. APIs enable integration and the use of functionalities provided by one application in another.

### What is a REST API

A REST API (Representational State Transfer API) is a web service that adheres to REST principles. It uses standard HTTP methods like GET, POST, PUT, DELETE, and operates on resources identified by URLs.

Key principles of REST:
- **Stateless**: Each request must contain all necessary information.
- **Client-Server**: Separation of concerns allows independent evolution.
- **Cacheable**: Responses can be marked as cacheable or not.
- **Uniform Interface**: Simplifies and decouples the architecture.

### What Are Microservices

Microservices are an architectural style where an application is composed of small, independent services, each fulfilling a specific business function. They communicate through well-defined APIs.

Advantages:
- **Scalability**: Services can be scaled independently.
- **Flexibility**: Different technologies can be used for different services.
- **Resilience**: Fault isolation ensures system robustness.

### What is the CSV Format

CSV (Comma-Separated Values) is a simple file format for storing tabular data. Each line in a CSV file corresponds to a row, and each value is separated by a comma.

Example of CSV content:
```
name,age,email
John Doe,30,john.doe@example.com
Jane Smith,25,jane.smith@example.com
```

### What is the JSON Format

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.

Example of JSON content:
```json
{
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}
```

## Pythonic Naming Styles

### Pythonic Package and Module Name Style

- **Packages**: Use lowercase words, separated by underscores if needed.
- **Modules**: Similar to packages, use lowercase with underscores if necessary.

Example:
```
my_package/
    __init__.py
    my_module.py
```

### Pythonic Class Name Style

Class names should use the CapWords (CamelCase) convention, where each word starts with a capital letter and no underscores are used.

Example:
```python
class MyClass:
    def __init__(self, value):
        self.value = value
```

### Pythonic Variable Name Style

Variable names should be in lowercase, with words separated by underscores.

Example:
```python
my_variable = 10
another_variable = 20
```

### Pythonic Function Name Style

Function names should be in lowercase, with words separated by underscores.

Example:
```python
def my_function():
    pass

def calculate_sum(a, b):
    return a + b
```

### Pythonic Constant Name Style

Constants should be in all uppercase letters, with words separated by underscores.

Example:
```python
MAX_CONNECTIONS = 100
PI = 3.14159
```

### Significance of CapWords or CamelCase in Python

CapWords (CamelCase) improves readability by clearly delineating the start of new words. It maintains a consistent naming convention, making code easier to understand and maintain. Following these conventions adheres to the Python Enhancement Proposal (PEP 8), the style guide for Python code.

Example:
```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```

---

