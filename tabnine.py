def sort_dicts_by_key(list_of_dicts, key):
    """
    Sorts a list of dictionaries by a specific key.

    Args:
    list_of_dicts (list): A list of dictionaries to be sorted.
    key (str): The key by which to sort the dictionaries.

    Returns:
    list: The sorted list of dictionaries.

    Raises:
    TypeError: If list_of_dicts is not a list or if elements are not dictionaries.
    """
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

    # Test error handling: non-list
    try:
        sort_dicts_by_key("not a list", "age")
    except TypeError as e:
        print("Error for non-list:", e)

    # Test error handling: non-dict in list
    try:
        sort_dicts_by_key([{"name": "Alice"}, "not a dict"], "age")
    except TypeError as e:
        print("Error for non-dict element:", e)
