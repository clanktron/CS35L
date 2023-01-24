# Assignment 1

>Note: I'm using vim rather than emacs for the following Labs/Homework. If a TA is grading this 
please note that I already consulted with Professor Eggert confirming this was okay.

For grading conveniece purposeses the './simulate' script can be called to run the vim commands that I recorded. 
This will download the necessary files and output the resulting edits/diffs to the scratchwork directory.
The scratchworkbk directory contains the results of my manual edits; these should be the same as the output of the given script.

A dockerfile is also included for running the script in a controlled environment.
```sh
# If you are unfamiliar with docker then you can simply copy the following commands.
$ docker build -t assign1 .
$ docker run -v $PWD/scratchwork/:/assignment/scratchwork assign1
```

All vim motions and answers for the labs are documented in markdown files in the notes directory.
You can also view the viminfo files in the vimscriptbk directory for the exact commands that are run on said html files.

The c file and its resulting binary are in the junk folder along with their outputs.

The myspell script is in the spellscript directory along with the sorted.words dictionary file.
