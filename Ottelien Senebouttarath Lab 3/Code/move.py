from dataclasses import dataclass


@dataclass(frozen=True)
class Move:
    player: int
    row: int
    column: int
