This script aims to segment a .wav file based on a .TextGrid file (format used by Praat). The script (main.py) is build on top of the textgrid.py script, distributed by NLTK project.

To segment a .wav file, run the following command:

python main.py src dest

"src" is the directory where the .wav and .TextGrid files are. Both .wav and .TextGrid files should have the same name for a specific audio.

"dest" is the directory where the segmented chunks should be written. 
