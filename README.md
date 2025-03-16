# Practical Design Patterns in Python
This project demonstrates the implementation of various design patterns in Python.
Each design pattern is implemented conceptually in a file named `concept.py` and practical examples are provided in files prefixed with `ex_`.
This way you can see how to apply the design pattern in real-world scenarios.

I attempted to use modern Python features and best practices in the examples, such as:
- Type hints
- Dataclasses
- Protocols
- Alternative approaches to design patterns such as function decorators

This repository serves as a comprehensive reference for understanding and implementing design patterns in Python.
## What are Design Patterns?
Design patterns are proven solutions to common software design problems. They provide a template for writing code that is maintainable, reusable, and scalable. 
This project covers a wide range of design patterns, traditionally divided into three categories: creational, structural, and behavioral.

Most of them are from the book "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides.

## Installing
Required Python >= 3.8<br/>
Create virtual environment and install dependencies:
```
py -m venv venv
pip install -r requirements.txt
```

## List of Design Patterns
Each design pattern has at least two scripts:
  - `concept.py` - conceptual implementation
  - `ex_{script}.py` - example real-world scenario

We'll start with classic design patterns and then move on to additional patterns.
Classic design patterns are divided into three categories: creational, structural, and behavioral.
### Creational Patterns
- **Abstract Factory**
  - `concept.py` - Intent: Lets you create families of related objects without specifying their concrete implementations.
  - `ex_gui.py` - Example: Demonstrates creating families of related UI elements for Windows and Mac OS.

- **Builder**
  - `concept.py` - Intent: Separate the construction of a complex object from its representation so that the same construction process can create different representations.
  - `ex_computer.py` - Example: Computer Builder with concrete builder classes for gaming and office computers.
  - `ex_computer_fluent.py` - Example: Fluent Builder for building computers with different specifications.

- **Factory Method**
  - `concept.py` - Intent: Lets you create objects without specifying the exact class to create, using factory methods instead of constructors.
  - `ex_notifications.py` - Example: Notifications system that creates different types of notifications.

- **Prototype**
  - `concept.py` - Intent: Allows cloning objects without coupling to their specific classes using shallow and deep copying.
  - `ex_documents.py` - Example: Document cloning system.

- **Singleton**
  - `concept.py` - Intent: Ensures that a class has only one instance while providing a global access point to this instance.
  - `concept_threadsafe.py` - Intent: Thread-safe implementation of the Singleton pattern.
  - `ex_configuration.py` - Example: Configuration class that stores application settings as a singleton.

### Structural Patterns
- **Adapter**
  - `concept_class_adapter.py` - Intent: Converts the interface of a class into another interface clients expect using multiple inheritance.
  - `concept_object_adapter.py` - Intent: Converts the interface of a class into another interface clients expect using composition.
  - `ex_xml_to_json_adapter.py` - Example: Adapts XML data processor to work with a JSON analytics system.

- **Bridge**
  - `concept.py` - Intent: Decouples an abstraction from its implementation so that the two can vary independently.
  - `ex_databases.py` - Example: Refined abstractions of Database for different (SQLite, Postgres) implementations.
  - `ex_gui.py` - Example: Tkinter GUI application with theme implementations (Light and Dark) bridged with applications.

- **Composite**
  - `concept.py` - Intent: Composes objects into tree structures to represent part-whole hierarchies, allowing clients to treat individual objects and compositions uniformly.
  - `ex_file_system.py` - Example: Working with files and directories through a composite structure.

- **Decorator**
  - **Class Decorators**
    - `concept.py` - Intent: Python class-based decorators that modify the behavior of functions or methods.
    - `ex_data_access.py` - Example: Data access control with class decorators for role checking and caching.
  - **Classic Decorators**
    - `concept.py` - Intent: Adds behavior to objects dynamically without affecting other instances of the same class.
    - `ex_data_access.py` - Example: Data access service with access control and caching decorators.
    - `ex_data_handler.py` - Example: Data handler with encryption and compression decorators.
    - `ex_document_processor.py` - Example: Document processor with spell check and grammar check decorators.
  - **Function Decorators**
    - `concept.py` - Intent: Python function decorators that modify the behavior of functions or methods.
    - `ex_access_control.py` - Example: Access control decorator for functions.
    - `ex_caching.py` - Example: Caching decorator for functions.
    - `ex_logging.py` - Example: Logging decorator for functions.

- **Facade**
  - `concept.py` - Intent: Provides a simplified interface to a complex subsystem of classes.
  - `ex_third_party_lib.py` - Example: Facade for a third-party email library.

- **Flyweight**
  - `concept.py` - Intent: Minimizes memory usage by sharing common state between multiple objects.
  - `ex_chess.py` - Example: Chess pieces factory reusing shared pieces.

- **Proxy**
  - `concept.py` - Intent: Provides a surrogate or placeholder for another object to control access to it.
  - `ex_caching_proxy.py` - Example: Caching proxy for expensive operations.
  - `ex_logging_proxy.py` - Example: Logging proxy that logs each request to the original object.
  - `ex_protection_proxy.py` - Example: Protection proxy controlling access based on user roles.
  - `ex_protection_proxy_decorator.py` - Example: Protection proxy using decorators.
  - `ex_smart_reference_proxy.py` - Example: Smart reference proxy.
  - `ex_virtual_proxy.py` - Example: Virtual proxy for lazy initialization of expensive objects.

### Behavioral Patterns
- **Chain of Responsibility**
  - `concept.py` - Intent: Passes a request along a chain of handlers, with each handler deciding to process or pass it along.
  - `ex_gui.py` - Example: GUI components with contextual help system.

- **Command**
  - `concept.py` - Intent: Turns requests into stand-alone objects for parameterization, queuing, and supporting undoable operations.
  - `ex_editor.py` - Example: Text editor with undo functionality.

- **Iterator**
  - `concept.py` - Intent: Provides a way to traverse elements of a collection without exposing its underlying representation.
  - `ex_graph.py` - Example: Graph traversal using breadth-first and depth-first search.
  - `ex_inventory.py` - Example: Inventory traversal system.
  - `ex_tree.py` - Example: Tree traversal implementation.

- **Mediator**
  - `concept.py` - Intent: Reduces dependencies between objects by forcing them to communicate via a mediator object.
  - `ex_chatroom.py` - Example: Chat room using mediator to notify users of messages.
  - `ex_stock_market.py` - Example: Stock market communication system.
  - `ex_ui_components.py` - Example: UI components coordinated by a mediator.

- **Memento**
  - `concept.py` - Intent: Captures an object's internal state to restore it later without exposing its structure.
  - `ex_game_state.py` - Example: Saving and restoring game states.
  - `ex_transactional_db.py` - Example: Transactional database with save and restore capabilities.

- **Observer**
  - `concept.py` - Intent: Defines a one-to-many relationship so when one object changes state, all dependents are notified.
  - `concept_distributed.py` - Intent: Distributed observer pattern allowing components to act as both publishers and subscribers.
  - `ex_smart_home.py` - Example: Home automation system with devices publishing and subscribing to events.
  - `ex_stock_market.py` - Example: Stock market monitoring where clients subscribe to price updates.

- **State**
  - `concept.py` - Intent: Allows an object to alter its behavior when its internal state changes.
  - `ex_traffic_lights_enum.py` - Example: Traffic lights using simple enum-based state machine.
  - `ex_traffic_lights_sm_library.py` - Example: Traffic lights using a third-party state machine library.
  - `ex_traffic_lights_state.py` - Example: Traffic lights using class-based state pattern implementation.

- **Strategy**
  - `concept.py` - Intent: Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
  - `ex_payment_processor.py` - Example: Payment strategies for an online store.
  - `ex_text_formatter.py` - Example: Text formatting strategies for a document editor.

- **Template Method**
  - `concept.py` - Intent: Defines the skeleton of an algorithm allowing subclasses to override specific steps without changing structure.
  - `ex_data_pipeline.py` - Example: Data processing pipeline implementation.

- **Visitor**
  - `concept.py` - Intent: Separates algorithms from the objects they operate on using double dispatch.
  - `ex_file_visitor.py` - Example: File system visitor performing operations on different file types.

### Additional Patterns
- **Repository**
  - `concept.py` - Intent: Mediates between the domain and data mapping layers using a collection-like interface for accessing data.
  - `ex_sqlite_repository.py` - Example: SQLite repository for storing and retrieving data.

- **Specification**
  - `concept.py` - Intent: Creates complex filtering logic by combining simple rules.
  - `ex_ecommerce.py` - Example: E-commerce product filtering using combined specifications.

- **Context Manager**
  - `concept.py` - Intent: Simplifies resource management by providing setup and teardown actions.
  - `ex_timing.py` - Example: Timing context manager for measuring execution time of inner block.
  - `ex_database_connection.py` - Example: Database connection context manager to properly save changes and close connections.

## Remarks
- Most of the examples don't do the real job, they just show how you'd leverage the design pattern in certain use case.<br/>
But there are some examples in which I've attempted to do the real job as in [bridge pattern database example](https://github.com/saikotek/python-design-patterns/blob/main/src/bridge/ex_databases.py) that uses Testcontainers to boot the real database.
- Whenever possible I've used Protocols as a static way of duck typing (more on that here: [Protocols](https://mypy.readthedocs.io/en/stable/protocols.html))

## References
I recommend these great resources about design patterns 
- Design Patterns: Elements of Reusable Object-Oriented Software
- https://refactoring.guru/
- [Christopher Okhravi's YT Channel](https://www.youtube.com/playlist?list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc)
