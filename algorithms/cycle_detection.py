from typing import Callable

from data_structures.linked_list import LinkedList


def floyd_cycle_detection(mapping_function: Callable[[LinkedList], LinkedList], x0: LinkedList) -> (LinkedList, int):
    tortoise = mapping_function(x0)
    hare = mapping_function(mapping_function(x0))
    while tortoise is not hare:
        tortoise = mapping_function(tortoise)
        hare = mapping_function(mapping_function(hare))

    tortoise = x0
    while tortoise is not hare:
        tortoise = mapping_function(tortoise)
        hare = mapping_function(hare)

    cycle_length = 1
    hare = mapping_function(tortoise)
    while tortoise is not hare:
        hare = mapping_function(hare)
        cycle_length += 1

    return tortoise, cycle_length


def brent_cycle_detection(mapping_function: Callable[[LinkedList], LinkedList], x0: LinkedList) -> (LinkedList, int):
    power = cycle_length = 1
    tortoise = x0
    hare = mapping_function(x0)
    while tortoise is not hare:
        if power == cycle_length:
            tortoise = hare
            power *= 2
            cycle_length = 0
        hare = mapping_function(hare)
        cycle_length += 1

    tortoise = hare = x0
    for _ in range(cycle_length):
        hare = mapping_function(hare)

    while tortoise is not hare:
        tortoise = mapping_function(tortoise)
        hare = mapping_function(hare)

    return tortoise, cycle_length


def get_next_node(x: LinkedList) -> LinkedList:
    return x.next


if __name__ == '__main__':

    # +-------+----------+
    # |   x   |   f(x)   |
    # +-------+----------+
    # |   a   |    b     |
    # |   b   |    c     |
    # |   c   |    d     |
    # |   d   |    e     |
    # |   e   |    f     |
    # |   f   |    g     |
    # |   g   |    h     |
    # |   h   |    i     |
    # |   i   |    e     |
    # +-------+----------+

    # a -- b -- c -- d -- e -- f -- g -- h -- i
    #                     |                   |
    #                      -------------------

    a = LinkedList('a')
    b = LinkedList('b')
    c = LinkedList('c')
    d = LinkedList('d')
    e = LinkedList('e')
    f = LinkedList('f')
    g = LinkedList('g')
    h = LinkedList('h')
    i = LinkedList('i')

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h
    h.next = i
    i.next = e

    starting_position_of_cycle, length_of_cycle = floyd_cycle_detection(get_next_node, a)
    print(f"\nFLOYD CYCLE DETECTION"
          f"\nStart of Cycle: {starting_position_of_cycle.value}"
          f"\nLength: {length_of_cycle} nodes")

    starting_position_of_cycle, length_of_cycle = brent_cycle_detection(get_next_node, a)
    print(f"\nBRENT CYCLE DETECTION"
          f"\nStart of Cycle: {starting_position_of_cycle.value}"
          f"\nLength: {length_of_cycle} nodes")
