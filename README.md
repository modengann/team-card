# Team Card

Answer three questions about the Pokédex, one function each.

## The questions

All three functions are in `src/team_card.py`.

1. **Make a team card.** `team_card(df)` returns a table with only the Name, Type 1 and Speed columns, in that order.
2. **Who are the 5 Pokémon with the most HP?** `five_biggest(df)` returns a table of the top 5 by HP, most HP first.
3. **Who is the third-fastest Electric type?** `third_fastest_electric(df)` returns the Name of the Pokémon whose Type 1 is Electric and that has the third-highest Speed among Electric types.

Questions 1 and 2 return a table (a DataFrame). Question 3 returns a name.

Every function must work on any Pokédex table with these columns; the tests also use a small practice table.

## How to run

- See your findings: `python src/team_card.py`
- Run the tests: `python -m unittest discover` (or use the "Python Tests" tree in the Testing panel)

## If tests won't run

- **"No module named pandas"**: select the conda/Anaconda interpreter (Cmd/Ctrl+Shift+P → Python: Select Interpreter), then trash the terminal and open a new one.
- If "Python Test Explorer for Visual Studio Code" is installed, uninstall it; it ignores your interpreter choice.
- Open the assignment folder itself (File → Open Folder), not a folder above it.
- Windows: if conda won't activate in the terminal, run `conda init powershell` once in Anaconda Prompt and restart VS Code.
