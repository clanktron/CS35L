# Lab 1.4 (Other editing tasks in Emacs)

1. Execute the command "cat exer2.html exer2.diff >exer4.html" to create a file exer4.html that contains a copy of exer2.html followed by a copy of exer2.diff.
2. Use Emacs to edit the file exer4.html. The idea is to edit the file so that it looks identical to exer1.html on a browser, but the file itself is a little bit different internally.
3. Go to the end of the file. Copy the new lines in the last chunk of diff output, and paste them into the correct location earlier in the file.

First select the deleted lines with "V" and delete them with "d". Then jump to the line specified in the diff section (":linenumber<CR>") and paste the deleted line with "p".
The pasted line/lines will have an extra "-" at the front, so you will need to press "0" to jump to the beginning of the line, followed by "<C-v>" to select the "-".
If there were multiple lines to paste simply press "j" however many times is needed to move down and select all the extra "-". 
Then press "d" to delete the selected "-".

4. Repeat the process, until the earlier part of the file is identical to what was in the original.
5. Delete the last part of the file, which contains the diff output.

Jump to line 513 with ":513<CR>", as this is the beginning of the diff output. Press "V" to select the line, then "G" to jump to the end of the file (selecting all the remaining diff output).
Now press "d" to delete such.
    
6. … except we didn't really want to do that, so undo the deletion.

Simply press "u" to undo that action.
    
7. Turn the diff output into a comment, by surrounding it with "<!--" and "-->". If the diff output itself contains end-comment markers "-->", escape them by replacing each such "-->" with "--&gt;".
    
Jump to line 513 again with ":513<CR>". Press "i" for insert mode and type "<!-- <Esc>". 
Now type "G" to jump to the bottom/end of the diff and type "A" to jump to the end of the line and enter insert mode.
Now simply type " --><Esc>".

8. Now let's try some search and replaces. Search the text document for the pattern "<ol>". How many instances did you find? Use the search and replace function to replace them all with the final-caps equivalent "<oL>".

This can be accomplished with a single command ":%s/<ol>/<oL><CR>". 
This will replace all instances and give a message telling the number of instances replaced, in this case 6.
    
9. Check your work with viewing exer4.html with an HTML browser, and by running the shell command "diff -u exer1.html exer4.html >exer4.diff". The only differences should be changes from "<ol>" to "<oL>", and a long HTML comment at the end.

All should be well.


