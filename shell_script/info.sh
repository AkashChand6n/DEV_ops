echo "==========================================================="
echo "System information"
uname -a
echo "==========================================================="

echo "==========================================================="
echo "Memory information"
cat /proc/meminfo
echo "==========================================================="

echo "==========================================================="
echo "Disk information"
lsblk
echo "==========================================================="
#uname is a command in Unix and Unix-like operating systems that prints system information. It stands for "Unix Name". It can also be used to print certain system information, such as the kernel version or the name of the machine.
#meminfo is a command in Unix and Unix-like operating systems that prints memory information. It stands for "Memory Information". It can also be used to print certain memory information, such as the total memory available or the memory used.
#diskinfo is a command in Unix and Unix-like operating systems that prints disk information. It stands for "Disk Information". It can also be used to print certain disk information, such as the total disk space available or the disk space used.