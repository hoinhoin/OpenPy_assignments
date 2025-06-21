#Table of Contents   
[TOP](#top)   
[PS](#ps)   
[JOBS](#jobs)   
[KILL](#kill)   


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

# jobs

### Purpose

Displays status of jobs in the current session.

```bash
jobs [  -l | -n | -p ] [ JobID ... ]
```

### Description

The `jobs` command displays the status of jobs started in the current shell environment, showing information for all active jobs when no specific JobID is specified, and automatically removing terminated jobs from the shell's process list. Since it operates within the shell's job control system, it's implemented as a built-in command in Korn shell and POSIX shell rather than as a standalone executable like `/usr/bin/jobs`, which cannot function properly in its own execution environment due to lack of applicable jobs to manipulate. The command outputs process IDs one per line when the `-p` flag is used, or provides detailed job information in a multi-field format when no flags are specified.

| **Item** | **Description** |
| --- | --- |
| **-l** | Provides more information about each job listed. (job number, current job, process group ID, state, command that initiated the job) |
| **-n** | Displays only jobs that have stopped or exited since last notified. |
| **-p** | Displays the process IDs for the process group leaders for the selected jobs. |

# kill

### Purpose

Sends a signal to running processes.


### Description

The `kill` command sends signals to running processes, defaulting to the SIGTERM signal which normally terminates processes, and requires specifying the process ID (PID) which can be found through background process reports from the shell or using the `ps` command. Root users can terminate any process, while regular users can only kill processes they initiated, and the command accepts signal names (case-insensitive, without SIG prefix) or numbers, with signal number 0 used specifically to validate PID existence without actually sending a termination signal.

| **Option / Argument** | **Description** |
| --- | --- |
| **-s {SignalName | SignalNumber}** | Sends the specified signal by name or number (e.g., -s KILL or -s 9). |
| **-SignalName** | Sends the specified signal using its name (e.g., -HUP). |
| **-SignalNumber** | Sends the specified signal using its number (e.g., -9); use `--` to avoid confusion with PID. |
| *ProcessID* | Sends the signal to a specific process or group based on the value of PID. |
| **-l** | Lists all supported signal names. |
| **-l ExitStatus** | Shows the signal name for a given exit status or signal number. |

# Examples

1. To stop a given process, enter the following command:This stops process  by sending it the default **SIGTERM** signal. Note that process  might not actually stop if it has made special arrangements to ignore or override the **SIGTERM** signal.
    
    ```bash
    kill 1095
    ```
    
2. To stop several processes that ignore the default signal, enter the following command:This sends signal 9, the **SIGKILL** signal, to processes  and . The **SIGKILL** signal is a special signal that normally cannot be ignored or overridden.
    
    
    ```bash
    kill -kill 2098 1569
    ```
    
3. To stop all of your processes and log yourself off, enter the following command:This sends signal 9, the **SIGKILL** signal, to all processes that have a process group ID equal to the senders process group ID. Because the shell cannot ignore the **SIGKILL** signal, this command also stops the login shell and logs you off.
    
    
    ```bash
    kill -kill 0
    ```
    
4. To stop all processes that you own, enter the following command:This command sends signal 9, the **SIGKILL** signal, to all processes that are owned by the effective user, even those processes that are started at other workstations and that belong to other process groups. If a listing that you requested is being printed, it is also stopped.
    
    
    ```bash
    kill -9 -1
    
    ```
    
5. To send a different signal code to a process, enter the following command:The name of the **kill** command is misleading because many signals, including **SIGUSR1**, do not stop processes. The action that is taken on **SIGUSR1** is defined by the particular application you are running.

