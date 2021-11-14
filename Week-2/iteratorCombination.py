# https://leetcode.com/problems/iterator-for-combination/
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self._characters = characters
        self._combination_length = combinationLength
        self._indices = list(range(self._combination_length))
        self._exausted = False

    def _shift_indices(self) -> None:
        for i in reversed(range(self._combination_length)):
            if self._indices[i] != i + len(self._characters) - self._combination_length:
                last_not_max_index = i
                break
        else:
            self._exausted = True
            return
        self._indices[last_not_max_index] += 1
        for j in range(last_not_max_index+1, self._combination_length):
            self._indices[j] = self._indices[j-1] + 1

    def next(self) -> str:
        result = ''.join(self._characters[i] for i in self._indices)
        self._shift_indices()
        return result

    def hasNext(self) -> bool:
        return not self._exausted


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
