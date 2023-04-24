from datetime import datetime as dt
from datetime import time as dt_time
from datetime import timezone

timestamp = 1673339018

tmp = dt.combine(dt.fromtimestamp(timestamp), dt_time.min)
print(int(tmp.replace(tzinfo=timezone.utc).timestamp()))

t1 = int(timestamp / 86400) * 86400
print(t1)
