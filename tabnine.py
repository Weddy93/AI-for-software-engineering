def sort_dicts_by_key(list_of_dicts, key):
    
    if not isinstance(list_of_dicts, list):
        raise TypeError("list_of_dicts must be a list")
    for item in list_of_dicts:
        if not isinstance(item, dict):
            raise TypeError("All elements in list_of_dicts must be dictionaries")

    return sorted(list_of_dicts, key=lambda d: d.get(key, ''))

# Example usage and tests
if __name__ == "__main__":
    # Basic test
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    sorted_data = sort_dicts_by_key(data, "age")
    print("Basic sort by age:", sorted_data)

    # Test with different key
    sorted_by_name = sort_dicts_by_key(data, "name")
    print("Sort by name:", sorted_by_name)

    # Test with non-existing key
    sorted_by_missing = sort_dicts_by_key(data, "height")
    print("Sort by missing key:", sorted_by_missing)

    # Test empty list
    empty_data = []
    sorted_empty = sort_dicts_by_key(empty_data, "age")
    print("Empty list:", sorted_empty)

    # Test single dict
    single_data = [{"name": "Alice", "age": 30}]
    sorted_single = sort_dicts_by_key(single_data, "age")
    print("Single dict:", sorted_single)

  
    try:
        sort_dicts_by_key("not a list", "age")
    except TypeError as e:
        print("Error for non-list:", e)


    try:
        sort_dicts_by_key([{"name": "Alice"}, "not a dict"], "age")
    except TypeError as e:
        print("Error for non-dict element:", e)
