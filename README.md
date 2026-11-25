[![Make.fun bounty](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![Rank](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/firlifirrizqi/autocorrect-fail-makefun/rank.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![Reward](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/firlifirrizqi/autocorrect-fail-makefun/reward.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154)

# Funniest Autocorrect Fail

One original autocorrect-fail line, written for the [Make.fun bounty](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154).

## The line

> Dinner's ready, I made pastor with garlic bread, come home hungry!

The slip: "pasta" autocorrected to "pastor" — the intended word is guessable at once, the wrong word is surprising, and the invitation itself ("come home hungry") makes the mix-up land on first read.

## How it works

`main.py` (standard library only) writes the line — and nothing else — to `/output/entry.txt`. It asserts the text is a single line of 1–199 characters with exactly 11 words, then re-opens the written file and verifies its content matches the line exactly.

## Run

```sh
python3 main.py
```
