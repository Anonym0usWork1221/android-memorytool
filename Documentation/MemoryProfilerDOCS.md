# Memory Profiler Documentation

### Introduction 

This documentation outlines the steps to create and use a custom memory profiler using the `androidMemoryTool` library 
and the `MemoryProfiler` class provided in the code. The memory profiler is designed to monitor the memory usage of a 
specified process and log the data to a file or display it in the console.

### Prerequisites
Before using the memory profiler, make sure you have the following:
* Python 3.6 or greater installed on your system.
* The `androidMemoryTool` library, which contains the MemoryProfiler class.
* Knowledge of the Process ID (PID) or Name of the target process you want to profile.

### Basic Usage
If you want to use the MemoryProfiler class directly without the custom functions, 
you can do so by following these steps:

*  Create a MemoryProfiler instance and Start Profiling:
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG='ac_client')
profiler = tool.get_memory_profiler(logging_file_path='memory_log.txt')
profiler.start_profiling(threshold_in_mb=20.0,  # Look for 20mb threshold in target program  
                         verbose=True,   # Show output on screen
                         update_interval_delay=1.0,   # Recheck the memory of target program for next threshold
                         logging=True   # Save logs continuously in file after given interval
                         )
```

## Custom Memory Profiler
### Setting Up the Environment
* Import the necessary libraries and classes:
```python
from androidMemoryTool import AndroidMemoryTool
from time import sleep
from os import system
```
* Initialize an instance of `AndroidMemoryTool` with the package name (PKG) of the target process:
```python
tool = AndroidMemoryTool(PKG="ac_client")
```

* Obtain an instance of the MemoryProfiler class from the AndroidMemoryTool instance:
```python
profile_instance = tool.get_memory_profiler()
```

* Define the custom log file where memory data will be stored:
```python
custom_log_file = "memory_dump.txt"
```

### Custom Memory Logging Functions
Two custom functions are provided to handle memory data logging and printing:
* `custom_log_memory_data(data: list[dict])`: This function logs memory data to the specified file.
* `custom_print_function(data: list[dict])`: This function prints memory data to the console.
Make sure to modify these functions according to your requirements.

Example:
```python
def custom_log_memory_data(data: list[dict]) -> None:
    with open(custom_log_file, 'w') as log_file:
        log_file.write(f"{'Time':<10}{'Process RSS (BYTES)':<40}{'Memory Leak':<15}{'Memory Churn':<15}\n")
        for entry in data:
            log_file.write(f"{entry['time']:<10}{entry['process_memory']:<40}{entry['leak']:<15}{entry['churn']:<15}\n")


def custom_print_function(data: list[dict]):
    if AndroidMemoryTool.get_platform() == 'Windows':
        system("CLS")
    else:
        system("clear")
    formatted_status_print_header = f"{'Time':<10}{'Process RSS (MB)':<30}{'Memory Leak':<15}{'Memory Churn':<15}\n"
    current_body = formatted_status_print_header
    for entry in data:
        current_body += f"{entry['time']:<10}{entry['process_memory'] / (1024 * 1024):<30}{entry['leak']:<15}" \
                        f"{entry['churn']:<15}\n"
    print(current_body)
```

### Creating and Starting the Custom Profiler
* Define a function to start the custom memory profiler:
```python
def start_custom_profiler():
    threshold_in_mb: float = 20.0
    update_interval_delay: float = 1.0
    while True:
        try:
            # Retrieve memory data and store it
            profile_instance.current_memory_data(threshold_in_mb=threshold_in_mb)
            profile_instance.create_data_from_files()
            data = profile_instance.get_current_data()

            # Log memory data
            custom_log_memory_data(data=data)

            # Print memory data
            custom_print_function(data=data)

            sleep(update_interval_delay)
        except KeyboardInterrupt:
            print('Closing Program. Please wait.')
            break
```
* Call the `start_custom_profiler` function to begin memory profiling:
```python
start_custom_profiler()
```

### Customizing Memory Profiling
You can customize various aspects of the memory profiling process:
* Adjust the `threshold_in_mb` variable to set the memory usage threshold for detecting memory leaks and churn.
* Modify the `update_interval_delay` variable to control how often memory data is collected and logged.





