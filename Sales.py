class Sales:
    def __getstate__(self):
        state = self.__dict__.copy()
        for key, value in state.items():
            state[key] = value.get()
        return state

    def __setstate__(self, state):
        for key, value in state.items():
            state[key] = StringVar()
            state[key].set(value)
        self.__dict__.update(state)
