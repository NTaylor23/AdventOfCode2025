import os
import requests


class AdventOfCodeError(Exception):
    pass


class AdventOfCodeSession(requests.Session):
    def __init__(self, day: int) -> None:
        super().__init__()
        self.day = day
        aoc_token = os.environ.get("AOC_TOKEN")
        if not aoc_token:
            raise AdventOfCodeError("Unable to get credentials, no token found.")

        github = os.environ.get("GITHUB_ACCT", "")
        email = os.environ.get("EMAIL", "")
        self.headers["Cookie"] = aoc_token
        self.headers["User-Agent"] = f"{github} (contact: {email})"
        self.puzzle_input = self.get_puzzle_input()

    def get_puzzle_input(self) -> str:
        path = f"./input/day{str(self.day).zfill(2)}.txt"
        try:
            with open(path, "r") as f:
                return f.read()
        except FileNotFoundError:
            response = self.get(f"https://adventofcode.com/2025/day/{self.day}/input")
            if response.status_code >= 400:
                raise AdventOfCodeError(
                    f"Failed to get input for day {self.day}, response code {response.status_code}"
                )
            with open(path, "w") as f:
                data = response.text
                f.write(data)
                return data
        raise AdventOfCodeError(
            f"Failed to read day {self.day} file or fetch it from Advent Of Code."
        )
