from typing import Iterator, List, Set, Tuple

def compute_pairings(
    matrix: List[List[int]] | Iterator[List[int]],
    options: LoPhatOptions | None = None,
) -> PersistenceDiagram:
    """
    Decomposes the input matrix, using the lockfree or standard algorithm (according to options).

    :param matrix: The boundary matrix, provided in sparse column format, either as a list of lists or an iterator of lists.
    :param options: Options to control the R=DV decomposition algorithm.
    :returns: The persistence pairings read off from the R=DV decomposition.
    """

class LoPhatOptions:
    """
    A class representing the persistence diagram computed by LoPHAT.
    Each column index in the input matrix appears exactly once, either in a pairing or as unpaired.

    :param maintain_v: Whether to maintain_v during decompositon, usually best left False.
    :param num_threads: Max number of threads to use. Set at 0 to use all threads. Set at 1 to use standard, serial algorithm.
    :param column_height: Optional hint to height of columns. If None, assumed that matrix is square.
    :param max_chunk_len: Maximum size of a chunk, given to each thread.
    """

    def __init__(
        self,
        maintain_v: bool = False,
        num_threads: int = 0,
        column_height: int | None = None,
        max_chunk_len: int = 1,
    ) -> None: ...

class PersistenceDiagram:
    """
    A class representing the persistence diagram computed by LoPHAT.
    Each column index in the input matrix appears exactly once, either in a pairing or as unpaired.

    :param unpaired: The set of input column indices that were not paired in the R=DV decomposition.
    :param paired: The set of (birth, death) pairs of column indices that were paired in the R=DV decomposition.
    """

    unpaired: Set[int]
    paired: Set[Tuple[int, int]]
