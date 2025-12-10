import time
import statistics
from dataclasses import dataclass, field
from typing import List

@dataclass
class Metrics:
    requests_count: int = 0
    total_duration: float = 0
    durations: List[float] = field(default_factory=list)

    def add_request(self, duration: float):
        self.requests_count += 1
        self.total_duration += duration
        self.durations.append(duration)

    def get_summary(self):
        if not self.durations:
            return "No requests recorded."
        
        return {
            "count": self.requests_count,
            "avg_duration": self.total_duration / self.requests_count,
            "min_duration": min(self.durations),
            "max_duration": max(self.durations),
            "median_duration": statistics.median(self.durations)
        }

class Instrumentor:
    def __init__(self):
        self.metrics = Metrics()

    def record(self, start_time: float):
        duration = time.time() - start_time
        self.metrics.add_request(duration)
        return duration

