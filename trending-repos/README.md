# trending-repos 🔥

A command-line tool that fetches and displays trending GitHub repositories for a given time range — with an interactive menu, spinner animations, and a beautiful table output.

---

## What It Does

You run `uv run main.py`, pick a time range and limit using arrow keys, and the tool fetches the most starred repos created in that window from the GitHub API and displays them in a clean table.

```
? Choose duration: (Use arrow keys)
 » today
   week
   month
   year

? How many repos to show? 10
```

Then after fetching:

```
                    Trending GitHub Repos
┏━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ # ┃ Name          ┃ Stars     ┃ Language   ┃ Description          ┃ URL                          ┃
┡━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1 │ awesome-repo  │ 4,200 ⭐  │ Python     │ An awesome project   │ https://github.com/...       │
│ 2 │ cool-project  │ 3,800 ⭐  │ TypeScript │ Another great repo   │ https://github.com/...       │
└───┴───────────────┴───────────┴────────────┴──────────────────────┴──────────────────────────────┘

? What would you like to do?
 » Search again
   Exit
```

---

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) — a fast Python package manager

---

## Installation

### 1. Install uv (if you haven't already)

On macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows (PowerShell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone this repository

```bash
git clone https://github.com/Ample1827/trending-repos.git
cd trending-repos
```

### 3. Install dependencies

```bash
uv sync
```

This creates a virtual environment and installs all dependencies automatically.

### 4. Run the tool

```bash
uv run main.py
```

---

## Usage

Just run the tool and follow the interactive prompts:

```bash
uv run main.py
```

You'll be asked two questions:

**1. Choose a duration** (use arrow keys to select):
- `today` — repositories created today
- `week` — repositories created in the last 7 days
- `month` — repositories created in the last 30 days
- `year` — repositories created in the last 365 days

**2. How many repos to show** (type a number, default is 10)

After the results are displayed, you can choose to search again or exit.

---

## How It Works

1. You pick a duration and limit from the interactive menu
2. `main.py` calculates the start date for that window
3. It calls `api.py` which sends a request to the GitHub Search API
4. GitHub returns repos created after that date, sorted by stars
5. `display.py` renders the results in a rich table
6. You can search again or exit

No GitHub account or API token required — this uses GitHub's public API.

---

## Project Structure

```
trending-repos/
├── README.md
├── pyproject.toml       ← project config & dependencies (managed by uv)
├── uv.lock
├── main.py              ← entry point, interactive prompts, date calculation
├── api.py               ← GitHub API requests & error handling
└── display.py           ← table formatting and printing
```

---

## Error Handling

- **No internet connection** — shows a red error message and exits cleanly
- **GitHub API error** — shows the status code and exits cleanly
- **Request timeout** — shows a red error message and exits cleanly
- **No language/description** — shows "Unknown" or "No description" as fallback

---

## Dependencies

| Package | Purpose |
|---|---|
| `requests` | Making HTTP calls to the GitHub API |
| `click` | CLI entry point |
| `rich` | Beautiful table and spinner output |
| `questionary` | Interactive arrow key menus |
| `pyfiglet` | ASCII art banner |

---

## License

MIT