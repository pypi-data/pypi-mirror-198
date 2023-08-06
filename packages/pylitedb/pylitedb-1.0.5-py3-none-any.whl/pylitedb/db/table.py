from typing import Dict, List, Tuple
from datetime import datetime


from pylitedb.db.database import DB
from pylitedb.common.types import Records



class Table:
    insert_datetime_colname = 'insert_datetime'
    
    def __init__(self, 
                 db: DB, 
                 name: str,
                 schema: Dict[str, type],
                 primary_keys: List[str] = None) -> None:
        # Tables include the insertion datetime by default
        schema[self.insert_datetime_colname] = datetime
        
        self.db = db
        self.name = name
        self.schema = schema
        self.primary_keys = primary_keys
        
        # Create table only if it doesn't exist
        if self.name not in self.db.table_names():
            self.create()

    def create(self) -> None:
        """
        Creates the table in database
        """
        
        self.table.create(self.schema, pk=self.primary_keys)
    
    @property
    def table(self):
        return self.db[self.name]
    
    def insert(self, records: Records) -> None:
        time = datetime.now()
        [record.update({self.insert_datetime_colname: time}) for record in records]
        
        self.table.insert_all(records=records)
        
    def upsert(self, records: Records) -> None:
        time = datetime.now()
        [record.update({self.insert_datetime_colname: time}) for record in records]
        
        self.table.upsert_all(records=records, pk=self.primary_keys)
    
    def delete(self, conditions: List[Tuple[str, list]] = None) -> None:
        """
        Deletes rows from table. If conditions is None, all rows are deleted
        
        example of conditions => [("Where value > ?", [2])]
        conditions can be put in sequence

        Args:
            conditions (List[Tuple[str, list]], optional): conditions on which to delete rows. Defaults to None.
        """
        if conditions is None:
            self.table.delete_where()
            return
        
        for expr, args in conditions:
            self.table.delete_where(expr, args)
    
    def query(self, args: str = "", params: dict = None) -> Records:
        q = f"SELECT * FROM {self.name} {args}"
        data = self.db.query(q, params)
        records = [d for d in data]
        return records
    