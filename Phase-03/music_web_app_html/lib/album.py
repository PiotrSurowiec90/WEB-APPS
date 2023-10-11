from dataclasses import dataclass

@dataclass
class Album:
    id: int
    title: str
    release_year: int
    artist_id: int

    def __repr__(self) -> str:
        return f"{self.title}, {self.release_year}"