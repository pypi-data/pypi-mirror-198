from typing import Dict, List, Tuple
from datetime import datetime

from pylitedb.db.database import DB
from pylitedb.common.types import Records


class Table:
    insert_date_colname = 'insert_date'
    
    def __init__(self, 
                 db: DB, 
                 name: str,
                 columns: Dict[str, type],
                 primary_keys: List[str] = None) -> None:
        columns[self.insert_date_colname] = datetime
        
        self.db = db
        self.name = name
        self.columns = columns
        self.primary_keys = primary_keys if primary_keys else None
        
        # Create table only if it doesn't exist
        if self.name not in self.db.table_names:
            self.create()

    def create(self) -> None:
        """
        Creates the table in database
        """
        
        self.db[self.name].create(self.columns, pk=self.primary_keys)
    
    def insert(self, records: Records) -> None:
        time = datetime.now().strftime("%Y-%m-%d")
        [record.update({self.insert_date_colname: time}) for record in records]
        
        self.db[self.name].insert_all(records=records)
        
    def upsert(self, records: Records) -> None:
        time = datetime.now()
        [record.update({self.insert_date_colname: time}) for record in records]
        
        self.db[self.name].upsert_all(records=records, pk=self.primary_keys)
    
    def delete(self, conditions: List[Tuple[str, list]] = None) -> None:
        if conditions is None:
            self.db[self.name].delete_where()
            return
        
        for expr, args in conditions:
            self.db[self.name].delete_where(expr, args)
        