su - a script that switches the current user
whoami - a script that prints the effective username of the current user
groups - a script that prints all the groups
chown - a script that changes the owner of the file
touch - a script that creates an empty file
chmod 744 -  a script that adds execute permission to the owner
chmod 774 - a script that adds execute permission to the owner and the group owner, and read permission to other users
chmod a+x - a script that adds execution permission to the owner, the group owner and the other users without commas
chmod 007 - a script that adds all permissions to Other users
chmod 753 - a script that sets the mode of the file -rwxr-x-wx
chmod --reference=FILE1 FILE2 - a script that sets the mode of the FILE2 the same as FILE1
chmod a+X *  - a script that adds execute permission to all subdirectories of the current directory for all
mkdir -m 751 DIR - a script that creates a DIR directory with permissions 751
chgrp NEWOWNER FILE -  a script that changes the group owner
chown -R NEWOWNER:GRPOWNER ./*  - a script that changes the owner and the group owner for all the files and directories
chown -h NEWOWNER:GRPOWNER FILE  - a script that changes the owner and the group owner respectively
chown --from=OLDOWNER NEWOWNER FILE  - a script that changes the owner only if the owner is specified
telnet towel.blinkenlights.nl  - a script that will play the StarWars IV episode in the terminal.
