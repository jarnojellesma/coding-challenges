"""
Credits: https://www.dailycodingproblem.com/

You are the technical director of WSPT radio, serving listeners nationwide. For
simplicity's sake we can consider each listener to live along horizontal line
stretching from 0 (west) to 1000 (east). Given a list of N listeners, and a list
of M radio towers, each placed at various locations along this line, determine
what the minimum broadcast range would have to be in order for each listener's
home to be covered.

For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15]. In
this case the minimum range would be 5, since that would be required for the
tower at position 15 to reach the listener at position 20.
"""
import math
import unittest
import typing as t


def determine_shortest_distance(listener: int, towers: t.List) -> int:
    """ Determine the distance to the closest radio tower.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param listener: radio listener
    :param towers: radio towers
    :returns distance to closest radio tower
    """
    return min([abs(tower - listener) for tower in towers])


def determine_min_broadcast_range(listeners: t.List[int], towers: t.List[int]) -> int:
    """ Determine the minimum broadcast range to reach all listeners.

    Time Complexity: O(n^2)
    Space Complexity: O(n)

    :param listeners: list containing position of each listener on the horizontal axis
    :param towers: list containing position of each tower on the horizontal axis
    :returns minimum broadcast range
    """
    return max([determine_shortest_distance(listener, towers)
                for listener in listeners])


def determine_closest_towers(listeners: t.List[int], towers: t.List[int]) -> t.List:
    """ Determine the distance to the closest radio tower.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param listeners: radio listeners
    :param towers: radio towers
    :returns list of distances to the closest tower for each listener
    """
    distances = [math.inf for _ in listeners]
    j = 0
    for i, listener in enumerate(listeners):
        if listener > towers[j] and listener > towers[j] and j + 2 < len(towers):
            j += 1
        if listener < towers[j]:
            distances[i] = abs(towers[j] - listener)
        else:
            distance_a = abs(towers[j] - listener)
            distance_b = abs(towers[j + 1] - listener)
            distances[i] = min(distance_a, distance_b)
    return distances


def determine_min_broadcast_range_2(listeners: t.List[int], towers: t.List[int]) -> int:
    """ Determine the minimum broadcast range to reach all listeners.

    This version of the algorithm assumes the input is sorted.

    Computational complexity when input is already sorted:
        Time Complexity: O(n)
        Space Complexity: O(n)

    Computational complexity when sorting is part of the algorithm:
        Time Complexity: O(n log n)
        Space Complexity: O(n)

    :param listeners: list containing position of each listener on the horizontal axis
    :param towers: list containing position of each tower on the horizontal axis
    :returns minimum broadcast range
    """
    return max(determine_closest_towers(listeners, towers))


class Test(unittest.TestCase):
    def test_1(self):
        result = determine_min_broadcast_range(
            [1, 5, 11, 20], [4, 8, 15])
        self.assertEqual(5, result)

    def test_2(self):
        result = determine_min_broadcast_range_2(
            [1, 5, 11, 20], [4, 8, 15])
        self.assertEqual(5, result)


if __name__ == '__main__':
    unittest.main()

