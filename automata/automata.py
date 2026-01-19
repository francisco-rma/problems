from string import ascii_lowercase


class DFA:
    def __init__(self, q, sigma, delta, q0, f):
        """
        Initializes a Deterministic Finite Automaton (DFA).

        Args:
            q: The set of states.
            sigma: The set of symbols in the alphabet.
            delta: The transition function.
            q0: The initial state.
            f: The set of final states.
        """
        self.states = q
        self.symbols = sigma
        self.delta = delta
        self.q0 = q0
        self.f = f

    def __repr__(self):
        return f"DFA{self.states},\n\t{self.symbols},\n\t{self.delta}"

    def run(self, word: str):
        q = self.q0
        while word:
            q = self.delta[q][word[0]]
            word = word[1:]

        return q in self.f
