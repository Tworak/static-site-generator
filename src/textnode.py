from enum import Enum

class TextType(Enum):
    # Basic types of textual content that the static site generator may
    # encounter.  The enum is intentionally minimal; additional members can
    # be added as needed.
    TEXT = "text"
    LINK = "link"
    BOLD = "bold"
    CODE = "code"
    IMAGE = "image"
    ITALIC = "italic"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        """Return ``True`` when *other* is a :class:`TextNode` with the same
        attributes.

        The previous implementation compared ``self`` to ``other`` using
        ``==`` which called this very method again, leading to infinite
        recursion.  We now perform an explicit attribute comparison.
        """
        if not isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self) -> str:
            return f"TextNode({self.text}, {self.text_type.value}, {self.url})"