"""
module for data redaction models.
"""
# pylint:disable=E0611,R0903
from typing import Dict, List, Optional, Union

from pydantic import BaseModel

from postman.model.dynamic_model import DynamicBaseModel
from postman.model.http import HTTPVerbEnum


class Rules(DynamicBaseModel):
    """
    Rules object
    """

    __root__: Dict[str, str]


class ExcludeConditionSet(BaseModel):
    """
    Exclude rules structured.
    """

    method: Optional[HTTPVerbEnum] = None
    url: Optional[str] = None


class ExcludeConditions(DynamicBaseModel):
    """
    List type supporting string or ExcludeConditionSet
    """

    __root__: Optional[List[Union[str, ExcludeConditionSet]]] = None


class DataRedactionConfig(BaseModel):
    """
    DataRedaction config model.
    """

    enable: bool = True
    rules: Rules
    exclude: Optional[ExcludeConditions]
