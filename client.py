import os
import six
from InquirerPy import prompt
from prompt_toolkit import document as doc
from prompt_toolkit.validation import ValidationError, Validator
from logs import editFileLog, createFileLog  

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

def createdLogs(status):
    if status:
        createFileLog()
        boolLogs.valLogs = status

def log(str, color="white"):
    if boolLogs.valTextConsole < 60: 
        boolLogs.valTextConsole += 1
    elif 60 <= boolLogs.valTextConsole: 
        boolLogs.valTextConsole = 0
        os.system('cls')
    if boolLogs.valLogs: 
        editFileLog(str.replace('\n', ' '))
    print(str)

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
import os
import six
from InquirerPy import prompt
from prompt_toolkit import document as doc
from prompt_toolkit.validation import ValidationError, Validator
from logs import editFileLog, createFileLog  

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

def createdLogs(status):
        if status:
                    createFileLog()
                    boolLogs.valLogs = status

    def log(str, color="white"):
            if boolLogs.valTextConsole < 60: 
                boolLogs.valTextConsole += 1
            elif 60 <= boolLogs.valTextConsole: 
                boolLogs.valTextConsole = 0
                        os.system('cls')
                    if boolLogs.valLogs: 
                        editFileLog(str.replace('\n', ' '))
                            print(str)

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
