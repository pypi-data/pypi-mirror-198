# Orbitmagic

The "orbitmagic" library helps magicians model mathematical orbits. It is designed for magicians who know Python and lists.
[Warning] Only defined mixes have an orbit!

## Installation

To install the library, you can use pip:

```pip install orbitmagic```


## Exposed Functions

Here is the list of functions exposed by the library:

```is_pack(pack: list[int]) -> bool```

Verifies whether a list of integers represents a valid deck of cards.

Arguments:

- `pack`: a list of integers representing a deck of cards.

Returns:

- `True` if the deck is valid, `False` otherwise.

```is_init(pack: list[int]) -> bool```


Verifies whether a list of integers represents the initial deck.

Arguments:

- `pack`: a list of integers representing a deck of cards.

Returns:

- `True` if the deck is the initial deck, `False` otherwise.

```orbit(mix:list[int]) -> int```


Calculates the number of orbits of a mix from a deck of cards.

Arguments:

- `mix`: a list that represents a way of shuffling the cards.

Returns:

- an integer representing the number of orbits of the mix.

```mix(pack: list[int], mix_method: list[int]) -> list[int]```


Shuffles a deck of cards according to a given shuffling method.

Arguments:

- `pack`: a list of integers representing a deck of cards.
- `mix_method`: a list representing a way of shuffling the cards.

Returns:

- a list of integers representing the shuffled deck of cards.

```reverse(mix_method: list[int]) -> list[int]```


Reverses the mixing of a deck of cards according to a given mixing method.

Arguments:

- `mix_method`: a list that represents a way to mix the cards.

Returns:

- a list of integers representing a mixing that is the reverse of the given mixing.

```cycle(mix_method: list[int], k: int) -> list[int]```


Calculates the condition of the starting deck of cards mixed k times by the given mixing.
(Also equivalent to mixing k times by the given mixing.)

Arguments:

- `mix_method`: a list that represents a way to mix the cards.
- `k`: number of iterations (can be negative).

Returns:

- a list of integers representing the equivalent mixing.

```rev_cycle(mix_method: list[int], k: int) -> list[int]```


Similar to the cycle function, but instead of using `mix_method`, it cycles using `reverse(mix_method)`.

Arguments:

- `mix_method`: a list that represents a way to mix the cards.
- `k`: number of iterations (can be negative).

Returns:

- a list of integers representing the equivalent mixing.

```all_cases(mix_method: list[int]) -> list[list[int]]```


Calculates all iterations of the given mixing until the deck returns to the starting deck.

Arguments:

- `mix_method`: a list that represents a way to mix the cards.

Returns:

- a list of lists, with each element (a list of integers) representing an iteration of the given mixing.

```find_mix(pack0: list[int], pack1: list[int]) -> list[int]```

Computes a mix according to the conditions of the deck before and after the mix.

Arguments:
- `pack0:`a list of integers representing a deck of cards before a mix.
- `pack1:`a list of integers representing the deck of cards after the mix.

Returns:
- a list of integers representing the mix.

```pack_init(n: int) -> list[int]```

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

### Contact Us
If you have any questions or feedback, feel free to [contact us](https://github.com/JeongHan-Bae).
