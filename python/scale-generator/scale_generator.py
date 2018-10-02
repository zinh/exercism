class Scale(object):
    def __init__(self, tonic, intervals="mmmmmmmmmmmm"):
        self.pitches = self.generate_pitches(tonic, intervals)

    def generate_pitches(self, tonic, intervals="mmmmmmmmmmmm"):
        notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        steps = {'m': 1, 'M': 2, 'A': 3}
        start_idx = notes.index(tonic.upper())
        results = [tonic.upper()]
        for interval in intervals:
            start_idx += steps[interval]
            results.append(notes[start_idx % len(notes)])
        return results
