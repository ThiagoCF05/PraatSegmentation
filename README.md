This script aims to segment a .wav file based on .TextGrid file, format used by Praat. The script (main.py) is build on top of the textgrid.py script, distributed by NLTK prject.

To segment a .wav file, run the following command:

python main.py src dest

"src" is the directory where the .wav and .TextGrid file(s) are. Both .wav and .TextGrid files should have the same name.

"dest" is the directory where the segmented chunks shoul be writeen. 
