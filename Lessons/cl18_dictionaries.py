"""examples of dictionary syntax with Ice Cream Shop order tallies"""

# Dictionary type is dict[key_type, value_type].
# Dictionaary literals are curly brackets
# that surround with key:value pairs.


ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawbery": 4,  # trailing comma
}

# len evaluates to number of key-value entries
print(len(ice_cream))

# Add key-value entries using subscription notation
ice_cream["mint"] = 10

# Acess values by their key using subscription
print(ice_cream["chocolate"])

# Re-assign values by their key using assignment
ice_cream["mint"] = ice_cream["mint"] + 1
ice_cream["mint"] += 1

# Remove items by key using the pop method
ice_cream.pop("strawberry")  # pop removes the value and returns
# the value that was popped at strawberry index

# Test if a  key is in dictionary
print("strawberry" in ice_cream)
