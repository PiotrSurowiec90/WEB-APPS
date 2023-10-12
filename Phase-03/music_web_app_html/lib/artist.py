class Artist:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, genre, albums = []):
        self.id = id
        self.name = name
        self.genre = genre
        self.albums = albums

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"

    def is_valid(self):
        return self.name and self.genre
    
    def generate_errors(self):
        errors = []
        if not self.name:
            errors.append("Name can't be empty!")
        if not self.genre:
            errors.append("Genre can't be epmty!")

        return errors if len(errors) > 0 else None