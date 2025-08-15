# abstract
# Key Points:

# human → Abstract class (can’t be instantiated).

# @abstractmethod → Forces child classes to implement gender() method.

# men and women → Concrete subclasses that implement gender().

# You cannot do human() directly — it will give an error.

# Useful for defining a common structure for all child classes.
from abc import ABC, abstractmethod
class human(ABC):
    @abstractmethod
    def gender(self):
        pass
class men(human):
    def gender(self):
        return "male"
class women(human):
    def gender(self):
        return "women"
men=men()
print(men.gender())
women=women()
print(women.gender())