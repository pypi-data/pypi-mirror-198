# Declback
## A declarative python backend framework

## Quickstart with pure Declback
1. Install the library via pip
```bash
pip install declback
```
2. Import it
```python
from declback import Trigger, chain
```
3. Create a functions to run inside chain
```python
def function_one():
    return "hello"
def function_two(message):
    return message + " world"
def function_three(full_message):
    print(full_message)
```
4. Create a Trigger instance
```python
trigger = Trigger()
```
5. Build a chain from your functions
```python
chain(trigger, function_one, function_two, function_three)
```
5. Run your trigger
```python
# run your trigger when you want to run your chain
trigger.run()
```