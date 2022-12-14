from datetime import datetime, timedelta
from collections import Counter
import re

with open('input4.txt') as file:
    raw_dates = file.read().splitlines()

from_str_to_date = lambda x: datetime(*[int(i) for i in re.split(r'[-:\s]', re.search(r'\d[^\]]+', x).group(0))])
srtd_dates = sorted(raw_dates, key=from_str_to_date)

guards = dict()
for timestamp in srtd_dates:
    match = re.search(r'(?<=#)\d+', timestamp)
    if match:
        guard = int(match.group(0))
    if guard in guards:
        guards[guard].append(timestamp)
    else:
        guards[guard] = [timestamp]

asleep_time = {g: [] for g in guards}
for guard in guards:
    calc = False
    for action in guards[guard]:
        if 'falls' in action:
            asleep_time[guard].append(from_str_to_date(action))
            calc = True
        elif calc:
            asleep_time[guard].append(from_str_to_date(action))
            calc = False

total_sleep_time = {g: sum((asleep_time[g][i]-asleep_time[g][i-1]).seconds
                           for i in range(1, len(asleep_time[g]), 2)) for g in asleep_time}

sleepiest_guard = max(total_sleep_time.items(), key=lambda x: x[1])[0]
sleepiest_times = asleep_time[sleepiest_guard]
default_delta = timedelta(seconds=60)

minutes = []
for t in range(0, len(sleepiest_times), 2):
        current = sleepiest_times[t]
        while current != sleepiest_times[t+1]:
            minutes.append(current.minute)
            current += default_delta

#soluzione 1
print(Counter(minutes).most_common()[0][0] * sleepiest_guard)

max_asleep_minute = [0, 0]
for guard in asleep_time:
    asleep_guard = asleep_time[guard]
    if not asleep_guard:
        continue
    minutes = []
    for t in range(0, len(asleep_guard), 2):
        current = asleep_guard[t]
        while current != asleep_guard[t + 1]:
            minutes.append(current.minute)
            current += default_delta
    most_common = Counter(minutes).most_common()[0]
    if most_common[1] > max_asleep_minute[1]:
        max_asleep_minute = most_common
        max_asleep_guard = guard

#soluzione 2 (un po' rozzo, si potrebbe fare un refactoring per trasformarlo in una funzione della prima parte)
print(max_asleep_minute[0] * max_asleep_guard)
