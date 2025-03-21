"""Traffic signal control module for adaptive traffic optimization"""


def adjust_signal_cycle(vehicle_count: int) -> int:
    """Adjust green light duration based on vehicle count.

    Args:
        vehicle_count: Number of vehicles detected at intersection

    Returns:
        int: Green light duration in seconds (30-60)
    """
    base_green_time = 30
    max_green_time = 60

    if vehicle_count > 50:
        return min(base_green_time + 20, max_green_time)
    if vehicle_count > 20:
        return base_green_time + 10
    return base_green_time
