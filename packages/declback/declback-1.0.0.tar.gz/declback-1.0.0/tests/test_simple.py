from context import chain, Trigger
from typing import Any
    
    
class SimpleRunner(Trigger):
    def run(self):
        for listener in self.listeners:
            listener(dict())
    
    
class ContextRunner(Trigger):
    def run(self, context: dict[str, Any]):
        for listener in self.listeners:
            listener(context)
            

def test_simple():
    runner = SimpleRunner()
    part1_executed = False
    part2_executed = False
    def part1():
        nonlocal part1_executed
        part1_executed = True
    def part2():
        nonlocal part2_executed
        part2_executed = True
    chain(runner, part1, part2)
    runner.run()
    assert part1_executed
    assert part2_executed
            

def test_argumented():
    runner = SimpleRunner()
    result = 0
    def part1():
        return 5
    def part2(arg: int):
        nonlocal result
        result = arg
    chain(runner, part1, part2)
    runner.run()
    assert result == 5
            

def test_first_returning_but_second_without_args():
    runner = SimpleRunner()
    result = 0
    def part1():
        return 5
    def part2():
        nonlocal result
        result = 3
    chain(runner, part1, part2)
    runner.run()
    assert result == 3
            

def test_with_context():
    runner = ContextRunner()
    result = 0
    def part1(**kwargs):
        print(kwargs)
        return kwargs["context"]["x"]
    def part2(arg: int):
        nonlocal result
        result = arg
    chain(runner, part1, part2)
    runner.run({"x": 1})
    assert result == 1