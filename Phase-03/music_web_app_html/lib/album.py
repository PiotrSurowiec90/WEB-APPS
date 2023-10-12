from dataclasses import dataclass

@dataclass
class Album:
    id: int
    title: str
    release_year: int
    artist_id: int

    def __repr__(self) -> str:
        return f"{self.title}, {self.release_year}"
    
    def is_valid(self):
        return self.title and self.release_year and self.artist_id
    
    def generate_errors(self):
        errors = []
        if not self.title:
            errors.append("Title can't be empty!")
        if not self.release_year:
            errors.append("Release year can't be empty!")
        if not self.artist_id:
            errors.append("Artist id can't be empty!")
        
        return ', '.join(errors) if len(errors) > 0 else None