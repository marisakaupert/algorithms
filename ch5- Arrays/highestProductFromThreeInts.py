from itertools import islice

def highest_product_of_3(A):

    if len(A) < 3:
        raise Exception('Less than 3 items!')

    # we're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # we could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(A[0], A[1])
    lowest  = min(A[0], A[1])

    highest_product_of_2 = A[0] * A[1]
    lowest_product_of_2  = A[0] * A[1]

    # except this one--we pre-populate it for the first *3* items.
    # this means in our first pass it'll check against itself, which is fine.
    highest_product_of_3 = A[0] * A[1] * A[2]

    # walk through items, starting at index 2
    for current in islice(A, 2, None):

        # do we have a new highest product of 3?
        # it's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_3 = max(
            highest_product_of_3,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        # do we have a new highest product of two?
        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_3

print(highest_product_of_3([-10, -10, 1, 3, 2]))
