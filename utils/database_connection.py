import sqlite3

class DatabaseConnection:
    def __enter__(self):
        # called when the flow goes into the context manager 
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # executed when the flow leaves the context manager
        pass