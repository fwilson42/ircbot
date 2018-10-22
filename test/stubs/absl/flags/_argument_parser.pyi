# Stubs for absl.flags._argument_parser (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class _ArgumentParserCache(type):
    def __call__(cls, *args: Any, **kwargs: Any): ...

class ArgumentParser:
    syntactic_help: str = ...
    def parse(self, argument: Any): ...
    def flag_type(self): ...

class ArgumentSerializer:
    def serialize(self, value: Any): ...

class NumericParser(ArgumentParser):
    def is_outside_bounds(self, val: Any): ...
    def parse(self, argument: Any): ...
    def convert(self, argument: Any) -> None: ...

class FloatParser(NumericParser):
    number_article: str = ...
    number_name: str = ...
    syntactic_help: Any = ...
    lower_bound: Any = ...
    upper_bound: Any = ...
    def __init__(self, lower_bound: Optional[Any] = ..., upper_bound: Optional[Any] = ...) -> None: ...
    def convert(self, argument: Any): ...
    def flag_type(self): ...

class IntegerParser(NumericParser):
    number_article: str = ...
    number_name: str = ...
    syntactic_help: Any = ...
    lower_bound: Any = ...
    upper_bound: Any = ...
    def __init__(self, lower_bound: Optional[Any] = ..., upper_bound: Optional[Any] = ...) -> None: ...
    def convert(self, argument: Any): ...
    def flag_type(self): ...

class BooleanParser(ArgumentParser):
    def parse(self, argument: Any): ...
    def flag_type(self): ...

class EnumParser(ArgumentParser):
    enum_values: Any = ...
    case_sensitive: Any = ...
    def __init__(self, enum_values: Any, case_sensitive: bool = ...) -> None: ...
    def parse(self, argument: Any): ...
    def flag_type(self): ...

class EnumClassParser(ArgumentParser):
    enum_class: Any = ...
    def __init__(self, enum_class: Any) -> None: ...
    def parse(self, argument: Any): ...
    def flag_type(self): ...

class ListSerializer(ArgumentSerializer):
    list_sep: Any = ...
    def __init__(self, list_sep: Any) -> None: ...
    def serialize(self, value: Any): ...

class CsvListSerializer(ArgumentSerializer):
    list_sep: Any = ...
    def __init__(self, list_sep: Any) -> None: ...
    def serialize(self, value: Any): ...

class BaseListParser(ArgumentParser):
    syntactic_help: Any = ...
    def __init__(self, token: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    def parse(self, argument: Any): ...
    def flag_type(self): ...

class ListParser(BaseListParser):
    def __init__(self) -> None: ...
    def parse(self, argument: Any): ...

class WhitespaceSeparatedListParser(BaseListParser):
    def __init__(self, comma_compat: bool = ...) -> None: ...
    def parse(self, argument: Any): ...
