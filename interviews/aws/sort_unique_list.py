### Can you please implement the following
# Given a 100MB JSON file <input.json> that looks similar to this:
arr = [
        {
            "charles": 3918
        },
        {
            "alice": 0
        },
        {
            "bob": 100
        },
        {
            "charles": 3918
        },
        {
            "django": 77
        },
        {
            "alice": 0
        }
        ]
# Please print the given pairs sorted (by value), without the duplicates.

def unique_arr(arr):
    arr_unique = set()
    for item in arr:
        for k, v in item.items():
            arr_unique.add((k, v))
    return arr_unique

def sort_arr(arr):
    arr_sorted = sorted(arr,
                        key=lambda x:x[1],
                        reverse=True)
    return arr_sorted



def test_unique_arr(orig_arr, expected_arr):
    assert unique_arr(orig_arr) == expected_arr
    print('unique_arr PASSED')
    
def test_sort_arr(orig_arr, expected_arr):
    assert sort_arr(orig_arr) == expected_arr
    print('sort_arr PASSED')

arr = [{'charles': 3918}, {'alice': 0}, {'bob': 100}, {'charles': 3918}, {'django': 77}, {'alice': 0}]
excepted_arr = {('bob', 100), ('django', 77), ('charles', 3918), ('alice', 0)}
test_unique_arr(arr, excepted_arr)

print(arr)
print(unique_arr(arr))