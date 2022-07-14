# Mastermind

Mastermind is a code-breaking game for two players.

The game is played using:
- a _decoding board_, with a _shield_ at one end covering a row of 4 large holes, and usually 12 additional rows containing 4 large holes next to a set of 4 small holes;
- _code pegs_ of 6 different colors (yellow, orange, red, purple, green, black), with round heads, these will be placed in the large holes on the board;
- _key pegs_: some colored black, some white, which are flat-headed and smaller than the code pegs; they will be placed in the small holes on the board.

The two players decide in advance how many games they will play, which must be an even number.
One player becomes the _codemaker_, the other the _codebreaker_.
1. The codemaker **chooses a pattern** of four code pegs. Duplicates are allowed, so the player could even choose four code pegs of the same color. The chosen pattern is placed in the four holes covered by the shield, visible to the codemaker but not to the codebreaker.
2. The codebreaker **tries to guess the pattern**, in both order and color, within twelve turns. Each guess is made by placing a row of code pegs on the decoding board.
3. Once placed, the codemaker **provides feedback** by placing from zero to four key pegs in the small holes of the row with the guess. A colored or black key peg is placed for each code peg from the guess which is correct in both color and position (`HIT`). A white key peg indicates the existence of a correct color code peg placed in the wrong position (`CLOSE`).

If there are _duplicate colors_ in the guess, they cannot all be awarded a key peg unless they correspond to the same number of duplicate colors in the hidden code.

_For example, if the hidden code is red-red-blue-blue and the player guesses red-red-red-blue, the codemaker will award two colored key pegs for the two correct reds, nothing for the third red as there is not a third red in the code, and a colored key peg for the blue. No indication is given of the fact that the code also includes a second blue._

4. Once feedback is provided, another guess is made; **guesses and feedback continue to alternate** until either the codebreaker guesses correctly, or all rows of the decoding boards are full.

It is easier to play than to write up the rules...

### Instruction:

To start:
```
python Mastermind.py
```

To display your choices:
```
BOARD
```
