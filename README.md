CUTEr Problem Chooser
=====================

Classificator: Leandro Prudente - lfprudente@gmail.com

Script to get files: Raniere Gaia Costa da Silva - r.gaia.cs@gmail.com

README and organization: Abel Soares Siqueira - abel.s.siqueira@gmail.com

Overview
--------

This program filters the problems of the CUTEr collection.
To achieve this objective **YOU MUST MODIFY** it according
to the type of problems you want to select.
See the end of __classification.f__ to see where your
modifications must be inserted.
The program creates a text file called **my\_problems**
containing the names of filtered problems.

See http://www.cuter.rl.ac.uk/Problems/classification.shtml for
a complete explanation of the CUTEr classification scheme.

To use this routine you must have a text file called **CUTEr\_problems **
with the names of all problems (line by line), and other text
file called **CUTEr\_classification** with the classifications of
all problems (line by line). 
This package came with a script called get_files.sh that you
can use to get these files.
You can also get this information on the
website http://www.cuter.rl.ac.uk/Problems/mastsif.shtml.
A simple way is to copy all the table with name, files
available and CUTEr classification, paste into a xlsx file
and extract the required information by copying and pasting the
first and third columns.

Installing and Running
----------------------

First, edit classification.f to reflect your needs. 
Then, use **get\_files.sh** to generate CUTEr\_problems and
CUTEr\_classification. You will need wget and sed installed.
Alternatively, you can see the recommendation on Overview
to generate these files. To use the script

    $ chmod a+x get_files.sh
    $ ./get_files.sh

Now simply compile the file classification.f. For instance, using
gfortran:

    $ gfortran classification.f -o classification

Now, run it.

    $ ./classification

License
-------

This software is available under the GNU Public License v.3,
which can be seen in COPYING.
Unless otherwise noted, all source is under this license.
