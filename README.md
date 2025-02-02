# Oracle Common packages

This repository serves as the common packages for Fondation.

## List of packages

### AzureORM

Responsible for holding the tables and ORM definition used across oracle.
In order to use it:
```python
import azureorm
from azureorm.tables import BaciSparseTradeVolume

orm = azureorm.setup(
    "your-server-name",
    "your-db-name", 
    1433
)

with orm.query_context(BaciSparseTradeVolume) as query:
    results = query.limit(10).all()
    print(results)
```
