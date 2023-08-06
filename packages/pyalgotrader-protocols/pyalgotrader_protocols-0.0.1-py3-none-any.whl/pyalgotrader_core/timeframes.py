from datetime import timedelta

timeframes = {
    timedelta(minutes=1): 1,
    timedelta(minutes=3): 2,
    timedelta(minutes=5): 3,
    timedelta(minutes=15): 8,
    timedelta(minutes=30): 16,
    timedelta(hours=1): 29,
    timedelta(hours=2): 50,
    timedelta(hours=3): 67,
    timedelta(hours=4): 100,
    timedelta(days=1): 200,
}
