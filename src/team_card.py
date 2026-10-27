import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/modengann/Data-sets/refs/heads/master/pokemon.csv"


def team_card(df: pd.DataFrame) -> pd.DataFrame:
    """Make a team card. Return a table with only the Name, Type 1 and Speed columns, in that order."""
    pass


def five_biggest(df: pd.DataFrame) -> pd.DataFrame:
    """Who are the 5 Pokémon with the most HP? Return a table of the top 5 by HP, most HP first."""
    pass


def third_fastest_electric(df: pd.DataFrame) -> str:
    """Who is the third-fastest Electric type? Return the Name of the Pokémon
    whose Type 1 is Electric and that has the third-highest Speed among Electric types."""
    pass


def main():
    df = pd.read_csv(DATA_URL)
    print("Team card:")
    print(team_card(df))
    print()
    print("Most HP:")
    print(five_biggest(df))
    print()
    print("Third-fastest Electric type:", third_fastest_electric(df))


if __name__ == "__main__":
    main()
