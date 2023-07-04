# Dictionaries in Python

Dictionaries in Python are unordered collections of key-value pairs. They are also known as associative arrays or hash maps. Dictionaries are defined using curly braces `{}` and consist of comma-separated key-value pairs.

## Creating a Dictionary

```python
# Creating an empty dictionary
my_dict = {}

# Creating a dictionary with initial values
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```
## Accessing Values
```python
# Accessing a value using the key
value = my_dict['key1']
print(value)  # Output: value1
```
## Modifying and Adding Elements
```python
# Modifying a value
my_dict['key2'] = 'new_value'

# Adding a new key-value pair
my_dict['key4'] = 'value4'
```
## Dictionary Methods
- **keys()** : Returns a list of all the keys in the dictionary.
- **values()** : Returns a list of all the values in the dictionary.
- **items()** : Returns a list of tuples, where each tuple contains a key-value pair.
```python
# Using dictionary methods
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(keys)   # Output: dict_keys(['key1', 'key2', 'key3', 'key4'])
print(values) # Output: dict_values(['value1', 'new_value', 'value3', 'value4'])
print(items)  # Output: dict_items([('key1', 'value1'), ('key2', 'new_value'), ('key3', 'value3'), ('key4', 'value4')])
```
## Iterating Through a Dictionary
```python
# Iterating through keys
for key in my_dict:
    print(key)

# Iterating through values
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)
```
## Checking Key Existence
```python
# Using the 'in' operator
if 'key1' in my_dict:
    print("Key exists")
else:
    print("Key does not exist")
```
## Removing Elements
```python
# Removing a key-value pair
del my_dict['key3']

# Removing all elements
my_dict.clear()
```
