import sqlite3
import pathlib
from typing import Optional
import sqlite_utils

class DB:
    """
    Wrapper around sql utils Database
    """
    def __init__(self, name: str, path: Optional[str] = None) -> sqlite3.Connection:
        self.path = path or pathlib.Path(__file__).parent / "dbfiles"
        
        conn = sqlite3.connect(f"{self.path}/{name}.db")
        self.db = sqlite_utils.Database(conn)

    def __getitem__(self, value: str) -> sqlite_utils.Database:
        return self.db[value]
    
    @property
    def table_names(self):
        return self.db.table_names()
    