from textgrid import TextGrid
from scipy.io import wavfile
from unicodedata import normalize
import argparse

import os

def parse(write_dir, grid, audio, person):
	# find the tier with the chunks
	tiers = filter(lambda x: x.nameid == 'Categ', grid.tiers)[0].simple_transcript

	# frequency, length and duration of the audio
	freq = int(audio[0])
	length = len(audio[1])
	duration = float(length)/freq # in seconds

	for i, interval in enumerate(tiers):
		s1 = (float(interval[0]) * length) / duration
		s2 = (float(interval[1]) * length) / duration

		fname = str(i) + '_' + interval[2] + '_' + person + '.wav'
		wavfile.write(os.path.join(write_dir, fname), freq, audio[1][int(s1):int(s2)])

def main(read_dir, write_dir):
	files = os.listdir(read_dir)
	if '.DS_Store' in files:
		files.remove('.DS_Store')
	files = set(map(lambda x: x.split('.')[0], files))

	for f in files:
		try:
			print 'File ', f, '\r'
			faudio = os.path.join(read_dir, f+'.wav')
			audio = wavfile.read(faudio)

			fgrid = os.path.join(read_dir, f+'.TextGrid')
			grid = normalize('NFKD', open(fgrid).read().decode('latin-1')).encode('ascii', 'ignore').replace('\x00', '')
			if grid[0] == 'y':
				grid = TextGrid(grid[1:])
			else:
				grid = TextGrid(open(fgrid).read())

			person = f.split('_')[-1]
			if not os.path.exists(os.path.join(write_dir, f)):
				os.makedirs(os.path.join(write_dir, f))
			parse(os.path.join(write_dir, f), grid, audio, person)
		except:
			print 'Error in file ', f

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Segmentation of a .wav file based on its .TextGrid annotation.')
	parser.add_argument("src", help="directory with the read files", type=str)
	parser.add_argument("dest", help="directory where the chunks should be written", type=str)
	args = parser.parse_args()

	read_dir = args.src
	write_dir = args.dest

	main(read_dir, write_dir)
