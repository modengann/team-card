import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

try:
    import pandas as pd
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "pandas is not installed for the Python running these tests:\n"
        f"    {sys.executable}\n"
        "Select the conda/Anaconda interpreter (Cmd/Ctrl+Shift+P → Python: Select Interpreter), "
        "trash the terminal and open a new one. If you have the extension "
        "'Python Test Explorer for Visual Studio Code', uninstall it and run tests "
        "from the 'Python Tests' tree."
    ) from None

from src.team_card import team_card, five_biggest, third_fastest_electric

REAL = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "pokemon.csv")

MINI = pd.DataFrame({
    "Name":   ["Zap", "Puff", "Boulder", "Spark", "Bolt", "Mossy", "Volt", "Tide"],
    "Type 1": ["Electric", "Normal", "Rock", "Electric", "Electric", "Grass", "Electric", "Water"],
    "HP":     [40, 150, 120, 50, 60, 90, 45, 100],
    "Speed":  [90, 20, 30, 110, 70, 50, 100, 60],
}, index=[10, 11, 12, 13, 14, 15, 16, 17])

NOT_A_TABLE = "should return a DataFrame (a table)"
CARD_COLUMNS = "columns should be exactly Name, Type 1, Speed — in that order"
MOST_HP = "should be the 5 with the MOST HP, biggest first"
THIRD = "third fastest means third in a fastest-first ranking — positions start at 0"


class TestTeamCard(unittest.TestCase):
    def test_real_pokedex(self):
        result = team_card(REAL.copy())
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        self.assertEqual(list(result.columns), ["Name", "Type 1", "Speed"], msg=CARD_COLUMNS)
        self.assertEqual(len(result), 800, msg="should keep every Pokémon (800 rows)")

    def test_small_table(self):
        result = team_card(MINI.copy())
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        self.assertEqual(list(result.columns), ["Name", "Type 1", "Speed"], msg=CARD_COLUMNS)
        self.assertEqual(len(result), 8, msg="should keep every Pokémon (8 rows)")


class TestFiveBiggest(unittest.TestCase):
    def test_real_pokedex(self):
        result = five_biggest(REAL.copy())
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        self.assertEqual(len(result), 5, msg="should have exactly 5 rows")
        self.assertEqual(list(result["Name"]),
                         ["Blissey", "Chansey", "Wobbuffet", "Wailord", "Alomomola"],
                         msg=MOST_HP)

    def test_small_table(self):
        result = five_biggest(MINI.copy())
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        self.assertEqual(len(result), 5, msg="should have exactly 5 rows")
        self.assertEqual(list(result["Name"]),
                         ["Puff", "Boulder", "Tide", "Mossy", "Bolt"],
                         msg=MOST_HP)


class TestThirdFastestElectric(unittest.TestCase):
    def check(self, df, expected):
        try:
            result = third_fastest_electric(df)
        except KeyError as error:
            result = "KeyError: " + str(error)
        self.assertEqual(result, expected, msg=THIRD)

    def test_real_pokedex(self):
        self.check(REAL.copy(), "Jolteon")

    def test_small_table(self):
        self.check(MINI.copy(), "Zap")


if __name__ == "__main__":
    unittest.main()
