# Orbitmagic

The "orbitmagic" library helps magicians model mathematical orbits. It is designed for magicians who know Python and lists.

[Warning] Only defined shuffles have an orbit!

## *Version 1.1 release*

(only Windows version -- Mac version coming soon!)


*What's new?*
=============

We've changed the function names to more formal ones:

`mix -> shuffle`

`pack -> deck`

## Installation

To install the library, you can use pip:

```pip install orbitmagic```


## Exposed Functions

Here is the list of functions exposed by the library:

```is_deck(deck: list[int]) -> bool```

Verifies whether a list of integers represents a valid deck of cards.

Arguments:

- `deck`: a list of integers representing a deck of cards.

Returns:

- `True` if the deck is valid, `False` otherwise.

```is_init(deck: list[int]) -> bool```


Verifies whether a list of integers represents the initial deck.

Arguments:

- `deck`: a list of integers representing a deck of cards.

Returns:

- `True` if the deck is the initial deck, `False` otherwise.

```orbit(shuffle:list[int]) -> int```


Calculates the number of orbits of a shuffle from a deck of cards.

Arguments:

- `shuffle`: a list that represents a way of shuffling the cards.

Returns:

- an integer representing the number of orbits of the shuffle.

```shuffle(deck: list[int], shuffle_method: list[int]) -> list[int]```


Shuffles a deck of cards according to a given shuffling method.

Arguments:

- `deck`: a list of integers representing a deck of cards.
- `shuffle_method`: a list representing a way of shuffling the cards.

Returns:

- a list of integers representing the shuffled deck of cards.

```reverse(shuffle_method: list[int]) -> list[int]```


Reverses the shuffling of a deck of cards according to a given shuffling method.

Arguments:

- `shuffle_method`: a list that represents a way to shuffle the cards.

Returns:

- a list of integers representing a shuffling that is the reverse of the given shuffling.

```cycle(shuffle_method: list[int], k: int) -> list[int]```


Calculates the condition of the starting deck of cards shuffled k times by the given shuffling.
(Also equivalent to shuffling k times by the given shuffling.)

Arguments:

- `shuffle_method`: a list that represents a way to shuffle the cards.
- `k`: number of iterations (can be negative).

Returns:

- a list of integers representing the equivalent shuffling.

```rev_cycle(shuffle_method: list[int], k: int) -> list[int]```


Similar to the cycle function, but instead of using `shuffle_method`, it cycles using `reverse(shuffle_method)`.

Arguments:

- `shuffle_method`: a list that represents a way to shuffle the cards.
- `k`: number of iterations (can be negative).

Returns:

- a list of integers representing the equivalent shuffling.

```all_cases(shuffle_method: list[int]) -> list[list[int]]```


Calculates all iterations of the given shuffling until the deck returns to the starting deck.

Arguments:

- `shuffle_method`: a list that represents a way to shuffle the cards.

Returns:

- a list of lists, with each element (a list of integers) representing an iteration of the given shuffling.

```find_shuffle(deck0: list[int], deck1: list[int]) -> list[int]```

Computes a shuffle according to the conditions of the deck before and after the shuffle.

Arguments:
- `deck0:`a list of integers representing a deck of cards before a shuffle.
- `deck1:`a list of integers representing the deck of cards after the shuffle.

Returns:
- a list of integers representing the shuffle.

```deck_init(n: int) -> list[int]```

Creates the initial deck of n cards.

Arguments:
- `n:`an integer representing the total number of cards in the deck.

Returns:
- a list of integers representing the initial deck of cards.

```help()```

Helps users to view all functions

## Author

This library was created by
*JeongHan-Bae*.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE.txt) file for more details.

## Future Version (Preview)

We are going to add some shuffling methods as fonctions such as Faro and Monge.

Now, for using these shuffles, we offer you the python code bellow :

```
def faro_in(n: int):
    if n % 2:
        return None
    return list(i // 2 + (1 - i % 2) * n // 2 for i in range(2, n + 2))


def faro_out(n: int):
    if n % 2:
        return None
    return list(i // 2 + (i % 2) * n // 2 for i in range(2, n + 2))


def monge_in(n: int):
    if n % 2:
        return list(range(n, -1, -2)) + list(range(2, n + 1, 2))
    return list(range(n - 1, 0, -2)) + list(range(2, n + 1, 2))


def monge_out(n: int):
    if n % 2:
        return list(range(n - 1, 0, -2)) + list(range(1, n + 1, 2))
    return list(range(n, 0, -2)) + list(range(1, n + 1, 2))
```

### Contact Us
If you have any questions or feedback, feel free to [contact us](https://github.com/JeongHan-Bae).
