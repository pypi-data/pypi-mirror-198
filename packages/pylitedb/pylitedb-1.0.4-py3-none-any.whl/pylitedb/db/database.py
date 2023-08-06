import sqlite3
from typing import Optional
import sqlite_utils


class DB(sqlite_utils.Database):
    """
    Wrapper around sqlite_utils Database class
    """
    def __init__(self, name: str, path: Optional[str] = None, **kwargs) -> sqlite3.Connection:
        self.path = path or "."
        
        conn = sqlite3.connect(f"{self.path}/{name}.db")
        super().__init__(conn, **kwargs)
    