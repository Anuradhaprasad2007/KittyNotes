"""
kittyNotes - Custom Exceptions
Application-specific exceptions
"""


class kittyNotesError(Exception):
    """Base exception for kittyNotes"""
    pass


class ValidationError(kittyNotesError):
    """Raised when validation fails"""
    pass


class NoteNotFoundError(kittyNotesError):
    """Raised when a note is not found"""
    pass


class DatabaseError(kittyNotesError):
    """Raised when a database operation fails"""
    pass

