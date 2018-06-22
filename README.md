# PE Meta Extractor

A simple extractor of information for PE files

## Installation

Python 3

pip install -r requirements.txt

## Usage

Dump the PE meta information only to console
python main.py --pefile "C:\Program Files (x86)\Notepad++\notepad++.exe" -d
Save it to a log file
python main.py --pefile "C:\Program Files (x86)\Notepad++\notepad++.exe" -d -o report

Hash all the icons with most common image hashes (save them into a file)
python main.py --pefile "C:\Program Files (x86)\Notepad++\notepad++.exe" -i -o report
Save also all the icons:
python main.py --pefile "C:\Program Files (x86)\Notepad++\notepad++.exe" -i -s -o report
Save just the primary icon (the one that windows show for the exe):
python main.py --pefile "C:\Program Files (x86)\Notepad++\notepad++.exe" -i -s -m -o report
