def merge_sort(list):
    """
    Sorts a list in ascending order
    :param list:
    :return: a new sorted list
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists in previous step
    Combine: Merge the sorted sublists created in previous step
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    :param list:
    :return: two sublists - left and right
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right
