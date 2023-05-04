from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParameterOptT")


@attr.s(auto_attribs=True)
class ParameterOptT:
    """
    Example:
        {'description': 'Sapiente possimus commodi qui sint aut.', 'value': 'Dolorem velit quia.'}

    Attributes:
        description (Union[Unset, str]):  Example: Atque asperiores architecto facere..
        value (Union[Unset, str]):  Example: Repudiandae quis numquam cumque magnam molestiae voluptates..
    """

    description: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        value = d.pop("value", UNSET)

        parameter_opt_t = cls(
            description=description,
            value=value,
        )

        parameter_opt_t.additional_properties = d
        return parameter_opt_t

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
