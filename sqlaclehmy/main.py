import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.core import SyncCore
from queries.orm import SyncORM

# реализация через core
# SyncCore.create_tables()
# SyncCore.insert_workers()
# SyncCore.select_workers()
# SyncCore.update_worker()
# SyncCore.select_workers()

# реализация через ORM
SyncORM.create_tables()
SyncORM.insert_workers()
SyncORM.select_workers()
SyncORM.update_worker()
