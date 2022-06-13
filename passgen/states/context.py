from __future__ import annotations


class AppContext:
    _state = None

    def __init__(self, state: State) -> None:
      self.transition_to(state)
      
    @property
    def transition_to(self, state: State):
        self._state = state
        self._state.context = self
