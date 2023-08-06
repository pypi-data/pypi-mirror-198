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
2. Create a Trigger class for your chains
```python
class SimpleRunner(Trigger):
    # you may put some logic here
    def just_run(self):
        for listener in self.listeners:
            listener(dict())
```
3. Create a functions to run inside chain
```python
def function_one():
    print('Hello')
    return 'world'
def function_two(message):
    print(message)
```
4. Create a Trigger instance and chain
```python
my_trigger = SimpleRunner()
my_chain = chain(my_trigger, function_one, function_two)
```
5. Run your trigger
```python
# run your trigger when you want to run your chain
# or put your logic into trigger and interact with it
my_trigger.just_run()
```