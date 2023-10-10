from dataclasses import dataclass

@dataclass
class Artist:
    id: int
    name: str
    genre: str

    def __repr__(self) -> str:
        return f"{self.name}"