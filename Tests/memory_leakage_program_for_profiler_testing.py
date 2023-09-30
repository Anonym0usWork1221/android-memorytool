import os
import time


class MemoryLeak:
    def __init__(self):
        self.data = []

    def leak_memory(self):
        while True:
            self.data.extend([1] * 1000000)  # Allocate more memory
            time.sleep(0.1)


if __name__ == "__main__":
    memory_leak = MemoryLeak()
    print(f"PID: {os.getpid()}")
    print("Running memory leak...")
    memory_leak.leak_memory()

