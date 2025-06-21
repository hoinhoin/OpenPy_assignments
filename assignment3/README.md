# top

The **`top`** (**t**able **o**f **p**rocesses) command shows a dynamic, real-time view of running processes and **kernel**-managed tasks in Linux. The command also provides a system information summary that shows resource utilization, including **CPU** and **memory usage**.

The **`top`** command has the following basic syntax:

```
top [options]
```

Run **`top`** without any options to display a live view of all processes running on the system:

```
top
```

| Option | Name |
| --- | --- |
| **`-h`** | Help |
| **`-v`** | Version |
| **`-b`** | Batch mode |
| **`-c`** | Toggle command line/program name |
| **`-d [secs.tenths]`** | Delay time interval |
| **`-e [k | m | g | t | p]`** | Toggle task memory scaling |
| **`-E [k | m | g | t | p | e]`** | Toggle summary memory scaling |
| **`-H`** | Threads mode operation |
| **`-i`** | Idle process toggle |
| **`-n`** | Limit iteration number |
| **`-o [field name]`** | Overwrite sort field |
| **`-O`** | Output field names |
| **`-p [N1, N2...]`** | Monitor process IDs mode |
| **`-s`** | Secure mode operation |
| **`-S`** | Cumulative time toggle |
| **`-u | -U [ID or name]`** | User filter mode |
| **`-w [number]`** | Output width override |
| **`-1`** | Single/separate CPU states toggle |
