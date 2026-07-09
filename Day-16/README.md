# Day-16: Coffe Machine Project in OOP
## Project Objective
Build an Object-Oriented Programming (OOP) command-line Coffee Machine application in Python that simulates the functionality of a real coffee vending machine. The project applies OOP principles by organizing the program into classes and objects responsible for managing the menu, machine resources, payment processing, and coffee preparation. Users can select different coffee drinks, the system verifies ingredient availability, processes coin payments, calculates and returns change, updates the remaining resources after each successful order, and keeps track of the machine's total profit.
## What I Learnt
1. **Procedural Programming:** A programming approach where code is executed sequentially using functions, loops, and conditional statements. The focus is on the flow of the program, but as the application grows, managing all the code in a single file can become challenging.
2. **Object-Oriented Programming (OOP):** A programming approach that structures code into objects, with each object responsible for its own data and behavior. In this project, classes such as Menu, CoffeeMaker, and MoneyMachine each perform a specific role, making the program more organized, reusable, and easier to maintain instead of having one large program handle everything.
3. **Class:** A class is a blueprint for creating objects. It defines the attributes (data) and methods (behaviors) an object will have, but it only becomes usable when an object is created. Examples in this project include the Menu, CoffeeMaker, and MoneyMachine classes.
4. **Object:** An object is an instance of a class. It is created from a class and can access the class's attributes and methods. For example, menu = Menu() creates a Menu object.
5. **Attributes:** Attributes are variables that belong to a class or object and store its data or state. They hold the information an object needs to perform its tasks.
5. **Methods:** Methods are functions defined inside a class that describe the actions an object can perform. They are called through an object to carry out specific operations.
6. **PyPI (Python Package Index):** I learned how to use PyPI to find, install, and manage third-party Python packages using the pip package manager. Like PrettyTable.
## How It Works
1. **Choose a Drink** – The user selects either espresso, latte, or cappuccino.
2. **Check Resources** – The machine verifies that there is enough water, milk, and coffee to prepare the selected drink.
3. **Process Payment** – The user inserts coins, and the machine calculates the total amount entered.
4. **Complete the Transaction** – If the payment is sufficient, the machine returns any change, and deducts the required ingredients from its resources.
5. **Serve the Drink** – The selected coffee is prepared and served. Users can also enter report to view available resources and profit or off to shut down the machine.

   ## Output
 ![alt text](2026-07-07.png)