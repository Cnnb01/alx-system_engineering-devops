0x05. Processes and Signals
Overview
This repository contains Bash scripts and examples related to the topic of "Processes and Signals" for the ALX-HIGHER program in system engineering and DevOps.

Scripts
ps_examples.sh

Description: Demonstrates the usage of the ps command to display information about processes.
Usage: ./ps_examples.sh
pgrep_pkill_examples.sh

Description: Provides examples of using pgrep and pkill to find and signal processes by name.
Usage: ./pgrep_pkill_examples.sh
kill_trap_examples.sh

Description: Illustrates the usage of the kill command and setting traps with the trap command.
Usage: ./kill_trap_examples.sh
exit_example.sh

Description: Shows how to use the exit command to terminate a script with a specific status.
Usage: ./exit_example.sh
Processes and Signals Overview
Processes are instances of executing programs in a computer system. They are managed by the operating system and have unique identifiers called Process IDs (PIDs).

Commands and Concepts Covered:
ps:

Display information about currently running processes.
Example: ps aux
pgrep:

Find the process ID of a running program.
Example: pgrep firefox
pkill:

Send a signal to a process based on its name.
Example: pkill -SIGTERM firefox
kill:

Send a signal to a process or a job.
Example: kill -9 1234
exit:

Exit the current shell or script.
Example: exit 0
trap:

Set up a command to be run when the script receives a signal.
Example: trap "echo 'Exiting...'; exit" INT TERM