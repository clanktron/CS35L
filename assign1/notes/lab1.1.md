# Lab 1.1 (Moving around in Emacs)

1. Use Emacs to edit the file exer1.html.

To open a file with vim simply type "vim exer1.html".

2. Move the cursor to just after the first occurrence of the word "HTML" (all upper-case).

In vim to find a word simply press "/" and type what you are looking for.
In this case "/HTML<CR>" (<CR> means the enter key) will bring your cursor to the first instance of "HTML" in the document (assuming your cursor is at the beginning of the file).
You can then simply press "el" which will bring you to one space past the end of the word.

3. Now move the cursor to the start of the first later occurrence of the word "scavenger".

Type /scavenger<CR> to jump to the first occurrence of scavenger.

4. Now move the cursor to the start of the first later occurrence of the word "self-referential".

Type /self-referential<CR> to jump to the first occurrence of self-referential.

5. Now move the cursor to the start of the first later occurrence of the word "arrow".

Type /arrow<CR> to jump to the first later occurrence of arrow.

6. Now move the cursor to the end of the current line.

To jump to the end of the current line in vim simply type "$".

7. Now move the cursor to the beginning of the current line.

To jump to the beginning of the current line type "0".

8. Doing the above tasks with the arrow keys takes many keystrokes, or it involves holding down keys for a long time. Can you think of a way to do it with fewer keystrokes by using some of the commands available in Emacs?

Doing these movements is trivial in vim and the arrow keys are not needed.

9. Did you move the cursor using the arrow keys? If so, repeat the above steps, without using the arrow keys.

No.

10. When you are done, exit Emacs.

To exit vim type :q


