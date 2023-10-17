"""An example of _not_ using Inversion of Control.

See https://martinfowler.com/bliki/InversionOfControl.html
"""

def process_name(name):
    """Handle the name processing logic"""
    # ...

def process_quest(quest):
    """Handle the quest processing logic"""
    # ...

name = input('What is your name?\n')
process_name(name)

quest = input('What is your quest?\n')
process_quest(quest)
