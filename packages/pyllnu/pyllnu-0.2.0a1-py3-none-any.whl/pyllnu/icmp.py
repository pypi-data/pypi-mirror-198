
from dataclasses import dataclass
from src.pyllnu.struct_ancestor import StructAncestor


class ICMPHeader(StructAncestor):
    """
    RFC2463.
    """
    pass


@dataclass
class ICMPPacket:
    header: ICMPHeader
    data: bytes
