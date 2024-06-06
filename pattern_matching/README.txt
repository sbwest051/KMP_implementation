
# README

## Overview
This repository contains two Python scripts, `dfa.py` and `kmp.py`, which are used for pattern matching and creating deterministic finite automata (DFA).

## dfa.py
This script reads a file and creates a deterministic finite automaton (DFA) using the Graphviz library. The DFA is saved to a file specified by the user. The script takes two command line arguments: the input file and the output file for the DFA.

Usage: python dfa.py <input_file> <output_file> (Or python3 depending on your system)

## Installation
To run these scripts, you need Python and the Graphviz library. You can install Graphviz with pip or brew if you already have brew downloaded:


## Input File Format
The input file for both scripts should contain one or more lines. Each line should contain a sequence of characters. For `kmp.py`, the first line is the sequence to search, and the second line is the pattern to find.

## Output
`dfa.py` outputs a Graphviz file representing the DFA. `kmp.py` prints the starting indices of all occurrences of the pattern in the sequence, or -1 if the pattern is not found.