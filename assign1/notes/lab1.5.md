# Lab 1.5 (Exploring the operating system outside Emacs)

1. Where are the sh, sleep, and type commands located?

Using the command "whereis" we can find the location of commands/executables.
sh: /usr/bin/sh /usr/share/man/man1p/sh.1p.gz /usr/share/man/man1/sh.1.gz
The first result is the command and the others are the zipped man pages.
sleep: /usr/bin/sleep /usr/local/cs/bin/sleep /usr/share/man/man3/sleep.3.gz /usr/share/man/man1p/sleep.1p.gz /usr/share/man/man1/sleep.1.gz /usr/share/man/man3p/sleep.3p.gz
The first result is the command, the second is another instance of it at a different location, and the others are the zipped man pages.
type: /usr/bin/type /usr/share/man/man1p/type.1p.gz /usr/share/man/man1/type.1.gz
The first result is the command and the others are the zipped man pages.

2. What executable programs in /usr/bin have names that are exactly three characters long and start with the two letters se, and what do they do?

The command "find /usr/bin -maxdepth 1 -executable -name "se?" will return those desired. Executeables "seq" and "sed" are the only ones that meet this criteria.
"seq" prints a sequence of numbers in the range specified.
"sed" can be used to modify text; this could be from some sort of input stream or an actual file.

3. When you execute the command named by the symbolic link /usr/local/cs/bin/emacs, which file actually is executed?

The actual executable is /usr/local/cs/emacs-28.2/bin/emacs-28.2

4. What is the version number of the /usr/bin/gcc program? of the plain gcc program? Why are they different programs?

"/usr/bin/gcc --version" tells me that it's version 8.5.0. Whereas the gcc on path (/usr/local/cs/bin/gcc which is a symlink to /usr/local/cs/gcc-12.2.0/bin/gcc) is version 12.2.0.
There are sometimes multiple copies of gcc on a system in order to compile programs that require a certain version.
    
5. The chmod program changes permissions on a file. What does the symbolic mode u+sx,o-w mean, in terms of permissions?

The "u+sx" part means the user/owner is being granted execute permissions and that anyone else who attempts to use the file will do so "as the user", meaning in this case they will always have execute permissions.
The "o-w" part means other users not in the group are being stripped of write permissions.
    
6. Use the find command to find all directories modified on or after the day of this class’s first lecture, that are located under (or are the same as) the directory /usr/local/cs.

Running "find . -type d -newermt "2023-01-10" -ls" will output all the files modified on or after the specified date in "ls -dils" format. I specified this format to double check the date of the outputted directories.
In this case there are none, however running the same command for January 9th (simply change the last "-10 to -09"; one day before the first lecture) we can see there were a large amount of directories modified.
The full list of these is in the following [file](./before-Jan-9-2023.txt).
    
7. Of the files in the same directory as find, how many of them are symbolic links?

The "whereis" command states that "find" is in /usr/bin/. Running "find . -maxdepth 1 -type l" in this directory outputs all of the symbolic links there.
Now we can count how many there are by either redirecting the stdout to a file and checking the line count of such...or as a more straightforward solution we can pipe the previous command to "wc -l" to just get the number.
I.e. "find . -maxdepth 1 -type l | wc -l" which returns 327.
    
8. What is the oldest file in the /usr/lib64 directory? Use the last-modified time to determine age. Specify the name of the file without the /usr/lib64/ prefix. Don't ignore files whose names start with ".", but do ignore files under subdirectories of /usr/lib64/. Consider files of all types, that is, your answer might be a regular file, or a directory, or something else.

The command "find /usr/lib64/ -maxdepth 1 -printf '%T+ %p\n' | sort | head -n 1" returns the oldest file in the directory. In this case it is libbz2.so which is a symlink. 
Running "ls -la /usr/lib64/libbz2.so" tells us the file was modified back in 2018.
    
9. In Emacs, what commands have transpose in their name?

Emacs can "transpose" (switch) a number of "things". These being transpose-chars, transpose-words, transpose-lines, transpose-sexps (balanced expressions), transpose-lines, transpose-sentences, transpose-paragraphs, and transpose-regions.
The equivalent can be done with vim through plugins or custom scripting (lua, vimscript, language of choice, etc), though personally this is not a common enough occurrence for me to add such to my config.
    
10. What does the Emacs yank function do, and how can you easily invoke it using keystrokes?

The emacs yank function pastes text from your clipboard, or more precisely your last "kill"/delete. This is opposite to vim in which yank means to copy a selection of text.
Pasting is instead just called pasting in vim and can be executed by pressing "p" (paste after), or "P" (paste before).
    
11. When looking at the directory /usr/bin, what's the difference between the output of the ls -l command, and the directory listing of the Emacs dired command?

Dired has a certain level of interactability that ls does not have, the full extent of such can also be modified. It also outputs the amount of available space at said path which ls does not include. 
    
12. Use the ps command to find your own login shell's process, all that process's ancestors, and all its descendants. Some ps options that you might find useful include -e, -f, -j, -l, -t, -H, and -T.

"ps -e" can be used to get all processes on the system. "ps -ejH" and "ps axjf" can both be used to show a process tree of the ancestors and descendants of the current processes.
A better tool for viewing process trees is the "pstree" command. 
That being said something like "top" (or the fancier htop) is more useful for general purpose process monitoring, as ps and pstree only give snapshots of the system at a point in time.


