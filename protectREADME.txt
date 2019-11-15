On Debian, Ubuntu, Linux Mint:

$ sudo apt-get install python-pip

Once PIP installed, run the following command to install ‘rm-protection’.

$ sudo pip install rm-protection

Protect Files From Accidental Deletion In Linux  using rm-protection

rm-protection works exactly like ‘rm’ command. The only difference is it will ask you to answer a question. It consists of two utilities namely rm-p and protect. Here, ‘rm-p’ will remove the files and ‘protect’ utility will protect your files from the accidental or intentional deletion. Allow me to explain with some examples.

First, make an alias for ‘rm-p’ and ‘protect’ utilities for easy convenience. This is optional. If you don’t create alias, you need to type rm-p each time when you want to delete a file.

$ alias rm="rm-p"

$ alias protect=protect

Let us say, we have an important file called ostechnix.txt.

To protect this file, run:

$ protect ostechnix.txt

You will be asked a question and its answer to protect the above file.

Question for /home/sk/ostechnix.txt: Do you love Linux?
Answer: Yes I do