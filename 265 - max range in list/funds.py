IMPOSSIBLE = 'Mission impossible. No one can contribute.'
DIFF_USER = 1


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    fund, starting, ending = 0, 0, 0

    # if no villager can donate
    if max(village) < 1:
        print(IMPOSSIBLE)
    # if at least one villager can donate
    else:

        # we iterate through the possible donations
        current_sum, max_sum, max_sum_index, min_sum, min_sum_index = 0, 0, 0, 0, 0
        for donation_index, donation_value in enumerate(village):
            current_sum += donation_value

            # we save the highest fund position
            if current_sum > max_sum:
                max_sum = current_sum
                max_sum_index = donation_index

            # we save the lowest fund position
            elif current_sum < min_sum:
                min_sum = current_sum
                min_sum_index = donation_index

        starting = min_sum_index + 1 + DIFF_USER
        ending = max_sum_index + DIFF_USER
        fund = sum(village[starting-1: ending])

    return fund, starting, ending

