class BowlingGame(object):
    def __init__(self):
        self.scores = 0
        self.current_frame = 1
        self.current_pins = 10
        self.throw = 1
        self.previous_states = []

    def roll(self, pins):
        if pins > 10 or pins < 0:
            raise ValueError("Invalid pins")
        if self.current_frame > 10 and all([state == [] for state in self.previous_states]):
            raise IndexError("Invalid frame")
        self.bonus_score(pins)
        if self.current_frame <= 10:
            self.scores += pins
        if self.throw == 1:
            if pins == 10:
                if self.current_frame <= 10:
                    self.previous_states.append(["strike", "strike"])
                    self.reset()
            else:
                self.current_pins -= pins
                self.throw += 1
        elif self.throw == 2:
            if pins == self.current_pins:
                if self.current_frame <= 10:
                    self.previous_states.append(["spare"])
            elif pins < self.current_pins:
                pass
            else:
                raise ValueError("Pins must be less than current_pins")
            self.reset()
        

    def reset(self):
        self.current_frame += 1
        self.current_pins = 10
        self.throw = 1

    def bonus_score(self, pins):
        for state in self.previous_states:
            if len(state) > 0:
                self.scores += pins
        self.previous_states = [state[1:] for state in self.previous_states if len(state) > 0]

    def score(self):
        if self.current_frame < 10 or any([state != [] for state in self.previous_states]):
            raise IndexError("Incomplete game")
        return self.scores
