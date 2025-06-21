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
| **`-e [k / m / g / t / p]`** | Toggle task memory scaling |
| **`-E [k / m / g / t / p / e]`** | Toggle summary memory scaling |
| **`-H`** | Threads mode operation |
| **`-i`** | Idle process toggle |
| **`-n`** | Limit iteration number |
| **`-o [field name]`** | Overwrite sort field |
| **`-O`** | Output field names |
| **`-p [N1, N2...]`** | Monitor process IDs mode |
| **`-s`** | Secure mode operation |
| **`-S`** | Cumulative time toggle |
| **`-u / -U [ID or name]`** | User filter mode |
| **`-w [number]`** | Output width override |
| **`-1`** | Single/separate CPU states toggle |

### **How to Interpret top Command Output**

The **`top`** command output is divided into several sections, each with specific information about system performance and processes. This section provides a breakdown of the output based on the information it shows.

### **Header Information**

This section shows basic system stats like [**uptime**](https://phoenixnap.com/glossary/what-is-uptime), [**active users**](https://phoenixnap.com/kb/how-to-list-users-linux), and recent system load:

- **`up`**. Displays the system running time since the last reboot.
- **`user(s)`**. Shows the current number of active users.
- **`load average`**. Lists the [**average system load**](https://phoenixnap.com/kb/linux-average-load) over the last 1, 5, and 15 minutes. Lower values indicate less CPU demand.

![Header information in the top command output.](https://phoenixnap.com/kb/wp-content/uploads/2024/10/header-information.png)

### **Tasks**

The *Tasks* section provides a quick overview of all running processes and their states:

- **`total`**. Indicates the number of processes currently running on the system.
- **`running`**. Number of processes actively using CPU resources.
- **`sleeping`**. Processes waiting for an event to continue (e.g., input/output).
- **`stopped`**. Processes that are paused or waiting for signals.
- **`zombie`**. Processes that have finished execution but remain in the process table.

![Task information from top output.](https://phoenixnap.com/kb/wp-content/uploads/2024/10/task-information.png)

### **CPU Usage**

This section shows how various processes are using the CPU.

- **`us`**. Time the CPU spends on user (non-kernel) processes.
- **`sy`**. Time spent on system/kernel processes.
- **`ni`**. Time spent on user processes with adjusted priority (nice values).
- **`id`**. Percentage of time the CPU is idle.
- **`wa`**. Time spent waiting for I/O operations (like disk access).
- **`hi`**. Time handling hardware interrupts.
- **`si`**. Time handling software interrupts.
- **`st`**. Time "stolen" from the [**virtual machine**](https://phoenixnap.com/glossary/what-is-a-virtual-machine) by the [**hypervisor**](https://phoenixnap.com/kb/what-is-hypervisor-type-1-2) (when using [**virtualization**](https://phoenixnap.com/kb/what-is-server-virtualization)).

![CPU usage information.](https://phoenixnap.com/kb/wp-content/uploads/2024/10/cpu-information.png)

### **Memory Usage (Mem)**

*Memory usage* stats explain how the system uses [**physical RAM**](https://phoenixnap.com/glossary/physical-memory).

- **`total`**. Total physical memory available.
- **`free`**. Unused RAM memory.
- **`used`**. Total memory in use by the system.
- **`buff/cache`**. Memory reserved for buffers and [**caches**](https://phoenixnap.com/glossary/what-is-cache). This memory can be reclaimed if needed by other processes.

![RAM memory usage in top.](https://phoenixnap.com/kb/wp-content/uploads/2024/10/memory-usage.png)

### **Swap Usage (Swap)**

The *Swap* section shows the disk-based memory usage, which the system uses when RAM is full.

- **`total`**. Total [**swap memory**](https://phoenixnap.com/kb/swap-memory) (disk-based memory used when RAM is full).
- **`free`**. Unused swap memory.
- **`used`**. Swap currently in use.
- **`avail Mem`**. Total memory available (sum of free and buffered memory).

![Swap memory usage information.](https://phoenixnap.com/kb/wp-content/uploads/2024/10/swap-usage.png)

### **Process List**

The *Process List* displays detailed information about each active process.

- **`PID`**. The process ID.
- **`USER`**. The user account that started the process.
- **`PR`**. Process priority.
- **`NI`**. Nice value, affecting scheduling priority.
- **`VIRT`**. Total virtual memory the process uses.
- **`RES`**. Resident memory (actual physical memory in use).
- **`SHR`**. Shared memory used by the process.
- **`S`**. Process state (e.g., **`S`** for sleeping, **`R`** for running).
- **`%CPU`**. Percentage of CPU time used by the process.
- **`%MEM`**. Percentage of RAM used by the process.
- **`TIME+`**. Total CPU time the process has consumed.
- **`COMMAND`**. The program, service, or command responsible for each active process.

![Process list in top command output.](https://phoenixnap.com/kb/wp-content/uploads/2024/10/process-list.png)


# ps

### Purpose

Shows status of processes. This document describes the standard AIX **ps** command and the System V version of the **ps** command.

### Description

The `ps` command displays information about active processes running on the system, showing process status to standard output and optionally including kernel threads with the `-m` flag. By default, it shows processes for the current terminal, while various flags like `-f`, `-o`, `-l`, `-s`, `-u`, and `-v` control the amount of detail displayed rather than which processes are listed. The command examines memory to determine original command names and parameters when processes were created, displaying kernel-stored names in square brackets when this information is unavailable, and has limitations including a maximum of 128 items for parameter lists and respect for the `COLUMNS` environment variable for screen formatting.

| **Option** | **Description** |
| --- | --- |
| **-A** | Displays information about all processes. |
| **-a** | Displays all processes except session leaders and those not associated with a terminal. |
| **-c** *Clist* | Displays only processes in the specified workload management classes. |
| **-d** | Displays all processes except session leaders. |
| **-e** | Displays all processes except kernel processes. |
| **-F** *Format* | Same as the `-o` *Format* option. |
| **-f** | Produces a full-format listing. |
| **-G** *Glist* | Displays only processes in the specified effective groups. |
| **-g** *Glist* | Displays only processes in the specified process groups. |
| **-k** | Displays kernel processes. |
| **-l** | Produces a long-format listing. |
| **-L** *pidlist* | Lists descendants of each process ID in the given list. |
| **-M** | Displays all 64-bit processes. |
| **-m** | Displays kernel threads along with processes. |
| **-N** | Omits thread statistics collection. |
| **-n** *NameList* | Specifies an alternate system namelist file. |

