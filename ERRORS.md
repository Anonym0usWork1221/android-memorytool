# Known Errors

1. **__ERROR [No 5]: input/output error__**  
   Source [Detail Error](https://linuxpip.org/errno-5-input-output-error/)

````
Input/output error is a general error message that happens all the time under different situation. It indicates a problem in filesystem level, more specifically, the operating system cannot access a certain part of the disk drive (or virtual disk drive).
In this article, we will explain the possible reasons why the “errno 5 input/output error” message happens and a few solutions that might help solving it.

“[Errno 5] Input/output error” causes

Before we get into any further, let’s make it clear that the error indicates a problem happens with the disk while the operating system is writing or reading from it. The error is specific to Linux machines.
Sometimes, especially in situation where you’re running Linux as a virtual machine, the cause of “[Errno 5] Input/output error” might be related to the hypervisor. Try updating VMware or VirtualBox to see if the problem goes away.
Windows is currently under heavy development with changes are made every few months, that makes running a virtual machine more complex than ever. On Windows machines, you have to pay attention to Hyper-V to see if it plays nicely with VirtualBox or VMware. If Hyper-V causes the problem, you would have no choice but update VMware or VirtualBox (or reinstall Windows, of course).

“OSError: error no 5 input/output error” with Python

It doesn’t really matter that you are using Django, Odoo, PyTorch or low-level libraries like pexpect or shutil, if there’s something wrong while reading/writing data to the disk, “OSError: errno 5 input/output error” might be the first error you will see.
There’s a couple of things you can try, depends on your specific scenario :

1. Check the disk for errors. On Windows, you can run chkdsk. 
2. On Linux, there is fsck. If there are recoverable errors, they’ll be fixed. 
3. After that, your Python program may run without any issue.
4. Carefully inspect the permissions of the folder/directory you’re working in. It should include appropriate read/write permission.
5. Replace the disk drive to see if the problem goes away. If it does, then your disk drive is faulty.

````
