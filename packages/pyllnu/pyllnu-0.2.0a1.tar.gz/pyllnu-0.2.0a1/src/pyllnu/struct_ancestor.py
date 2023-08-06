from typing import Any
from ctypes import BigEndianStructure

class StructAncestor(BigEndianStructure):
    def get_properties(self) -> dict[str, Any]:
        return {
            field[0]: self.__getattribute__(field[0])
            for field in self._fields_
        }
