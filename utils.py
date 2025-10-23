from numbers import Number

# refactoring
def validate_positive_number(value):  
# validation code:
    if not isinstance(value, Number): # otherwise if not isinstance(new_value, (int, float)):
        raise TypeError(f"Value must be a number not {type(value)}.") # chat gpt
    if value<=0:
        raise ValueError(f"Value cannot be negative/zero as {value}")