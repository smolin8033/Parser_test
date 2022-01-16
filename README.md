<h1>Installation</h1>

Clone parser's repo from GitHub:

`git clone https://github.com/smolin8033/Parser_test.git`

Install virtualenv:

`pip install virtualenv`

Choose a place in your local machine for a new virtualenv.
Then, create a new virtualenv:

`virtualenv newenv`

To activate it for Windows type into PowerShell:

`path_to_your_virtualenv/newenv/Scripts/activate`

To activate it for MacOS or Linux type into Terminal (bash):

`source newenv/bin/activate`

Then, enter into the cloned project directory, where you
cann see the file requirements.txt . Install all the
dependencies with the command:

`pip install -r requirements.txt`

Then, you can run the parser in your PowerShell(Windows) or
Terminal(MacOS or Linux bash) by typing:

`python parser_test.py`