import ast
from typing import List
from pydantic import BaseModel, BaseSettings


class ParserConfig(BaseSettings):
    type: str

    class Config:
        extra = "forbid"


class Parser(BaseModel):
    """Base class for all parsers

    Parsers are used to parse the AST of the generated python code. They can be used to
    modify the AST before it is written to the file."""

    config: ParserConfig

    def parse_ast(
        self,
        asts: List[ast.AST],
    ) -> List[ast.AST]:
        ...  # pragma: no cover
