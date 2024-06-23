# Practical Python Design Patterns
I've implemented all GoF design patterns in Python alongside with example use cases for them so you can see practical scenarios where you'd use them.

## Installing
Required Python >= 3.8<br/>
Create virtual environment and install dependencies:
```
py -m venv venv
pip install -r requirements.txt
```

## Structure
Each design pattern has at least two scripts:
  - concept.py - conceptual implementation of design pattern
  - ex_{script}.py - example use case in some real-world scenario

## Remarks
- Most of the examples don't do the real job, they just show how you'd leverage the design pattern in certain use case.<br/>
But there are some examples in which I've attempted to do the real job as in [bridge pattern database example](https://github.com/saikotek/python-design-patterns/blob/main/src/bridge/ex_databases.py) that uses Testcontainers to boot the real database.
- Whenever possible I've used Protocols as a static way of duck typing (more on that here: [Protocols](https://mypy.readthedocs.io/en/stable/protocols.html))

## References
I recommend these great resources about design patterns 
- Design Patterns: Elements of Reusable Object-Oriented Software
- https://refactoring.guru/
- [Christopher Okhravi's YT Channel](https://www.youtube.com/playlist?list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc)
