from enum import Enum


class EventPriority(Enum):
    FIRST = 1
    ANY = 2
    LAST = 3

    def __lt__(self, other_priority: 'EventPriority') -> bool:
        return int(self.value) < int(other_priority.value)