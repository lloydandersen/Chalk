class HeaderError(Exception):
    """Exception for header errors."""
    def __init__(self, message: str, details=None):
        super().__init__(message)
        self.details = details


class GlobalError(Exception):
    """Exception for Global header errors."""
    def __init__(self, message: str, details=None):
        super().__init__(message)
        self.details = details


class SourceError(Exception):
    """Exception for source header errors."""
    def __init__(self, message: str, details=None):
        super().__init__(message)
        self.details = details


class ImportsError(Exception):
    """Exception for Import header errors."""
    def __init__(self, message: str, details=None):
        super().__init__(message)
        self.details = details


class ProblemError(Exception):
    """Exception for Problem errors."""
    def __init__(self, message: str, details=None):
        super().__init__(message)
        self.details = details