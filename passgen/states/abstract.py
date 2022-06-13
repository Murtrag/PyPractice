from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def prompt(self) -> None:
        pass

    @abstractmethod
    def perform(self) -> None:
        pass
