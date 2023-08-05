# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE
import sys

import awkward as ak
from awkward._nplikes.shape import unknown_length
from awkward._regularize import is_integer


class ArrayType:
    def __init__(self, content, length):
        if not isinstance(content, ak.types.Type):
            raise ak._errors.wrap_error(
                TypeError(
                    "{} all 'contents' must be Type subclasses, not {}".format(
                        type(self).__name__, repr(content)
                    )
                )
            )
        if not ((is_integer(length) and length >= 0) or length is unknown_length):
            raise ak._errors.wrap_error(
                ValueError(
                    "{} 'length' must be a non-negative integer or unknown length, not {}".format(
                        type(self).__name__, repr(length)
                    )
                )
            )
        self._content = content
        self._length = length

    @property
    def content(self):
        return self._content

    @property
    def length(self):
        return self._length

    def __str__(self):
        return "".join(self._str("", True))

    def show(self, stream=sys.stdout):
        stream.write("".join([*self._str("", False), "\n"]))

    def _str(self, indent, compact):
        return [f"{self._length} * ", *self._content._str(indent, compact)]

    def __repr__(self):
        args = [repr(self._content), repr(self._length)]
        return "{}({})".format(type(self).__name__, ", ".join(args))

    def __eq__(self, other):
        if isinstance(other, ArrayType):
            return (
                other._length is unknown_length
                or self._length is unknown_length
                or self._length == other._length
            ) and self._content == other._content
        else:
            return False
