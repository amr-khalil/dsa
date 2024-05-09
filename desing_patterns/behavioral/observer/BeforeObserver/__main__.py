from collections import namedtuple
from itertools import starmap

data = (('new', 10), ('open', 20), ('closed',30))
nt = namedtuple('KPI', 'name value')
KPI_Data = starmap(nt, data)

print(list(KPI_Data))

# Report on current KPI values
for kpi in KPI_Data:
    if kpi.name == 'open':
        print(f'Current open tickets: {kpi.value}')
    elif kpi.name == 'new':
        print(f'New tickets in last hour: {kpi.value}')
    elif kpi.name == 'closed':
        print(f'Tickets closed in last hour: {kpi.value}')
