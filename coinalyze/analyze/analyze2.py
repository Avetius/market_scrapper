
import sys
sys.path.append("..")

from .. import models
import exp
# from models import Session, GateioOI
# from exp import update_to_datetime
import matplotlib.pyplot as plt
import time
import json

start_time = time.time()
session = models.Session()

# Query all records from the table
# all_records = session.query(GateioOI).all()

# from 2024-01-12 09:02:08.927 1705050113170 to 2024-01-12 12:17:47.710 1705061864295

# Query records with a specific condition (example: timestamp within the last day)
records = session.query(models.GateioOI).filter(
    models.GateioOI.symbol == 'ASTRA_USDT.Y',
    models.GateioOI.time >= '2024-01-12 12:12:35.786',
    models.GateioOI.time <= '2024-01-12 12:32:18.967',
    ).order_by(models.GateioOI.update).all()

# Print the results
print(f"result >>> {len(records)}")
value = []
update = []
for record in records:
    value.append(record.value)
    update.append(record.update)
    print(record.time, record.value, record.update)
# update, values = zip(*records)
upd = update_to_datetime(update)

# Plot the graph using matplotlib
plt.plot(upd, value, label='GateioOI Data')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('GateioOI Data Plot')
plt.legend()
plt.show()


# Close the session
session.close()
end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f"cycle time {round(float(execution_time), 3)} ms")
