# Lab 1.6 (Doing commands inside Emacs)

3. Compile this file, using the Emacs M-x compile command.

Doing this in vim is trivial. One can either define a custom command in their config and execute it with a custom keymap (what I did for this exercise) or type ":! gcc hello.c -o hello" to compile from within vim.

4. Run the compiled program from Emacs using the M-! command, and put the program's standard output into a file named hello-a1 and its standard error into a file hello-a2.

Similar to before we can run this shell command by typing ":! ./hello > hello-a1 2> hello-a2" from within vim.

5. Same as before, except run the program with standard input being closed, and put the program's standard output and error into hello-b1 and hello-b2, respectively. Here, “closed” does not mean the standard input is an empty file; it means that standard input is not open at all, to any file.

Similar to before we can run this shell command by typing ":! ./hello <&- > hello-b1 2> hello-b2" from within vim.

6. Same as before, except run the program with standard input being the file /etc/passwd, and put the program's standard output and error into hello-c1 and hello-c2.

Similar to before we can run this shell command by typing ":! ./hello < /etc/passwd > hello-c1 2> hello-c2" from within vim.

7. Same as before, except run the program with standard input being the file /etc/passwd and standard output being the file /dev/full, and put the program's standard error into hello-d2.

Similar to before we can run this shell command by typing ":! ./hello < /etc/passwd > /dev/full 2> hello-d2" from within vim.

