# Lab 1.2 (Deleting text in Emacs)

1. Use Emacs to edit the file exer2.html. The idea is to delete its HTML comments; the resulting page should display the same text as the original.

Open file with "vim exer2.html". General approach will be searching for "<!--", selecting the section and then deleting such.

2. Delete the 69th line, which is an HTML comment. <!-- HTML comments look like this, but the comment you delete has different text inside. -->

Jump to line 69 by typing ":69". Delete the line by typing "dd".

3. Delete the HTML comment containing the text "DELETE-ME DELETE-ME DELETE-ME".

The line with that text is only 11 lines below the other comment, so we can just type "11j" to move 11 lines down and then "dd" to delete the line.

4. Delete the HTML comment containing the text "https://en.wikipedia.org/wiki/HTML_comment#Comments".

To find the line I typed "/<!-- You<CR>" which took me to the proper comment. I then pressed "V" to highlight/select the entire line. 
Pressing "2j" will move the cursor down two lines, selecting the rest of the comment. The selection can then be deleted by pressing "d" or "x".

5. There are two more HTML comments; delete them too.

Typing "/<!--<CR>" took me to the first remaining comment, which I deleted in the same fashion as action #4. 
Pressing "n" takes you to the next instance of the last searched string...which in this case will take you to the last comment at the end of the file.
This last comment line can be deleted with "dd".

The file can then be saved with ":wq".


