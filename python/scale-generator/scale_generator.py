notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
notes_alt = ['A', 'BB', 'B', 'C', 'DB', 'D', 'EB', 'E', 'F', 'GB', 'G', 'AB']

class Scale(object):
    def __init__(self, tonic, intervals="mmmmmmmmmmm"):
        self.pitches = self.generate_pitches(tonic.upper(), intervals)

    def generate_pitches(self, tonic, intervals="mmmmmmmmmmm"):
        if len(tonic) == 2 and tonic[-1] == 'B':
            base_notes = notes_alt
        elif tonic == 'F':
            base_notes = notes_alt
        else:
            base_notes = notes
        steps = {'m': 1, 'M': 2, 'A': 3}
        start_idx = base_notes.index(tonic)
        results = [self.format_note(tonic)]
        for interval in intervals:
            start_idx += steps[interval]
            note = base_notes[start_idx % len(base_notes)]
            if note != tonic:
                results.append(self.format_note(note))
        return results

    def format_note(self, note):
        if len(note) == 2 and note[-1] == 'B':
            return note[0] + 'b'
        return note
