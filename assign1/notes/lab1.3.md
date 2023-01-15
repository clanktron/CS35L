# Lab 1.3 (Inserting text in Emacs)

1. Use Emacs to edit the file exer3.html.

Run "vim exer3.html".

2. Change the first two instances of "Assignment 1" to "Assignment 27".

Start at the beinning of the file. Seach for the string "Assignment 1" with "/Assignment 1<CR>".
Type "cgn" to remove the string and enter insert mode. Then type "Assignment 27<Esc>" to replace the string and exit insert mode.
You can repeat this action on the next instance of the searched string (aka "Assignment 1") by simply pressing ".".

3. Change the first instance of "UTF-8" to "US-ASCII".

Type "gg" to return to the beginning of the file. Type "/UTF-8<CR>" to jump to the first instance. Type "cgn" to remove it and enter insert mode.
Type the replacement string and exit insert mode with "US-ASCII<Esc>".

4. Ooops! The file is not ASCII so you need to fix that. Most of its non-ASCII characters are the Unicode character “’” (RIGHT SINGLE QUOTATION MARK U+2019); fix these by replacing each one with an ASCII “'” (U+0027 APOSTROPHE); for example, you can use M-x replace-string to do this systematically. Remove every line that contains a non-ASCII character other than U+2019. You can find the next non-ASCII character by searching for the regular expression "[^[:ascii:]]".
    
Every instance of the string "’" can be replaced in vim with ":%s/’/'".
Non-ASCII can be found in vim with "/[^[:ascii:]]<CR>". Simply press "dd" to delete the line it jumps you to.
Now press "n" followed by "dd" until you see the message "Pattern not found" at the bottom of the vim pane.

5. Insert an empty line after the last line containing "</ol>".
    
Press "G" to jump to the end of the document. Now type "?</ol><CR>" to reverse search for the string.
Now type "o<Esc>" to insert a newline below.

6. When you finish, save the text file and exit Emacs. As before, use the diff command to check your work.

Type ":wq" to save. The run the diff command and pipe to exer3.diff.


