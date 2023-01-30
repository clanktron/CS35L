# Assignment 2. Lisp and Python scripting

## Exercise 2.2: Scripting Emacs

## Homework: Python scripting

Consider the old-fashioned Python 2 script randline.py.

1) What happens when this script is invoked on an empty file like /dev/null, and why?

The program throws an IndexError because there are no lines in /dev/null.

2) What happens when this script is invoked with Python 3 rather than Python 2, and why? 

It throws a syntax error because certain builtins of python2 are not compatible with python3.

3) Use Emacs to write a new script shuf.py in the style of randline.py but using Python 3 instead. Your script should implement the GNU shuf 
command that is part of GNU Coreutils. GNU shuf is written in C, whereas you want a Python implementation so that you can more easily 
add new features to it. Your program should run on /usr/local/cs/bin/python3 as installed on SEASnet.

 Your program should support the following shuf options, with the same behavior as GNU shuf: 
    --echo (-e), 
    --input-range (-i), 
    --head-count (-n), 
    --repeat (-r), 
    --help. 
    As with GNU shuf, if --repeat (-r) is used without --head-count (-n), your program should run forever. 
    Your program should also support zero non-option arguments or a single non-option argument “-” (either of which means read from standard input), 
    or a single non-option argument other than “-” (which specifies the input file name). 
    Your program need not support the other options of GNU shuf. 
    As with GNU shuf, your program should report an error if given invalid arguments.

Your solution should use the argparse module instead of the obsolescent optparse. It should not import any modules other than argparse, string 
and the non-optparse modules that randline.py already imports. Don’t forget to change its usage message to accurately describe the modified behavior.

4) What happens when your shuf.py script is invoked with Python 2 rather than Python 3, and why?

It throws a syntax error due to certain semantics of passing variables not being backwards compatible.

5) The Python 3.11 release notes say that Python 3.11 is significantly faster than older releases. Can you measure the performance difference? 
Use Bash’s time command to compare the performance of your implementation when run via SEASnet’s /usr/bin/python3 (which should predate Python 3.11), 
versus running it via /usr/local/cs/bin/python3 (which should be Python 3.11 or later), versus running Coreutils /usr/local/cs/bin/shuf. 
Use Bash commands like the following to time these three benchmarks (this example is for Coreutils, and assumes /usr/local/cs/bin is at the 
start of your PATH):

  `time shuf < /usr/share/unicode/ucd/BidiTest.txt > /dev/null`

For each of these three benchmarks, run the benchmark at least three times on the text file shown above, and report the median of the sum of the user 
and system times. Do your benchmarks on the same SEASnet host, and document the CPU and operating system version of the SEASnet host you used 
by consulting the lscpu command and the /etc/os-release file. If your Python implementation runs on /usr/local/cs/bin/python3 but 
not /usr/bin/python3, do not benchmark it on the latter; instead, briefly explain which features of the newer Python your program relies on, and why. 

The median time for the program to execute with the newer python compiler was 0m0.501s. The median time for the program to execute with the older python compiler was 0m0.711s. 
The processor used was a Intel(R) Xeon(R) Silver 4116 CPU @ 2.10GHz and the host OS was RHEL (Red Hat Enterprise Linux). The program is compatible with both python3 binaries.
