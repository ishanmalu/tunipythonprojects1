"""
COMP.CS.100 Scoring the Dancing Games
Creator: Ishan Malu
Student id number: 154138420
"""

song_result = {
    "Boogie Nights": 91.4,
    "Dance Fever": 78.2,
    "Step Master": 86.6,
    "Groove Town": 79.9,
    "Beat Drop": 83.0,
}

def calculate_average(results: dict) -> float:
    """Return the average of all percentage values in the given dict."""
    return sum(results.values()) / len(results)


# Example usage (for testing):
if __name__ == "__main__":
    print(calculate_average(song_result))
