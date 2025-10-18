# DSA-With-Python

Short collection of Data Structures & Algorithms examples implemented in Python. Each folder groups problems by topic or difficulty and contains runnable example scripts.

## Contents

- `basic-Questions/` — small/basic practice problems (counts, palindrome, simple logic).
- `easy-Questions/` — easy-level problems and factor/frequency helpers.
- `Hashing-Basics/` — hashing examples and character-hashing utilities.
- `loops/` — loop practice scripts.
- `Recursion/` — recursion examples (head-tail recursion variations).

## Requirements

- Python 3.8+ (any recent 3.x should work)
- No external packages required — pure Python scripts.

## Quick start

1. Open the repository folder.
2. Run a script with Python, for example:

	python basic-Questions/palindrome.py

3. To run other examples, change the path to the script you want and run with `python`.

## Contributing

- Add new algorithm examples under an appropriate folder.
- Name files descriptively and keep functions small and focused.
- Add brief comments or docstrings explaining inputs/outputs.

## Notes

- This repo is intended for learning and quick reference. Feel free to reorganize or add tests and examples.

---
If you want, I can expand this README with a navigation table, run examples, or add a CONTRIBUTING guide.
<!---LeetCode Topics Start-->
# LeetCode Topics
## Math
|  |
| ------- |
| [0009-palindrome-number](https://github.com/aditya-niranjan/DSA-With-Python/tree/master/0009-palindrome-number) |
<!---LeetCode Topics End-->

## What I have done

- Implemented core practice problems grouped by topic: loops, basic problems, easy problems, hashing basics, recursion, sorting, and Fibonacci.
- Added small, focused scripts for common tasks:
	- Palindrome checks (`basic-Questions/palindrome.py`, `loops/PalindromeUSingloops.py`, `0009-palindrome-number/0009-palindrome-number.py`).
	- Counting and simple arithmetic helpers (`basic-Questions/count.py`, `basic-Questions/counting.py`).
	- Frequency and factor utilities (`easy-Questions/frequncey.py`, `easy-Questions/factors.py`, `easy-Questions/bestfactor.py`).
	- Hashing demonstrations (`Hashing-Basics/hashing.py`, `Hashing-Basics/optimalhashing.py`, `Hashing-Basics/dicationary.py`, character-hash examples).
	- Recursion examples covering head recursion, tail recursion, parameterized recursion, and small recursion problems (`RECURSION/**`).
	- Sorting implementations: Bubble, Insertion, Selection, and Merge (`SORTING-ALGORITHMS/**`).
	- Fibonacci example (`fibonacci/fib.py`).

- Files are written as standalone Python scripts — easy to run and adapt for learning.
- No external dependencies; intended for learners to read, run, and modify.

If you'd like, I can convert this into a table-of-contents with direct links and short descriptions for every file.

## Completed work (full summary)

This section lists folders and notable scripts implemented in the repository so far. Files are left unchanged — this is a documentation-only summary.

- Top-level helpers and runners:
	- `main.py`, `main2.py`, `LEANER-SEARCH.py` — workspace entry / experiment scripts.

- basic-Questions/
	- `palindrome.py`, `count.py`, `counting.py`, `Prime-Numbers.py`, `aram.py`, `aramnum.py`, `main.py` — simple practice problems and small utilities.

- easy-Questions/
	- `frequncey.py`, `factors.py`, `factorBetter.py`, `bestfactor.py`, `best-hash-freq.py` — frequency, factorization, and helper utilities.

- loops/
	- `PalindromeUSingloops.py`, `palindromeUsingWhile.py`, `main.py`, `main2.py`, `main3.py` — loop-based solutions and examples.

- Hashing-Basics/
	- `hashing.py`, `optimalhashing.py`, `dicationary.py` and `charecter/` examples (`Charecter-Hashing.py`, `charcterUsinghash-list.py`) — dictionary/hash-based patterns.

- ARRAYS-OR-LIST/
	- Many array problems: `TWO-SUM.py`, `TwoSum-Optimal.py`, `Second_largest_element.py`, rotate/rotate-by-k scripts, remove duplicates, move zeros, maximum subarray (optimal + naive), K rotations, check-sorted, helpers and a `main2.py`.

- SORTING-ALGORITHMS/
	- `BUBBLE-SORT/` (bubble, best-case), `INSERTION-SORT/` (Insertion-Sort.py), `SELECTION-SORT/` (Selection-Sorting.py, SElection-SortD.py), `MERGE-SROTING/` (Merge-sortings1way.py) — classic sorting implementations.

- RECURSION/
	- Head recursion examples (`RecursionTheory.py`, `RecursionTheory2.py`), tail recursion (`Recusrion1.py`, `Recursion2.py`), parameterized and functional recursion examples, recursion problems (`FACT.PY`, `ReverseArrayRecursion.py`), and recursion-with-parameters subfolders.

- fibonacci/
	- `fib.py` — Fibonacci example(s).

- Best-uniqueProblems/
	- Unique or combined problems like `disticnte.py`, `intersection_multiple_arrays.py.py`, `Merge-two-sorted-array.py`.

- QUESTIONS-SOLVING/
	- `merge-two-sorted-arr.py`, `MAX-CONSECUTIVE-ELEMNET.py` — problem-focused scripts.

- CHAT-GPT-PROVIDED-QUESTIONS/
	- `main2.py`, `main3.py` — copies/experiments with ChatGPT-provided prompts or examples.

- 0009-palindrome-number/
	- `0009-palindrome-number.py` and a small folder README (LeetCode problem example).


If you'd like a more structured README I can:
	- Add a clickable table-of-contents with direct file links.
	- Generate one-line descriptions for every file and insert them under each folder header.
	- Create a small `run_all_examples.py` that imports/executes sample functions (documented) without touching your existing scripts.

Tell me which of the above you'd like next and I will only modify `README.md` (or add a new documentation file) per your instruction.