# Root Directory Structure of Linux

> Vidath Dissanayake | Sri Lanka
> Tags: #OS/Linux 

## /boot

Contains static files required to boot the system, such as the kernel. These files are essential for the system to boot properly. If files are missing it may go into emergency mode or grub mode.


## /dev 

Contains device nodes that either represent devices that are attached to the system or virtual devices that are provided by the kernel.

## /etc

Contains configuration files that are local to the machine. No binaries are placed here.

## /bin

Contains the essential user programs that must be present when the system is mounted in single-user mode. These include important system programs and utilities such as the bash shell, `cat`, `cd`.

## /sbin 

Contains the essential binaries that are intended to be run by the root user for system administration.  
E.g: `fdisk`

## /home

Contains a home folder for each user. For example, for the user “vidath”, the home folder is `/home/vidath`. This home folder contains Desktop, Downloads, Documents, etc…

## /lib & /lib64

Contains libraries needed by the binaries in `/bin` and `/sbin`. Libraries required by `/usr/bin` are located in `/usr/lib`.

## /media & /mnt 

