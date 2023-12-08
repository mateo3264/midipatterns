from music21 import note, stream 
import random
import os
from os import path

RANGE_OF_NOTES = (48, 61)

def create_seq_notes(snd_path, filename, number_notes):
    notes = [note.Note(midi=random.randrange(*RANGE_OF_NOTES)) for _ in range(number_notes)]
    midi_notes = [n.pitch.midi for n in notes]
    

    

    with open(path.join(snd_path, filename), 'w') as f:
        f.write(','.join([str(mn) for mn in midi_notes]))

    s = stream.Stream(notes)
    n_scores = 0
    for file in os.listdir(snd_path):
        if 'score' in file and 'png' in file:
            n_scores += 1
        
    print('n_scores: ', n_scores)
    s.write('lilypond.png', path.join(snd_path, f'score{n_scores + 1}'))

    return midi_notes

# if __name__ == '__main__':
#     create_seq_notes()








