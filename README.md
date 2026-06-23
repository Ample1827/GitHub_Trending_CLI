# trending-repos 🔥

A command-line tool that fetches and displays trending GitHub repositories for a given time range.

---

## What It Does

`trending-repos` talks to the GitHub API, finds repositories created within your chosen time window, sorts them by star count, and prints a clean summary to your terminal.

```
$ trending-repos --duration month --limit 5

🔥 Trending GitHub Repositories (last month)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1  awesome-python  ⭐ 42,100
    Language: Python
    Description: A curated list of awesome Python frameworks and libraries
    URL: https://github.com/vinta/awesome-python

#2  shadcn-ui  ⭐ 38,500
    Language: TypeScript
    Description: Beautifully designed components built with Radix UI and Tailwind CSS
    URL: https://github.com/shadcn-ui/ui
trending_repos
... and so on
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Showing 5 of 5 results
```

---

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) — a fast Python package manager

---

## Installation

### 1. Install uv (if you haven't already)

On macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone this repository

```bash
git clone https://github.com/YOUR_USERNAME/trending-repos.git
cd trending-repos
```

### 3. Set up the project with uv

```bash
uv sync
```

This creates a virtual environment and installs all dependencies automatically.

### 4. Run the tool

```bash
uv run trending-repos
```

---

## Usage

```
uv run trending-repos [OPTIONS]
```

### Options

| Option | Description | Default |
|---|---|---|
| `--duration` | Time range: `day`, `week`, `month`, or `year` | `week` |
| `--limit` | How many repositories to show | `10` |

### Examples

Show the top 10 trending repos from the past week (default):
```bash
uv run trending-repos
```

Show the top 20 trending repos from the past month:
```bash
uv run trending-repos --duration month --limit 20
```

Show only the single hottest repo from today:
```bash
uv run trending-repos --duration day --limit 1
```

Show the top 50 repos from the past year:
```bash
uv run trending-repos --duration year --limit 50
```

---

## How It Works

1. You run the command and pass a `--duration` flag (e.g. `month`).
2. The tool calculates the start date for that window (e.g. 30 days ago).
3. It sends a request to the **GitHub Search API** — specifically the `/search/repositories` endpoint — filtering for repos created after that date.
4. GitHub returns a JSON response with repository data.
5. The tool sorts the results by star count (highest first).
6. It prints the top `--limit` repos in a readable format.

No GitHub account or API token required — this uses GitHub's public API.

---

## Project Structure

```
trending-repos/
├── README.md
├── pyproject.toml       ← project config & dependencies (managed by uv)
└── trending_repos/
    ├── __init__.py
    ├── main.py          ← entry point, CLI argument parsing
    ├── api.py           ← GitHub API requests & error handling
    └── display.py       ← formatting and printing results
```

---

## Error Handling

The tool handles the following gracefully:

- **Invalid `--duration`** — prints a helpful message listing valid options
- **Invalid `--limit`** (e.g. a negative number or text) — prints an error and exits
- **GitHub API rate limit hit** — tells you how long to wait
- **No internet connection** — shows a clear network error message
- **No results found** — lets you know instead of showing an empty list

---

## Dependencies

| Package | Purpose |
|---|---|
| `requests` | Making HTTP calls to the GitHub API |
| `click` | Building the CLI (arguments, help text, errors) |

---

## License

MIT