import os
from prompt_toolkit.validation import ValidationError, Validator
from prompt_toolkit import document as doc

array_logo = [
    "    ______                   ______ _____    ___                      ",
    "   / __/ /____ ___ ___ _    / ___(_) _/ /_  / _ \___ ________ ___ ____",
    "  _\ \/ __/ -_) _ `/  ' \  / (_ / / _/ __/ / ___/ _ `/ __(_-</ -_) __/",
    " /___/\__/\__/\_,_/_/_/_/  \___/_/_/ \__/ /_/   \_,_/_/ /___/\__/_/   " 
]

# Удалили код с вопросами и логированием, теперь всё идёт через переменные окружения.

class statusLogs:
    def __init__(self):
        self._valLogs = False
        self._valTextConsole = 0

    @property 
    def valTextConsole(self): 
        return self._valTextConsole

    @property
    def valLogs(self):
        return self._valLogs

    @valTextConsole.setter
    def valTextConsole(self, value):
        self._valTextConsole = value

    @valLogs.setter
    def valLogs(self, value):
        self._valLogs = value

boolLogs = statusLogs()

class PointValidator(Validator):
    def validate(self, document: doc.Document):
        value = document.text
        try:
            value = int(value)
        except Exception:
            raise Exception('Value should be greater than 0')

        if value <= 0:
            raise Exception('Value should be greater than 0')
        return True
