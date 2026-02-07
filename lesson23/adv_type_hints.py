from typing import Optional, Any, List, Union

from mainnnnn import number


def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name())

# type hintat-optional,union,any,list

def get_value(value: Union[int, str]) -> str:
    if isinstance(value,int):
        return f"Number: {value}"
    return f"String: {value}"

print(get_value(1))

def get_any_value(value: Any):
    return value
print(get_any_value("hi"))

# def get_v(value: List[int]) -> int:
#   return sum(value)
# numbers = [1,2,3]
# print(get_v(numbers))

def sum_list(num: List[int]) -> int:
    return sum(num)

numbers: List[int] = [1,2,3]
result: int = sum_list(numbers)
print(result)

