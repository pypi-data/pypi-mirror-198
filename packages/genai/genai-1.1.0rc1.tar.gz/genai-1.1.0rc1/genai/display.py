from enum import Enum
import os
from binascii import hexlify
from IPython.core import display_functions
from typing import Any, Iterator, Union, Optional, Tuple, Dict


class Stage(str, Enum):
    """The stage of feedback generation"""

    STARTING = "starting"
    GENERATING = "generating"
    FINISHED = "finished"


class GenaiMarkdown:
    """
    A class for displaying a markdown string that can be updated in place.

    This class provides an easy way to create and update a Markdown string in Jupyter Notebooks. It
    supports real-time updates of Markdown content which is useful for emitting ChatGPT suggestions
    as they are generated.

    Attributes:
        message (str): The Markdown string to display
        stage (Optional[Stage]): The current stage of feedback generation

    Example:
        >>> from genai.display import GenaiMarkdown, Stage
        ...
        >>> markdown = UpdatingMarkdown()
        >>> markdown.append("Hello")
        >>> markdown.append(" world!")
        >>> markdown.display()
        # Displays "Hello world!" in the notebook
        ...
        >>> markdown.append(" This is an update!")
        # Displays "Hello world! This is an update!" in the notebook
        ...
        >>> def text_generator():
        ...    yield " 1"
        ...    yield " 2"
        ...    yield " 3"
        ...
        >>> markdown.consume(text_generator())
        # Displays "Hello world! This is an update! 1 2 3" in the notebook
    """

    assists = {}

    def __init__(
        self, message: str = " ", stage: Optional[Stage] = None, execution_count=None
    ) -> None:
        self._message: str = message
        self._display_id: str = hexlify(os.urandom(8)).decode('ascii')
        self._stage: Optional[Stage] = stage

        if execution_count:
            self.assists[execution_count] = self

    def append(self, delta: str) -> None:
        self.message += delta

    def consume(self, delta_generator: Iterator[str]) -> None:
        for delta in delta_generator:
            self.append(delta)

    def display(self) -> None:
        '''Display the `UpdatingMarkdown` with a display ID for receiving updates'''
        display_functions.display(self, display_id=self._display_id)

    def update_displays(self) -> None:
        '''Force an update to all displays'''
        display_functions.display(self, display_id=self._display_id, update=True)

    def __repr__(self) -> str:
        return self._message

    def _repr_markdown_(self) -> Union[str, Tuple[str, Dict[str, Any]]]:
        if self._stage is None:
            return self._message

        metadata = {
            "genai": {
                "stage": self._stage,
            }
        }

        return self._message, metadata

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, value: str) -> None:
        self._message = value
        self.update_displays()

    @property
    def stage(self) -> Optional[Stage]:
        return self._stage

    @stage.setter
    def stage(self, stage: Stage) -> None:
        self._stage = stage
