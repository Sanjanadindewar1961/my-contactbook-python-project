## 📖 Project Overview

The **Contact Book** is a simple Python-based console application that allows users to manage a list of personal or professional contacts. It demonstrates the use of **Object-Oriented Programming (OOP)** concepts such as classes, objects, encapsulation, and modular design.

This program provides a user-friendly **menu-driven interface** where users can perform operations like adding new contacts, viewing all saved contacts, searching for a specific contact by name, updating contact details, and deleting contacts from the list.

---

## 🧩 Core Concepts

The project is built using the following theoretical principles:

### 1. **Modularity**

The code is organized into multiple files:

* `contact.py`: Defines the `Contact` class responsible for storing individual contact details.
* `contact_book.py`: Contains the `ContactBook` class, which manages a collection of contacts and provides methods to add, search, update, and delete them.
* `main.py`: Acts as the user interface, presenting a menu and capturing user input to interact with the `ContactBook`.

### 2. **Object-Oriented Programming (OOP)**

The project uses classes to model real-world entities:

* A **Contact** object encapsulates details like name, phone number, and email.
* A **ContactBook** object manages a list (or dictionary) of contacts and provides methods to manipulate them.

### 3. **Encapsulation**

Data and behavior related to contacts are bundled within classes. Users interact with objects using public methods, without needing to know the internal implementation.

### 4. **User Interaction**

The application uses a **text-based interface** that runs in a loop, allowing continuous user interaction until the user chooses to exit. Input validation and prompt messages guide the user through each operation.

---

## 🔍 Functionalities

* **Add Contact**: Collects user input to create and store a new contact.
* **Display Contacts**: Lists all stored contacts with their details.
* **Search Contact**: Allows the user to search for a contact by name.
* **Update Contact**: Enables the user to modify existing contact information.
* **Delete Contact**: Removes a contact from the list by name.
* **Exit**: Gracefully terminates the application.

---

## 📚 Educational Value

This project is ideal for beginners learning Python and OOP. It offers hands-on experience with:

* Class creation and usage
* Method definitions and parameter passing
* Loops and conditionals
* Input/output handling
* Basic software design patterns

---

