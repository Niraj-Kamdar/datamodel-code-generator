# generated by datamodel-codegen:
#   filename:  reference_to_object_properties.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Pet(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None


class Parent(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    pet: Optional[Pet] = None


class Child(BaseModel):
    id: Optional[str] = None
    parent_id: Optional[str] = None
    name: Optional[str] = None
    pet: Optional[Pet] = None
