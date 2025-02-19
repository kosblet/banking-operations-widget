from src.processing import filter_by_state, sort_by_date

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Тест filter_by_state
filtered_executed = filter_by_state(data)
print("Filtered by EXECUTED:", filtered_executed)

filtered_canceled = filter_by_state(data, state='CANCELED')
print("Filtered by CANCELED:", filtered_canceled)

# Тест sort_by_date
sorted_desc = sort_by_date(data)
print("Sorted descending:", sorted_desc)

sorted_asc = sort_by_date(data, ascending=True)
print("Sorted ascending:", sorted_asc)
