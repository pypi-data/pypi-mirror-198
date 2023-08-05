# dblib

Simple library to help manage a database

## Example
```python
from datetime import datetime

from pylitedb.db.database import DB
from pylitedb.db.table import Table

conn = DB("test")

daily_data = Table(conn,
              name="DailyData",
              columns={"date": datetime,
                        "ticker": str,
                        "field": str,
                        "value": float},
              primary_keys=['date', 'ticker', 'field'])

daily_data.upsert([{"date": datetime(2022, 2, 1),
                        "ticker": "AAPL",
                        "field": "PX_LAST",
                        "value": 6.}])

daily_data.delete()
```