from music21 import *
import random

# creates a random twelve-tone row
pitchList = list(range(12))
random.shuffle(pitchList)
noteList = [note.Note(thisPitch) for thisPitch in pitchList]

# puts the row into a stream
myStream = stream.Stream()
myStream.append(noteList)

if __name__ == '__main__':
    myStream.show()