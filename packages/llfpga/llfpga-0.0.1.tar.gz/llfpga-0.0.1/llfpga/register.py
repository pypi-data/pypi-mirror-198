from dataclasses import dataclass

@dataclass
class Register:
    address: int
    size: int