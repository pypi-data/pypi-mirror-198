from context import chain, Trigger
from typing import Any
    
            

def test_simple():
    runner = Trigger()
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
    runner = Trigger()
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
    runner = Trigger()
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
    runner = Trigger()
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
    
    
def test_quickstart():
    trigger = Trigger()
    def function_one():
        return "hello"
    def function_two(message):
        return message + " world"
    def function_three(full_message):
        print(full_message)
    chain(trigger, function_one, function_two, function_three)
    trigger.run()