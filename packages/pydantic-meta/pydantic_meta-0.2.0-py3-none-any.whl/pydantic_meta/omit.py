from types import UnionType
from typing import get_origin, Union

from pydantic.main import ModelMetaclass


class Omit(ModelMetaclass):
    """
        Example
            class Test(BaseModel, metaclass=Omit):
                name: str
                age: int

                class Config:
                    omit_fields = ['age']
    """
    def __new__(cls, name, bases, namespaces, **kwargs):
        omit_fields = []
        fields = namespaces.get('__fields__', {})
        config = namespaces.get('Config', False)

        if config and (omit_fields := getattr(config, 'omit_fields', False)):
            omit_fields = omit_fields

        for base in bases:
            if base_field := getattr(base.Config, 'omit_fields', False):
                omit_fields.extend(base_field)

            fields.update(base.__fields__)

        instance = super().__new__(cls, name, bases, namespaces, **kwargs)

        for field in instance.__fields__:
            model_field = instance.__fields__[field]
            name = hasattr(model_field, "alias") and model_field.alias or field

            if name not in omit_fields:
                if get_origin(model_field.annotation) in (UnionType, Union):
                    setattr(model_field, 'allow_none', True)

        return instance
