notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

class Scale(object):
    def __init__(self, tonic, intervals="mmmmmmmmmmm"):
        self.pitches = self.generate_pitches(tonic.upper(), intervals)

    def generate_pitches(self, tonic, intervals="mmmmmmmmmmm"):
        steps = {'m': 1, 'M': 2, 'A': 3}
        start_idx = notes.index(tonic)
        results = [tonic]
        for interval in intervals:
            start_idx += steps[interval]
            note = notes[start_idx % len(notes)]
            if note != tonic:
                results.append(note)
        return results

    def convert_flat(flat_note):
        note = flat_note[0]
        idx = notes.index(note)
        sharp_note = idx - 1
        return notes[sharp_note]
