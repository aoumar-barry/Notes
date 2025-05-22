
# 🕒 Python Dates with `pendulum` – Summary

## Why Use `pendulum`?
- Simplifies working with dates/times
- Cleaner syntax than `datetime`
- Handles time zones and durations intuitively

## Installation
```bash
pip install pendulum
```

## Basics
```python
import pendulum

now = pendulum.now()
utc_now = pendulum.now("UTC")
custom = pendulum.datetime(2023, 5, 24, 15, 30)
```

## Parsing & Formatting
```python
dt = pendulum.parse("2023-05-24T15:30:00")
dt = pendulum.from_format("24/05/2023 15:30", "DD/MM/YYYY HH:mm")
formatted = dt.format("dddd, MMMM D, YYYY h:mm A")
```

## Arithmetic
```python
dt = pendulum.now()
dt.add(days=5)
dt.subtract(months=2)

# Difference
diff_days = (pendulum.datetime(2023, 5, 24) - pendulum.datetime(2023, 1, 1)).in_days()
```

## Durations
```python
duration = pendulum.duration(days=3, hours=5, minutes=30)
duration.total_seconds()
```

## Time Zones
```python
dt = pendulum.now("America/New_York")
dt.in_timezone("Asia/Tokyo")
```

## Comparisons
```python
dt1 < dt2
dt1.is_before(dt2)
dt2.diff(dt1).in_days()
```

## Periods & Ranges
```python
period = pendulum.period(pendulum.datetime(2023, 1, 1), pendulum.datetime(2023, 1, 10))
for dt in period.range("days"):
    print(dt)
```

## Best Practices
- Use aware datetimes (with time zones)
- Prefer `pendulum` for better handling
- Avoid naive `datetime` in production
