# Practical Design Patterns in Python
This project demonstrates the implementation of various design patterns in Python.
Each design pattern is implemented conceptually in a file named `concept.py` and practical examples are provided in files prefixed with `ex_`.
This way you can see how to apply the design pattern in real-world scenarios.

I attempted to use modern Python features and best practices in the examples, such as:
- Type hints
- Dataclasses
- Protocols
- Alternative approaches to design patterns such as function decorators

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

## Structure
Each design pattern has at least two scripts:
  - `concept.py` - conceptual implementation
  - `ex_{script}.py` - example real-world scenario

### Creational Patterns
- **Abstract Factory**
  - `concept.py`
  - `ex_gui.py`
- **Builder**
  - `concept.py`
  - `ex_computer.py`
  - `ex_computer_fluent.py`
- **Factory Method**
  - `concept.py`
  - `ex_notifications.py`
- **Prototype**
  - `concept.py`
  - `ex_documents.py`
- **Singleton**
  - `concept.py`
  - `concept_threadsafe.py`
  - `ex_configuration.py`

### Structural Patterns
- **Adapter**
  - `concept_class_adapter.py`
  - `concept_object_adapter.py`
  - `ex_xml_to_json_adapter.py`
- **Bridge**
  - `concept.py`
  - `ex_databases.py`
  - `ex_gui.py`
- **Composite**
  - `concept.py`
  - `ex_file_system.py`
- **Decorator**
  - **Class Decorators**
    - `concept.py`
    - `ex_data_access.py`
  - **Classic Decorators**
    - `concept.py`
    - `ex_data_access.py`
    - `ex_data_handler.py`
    - `ex_document_processor.py`
  - **Function Decorators**
    - `concept.py`
    - `ex_access_control.py`
    - `ex_caching.py`
    - `ex_logging.py`
- **Facade**
  - `concept.py`
  - `ex_third_party_lib.py`
- **Flyweight**
  - `concept.py`
  - `ex_chess.py`
- **Proxy**
  - `concept.py`
  - `ex_caching_proxy.py`
  - `ex_logging_proxy.py`
  - `ex_protection_proxy.py`
  - `ex_protection_proxy_decorator.py`
  - `ex_smart_reference_proxy.py`
  - `ex_virtual_proxy.py`

### Behavioral Patterns
- **Chain of Responsibility**
  - `concept.py`
  - `ex_gui.py`
- **Command**
  - `concept.py`
  - `ex_editor.py`
- **Iterator**
  - `concept.py`
  - `ex_graph.py`
  - `ex_inventory.py`
  - `ex_tree.py`
- **Mediator**
  - `concept.py`
  - `ex_chatroom.py`
  - `ex_stock_market.py`
  - `ex_ui_components.py`
- **Memento**
  - `concept.py`
  - `ex_game_state.py`
  - `ex_transactional_db.py`
- **Observer**
  - `concept.py`
  - `concept_distributed.py`
  - `ex_smart_home.py`
  - `ex_stock_market.py`
- **State**
  - `concept.py`
  - `ex_traffic_lights_enum.py`
  - `ex_traffic_lights_sm_library.py`
  - `ex_traffic_lights_state.py`
- **Strategy**
  - `concept.py`
  - `ex_payment_processor.py`
  - `ex_text_formatter.py`
- **Template Method**
  - `concept.py`
  - `ex_data_pipeline.py`
- **Visitor**
  - `concept.py`
  - `ex_file_visitor.py`

### Additional Patterns
- **Specification**
  - `concept.py`
  - `ex_ecommerce.py`

Each directory contains a `concept.py` file illustrating the basic concept of the pattern and example files (`ex_*.py`) showing practical implementations. This repository serves as a comprehensive reference for understanding and implementing design patterns in Python.

## Remarks
- Most of the examples don't do the real job, they just show how you'd leverage the design pattern in certain use case.<br/>
But there are some examples in which I've attempted to do the real job as in [bridge pattern database example](https://github.com/saikotek/python-design-patterns/blob/main/src/bridge/ex_databases.py) that uses Testcontainers to boot the real database.
- Whenever possible I've used Protocols as a static way of duck typing (more on that here: [Protocols](https://mypy.readthedocs.io/en/stable/protocols.html))

## References
I recommend these great resources about design patterns 
- Design Patterns: Elements of Reusable Object-Oriented Software
- https://refactoring.guru/
- [Christopher Okhravi's YT Channel](https://www.youtube.com/playlist?list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc)
