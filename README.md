# noteterm
noteterm is a Python wrapper to quickly and efficiently create and view notes in the terminal. All notes are stored as .txt files and can be easily exported.

### Usage

##### Basic

|command  | functionality|
|----------|-------|
note	|			View this information
note -help	|		More information about noteterm
note -add (-a) ["title"] |	Add new note with optional title
note -view (-v)	|		View summary of all notes
note -view (-v) ["title"]|	Search for notes with particular title

#### Advanced
|command  | functionality|
|----------|-------|
note ["title"]	    |		If a note(s) with this title exists, show note;	otherwise, create a note with title
note -dir   	|		Print directory of note text files
note -about 		|	About this tool


### Setup
First, clone the repository:

`git clone git@github.com:samrawal/noteterm.git`

Then, create a symbolic link to the script so that the 'note' command can be used anywhere.

`ln -s $PWD/noteterm.py /usr/local/bin/note`
