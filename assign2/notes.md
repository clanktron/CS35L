# Assignment 2. Lisp and Python scripting

## Exercise 2.1: Navigating through Emacs source code

1) The basic idea here is to get a mental model of how Emacs works by looking at a bit of its keybindings and source code. Start up a fresh Emacs with a *scratch* buffer.
To warm up, compute (2607 − 1) × (2607 − 1) (i.e., 2**(607 - 1) * (2**607 - 1)) in the *scratch* buffer, by using the expt and other functions. This is the 14th perfect number, discovered in 1952.

(* (expt 2 (- 607 1)) (- (expt 2 607) 1)) yields

1410537837067120690632079580860631898814867435147156678388386759999548677426523801141041933290376902515619505687098
2932716408772436637008711673126815931365248745065243980587729620729744672329516665822884692680778665287018892086787
9451478364569313922060370695064736073572378695176473055266826253284886383715072974324463835300053138429460296575143
368065570759537328128

2) Use Emacs to determine how many bits it would take to represent this number in base-2 notation (not counting any sign bit), by writing a Lisp expression that yields the number of bits as an integer.
Type M-: and use it to compute (2607 − 1) × (2607 − 1).

The expression (+ (logb (* (expt 2 (- 607 1)) (- (expt 2 607) 1))) 1) yields 1213 as the number of bits.

141053783706712069063207958086063189881486743514715667838838675999954867742652380114104193329037690251561950568709829327164087724366370087116731268159313652487450652439805877296207297446723295166658228846926\
807786652870188920867879451478364569313922060370695064736073572378695176473055266826253284886383715072974324463835300053138429460296575143368065570759537328128 (#o17777777777777777777777777777777777777777777\
777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777000000000000000000000000000000000000000000000000\
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, #x1ffffffffffffffffffffffffffffffffffffffffffffffff\
fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000)

3) Get a list of keybindings by typing C-h b. Look for two keybindings: C-h k and M-SPC. C-h k stands for “Type Control-h, then ‘k’.” M-SPC is “Meta Space”; 
on good keyboards you can get this by holding down Alt while hitting the space bar, but you may need to type “Esc” and then follow by hitting the space bar. 
We will examine these two keybindings in more detail. Type C-h k C-h k and describe what happens and why. (This should relate to the C-h b output mentioned previously.)

C-h K key displays the section of the Emacs manual that describes the command corresponding to key. 
Running C-h k for the command C-h k itself will display the description of C-h k in the pop up.

4) Type C-h k M-SPC and describe what happens and why. (This should also relate.)

M-SPC deletes all spaces and tabs around the point where our cursor is, leaving one space (or N spaces if specified). If N is negative, it deletes newlines as well, leaving -N spaces.
It runs the command just-one-space. When we run C-h k for the command M-SPC, the description of M-SPC pops up in the help window.

5) Try out M-SPC on some sample text with a lot of white space, to see how it works. Visit the source code for the function that implements M-SPC, by going to its help and clicking (or typing RET) on its source file name.
Notice how M-SPC is implemented in terms of a more-general function, which does not have a keybinding. Use M-: to execute this more-general function on a buffer, such that the function changes the buffer’s contents.
Similarly, use M-x to execute the more-general function on a buffer.

The general function for M-SPC keybinding is `cycle-spacing`.

## Exercise 2.2: Scripting Emacs

`gps-line()` was implemented in lua and can be tested by running the following docker commands in this directory.
```
$ docker build -t gps-line .
$ docker run -it -v $PWD:/mnt/volume gps-line
```
This will open vim and auto-source the gps-line.lua file. An easy keymap has been provided so simply hit the `space key` followed by the `i key` to trigger the 
line output from the function. The function can also be directly called by typing `:lua gps-line()`. This will return the proper line number juxtaposed with the total number of lines in the buffer.

>As vim does more robust parsing than emacs for what a "line" is, the newline count will always be greater than or equal to the current line (not desired functionality).
As this could only be achieved in vim through writing lengthy custom code to open the file and parse individual characters I have also included the solution for emacs (exhibits asked of behavior).

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
