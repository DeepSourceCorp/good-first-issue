# Contributing to Good First Issue

Thanks for your interest in contributing! This guide will help you get started.

## Prerequisites

Before you begin, make sure you have the following installed:

- **Node.js** (v18 or later) - [Download](https://nodejs.org/)
- **Bun** – A fast JavaScript runtime and package manager. Install it with:
```bash
curl -fsSL https://bun.sh/install | bash
```

Or see https://bun.sh for other installation methods.

- **uv** – A fast Python package manager. Install it with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Arch Linux:

```bash
sudo pacman -S uv
```

On macOS:

```bash
brew install uv
```


  


## Project Structure

Good First Issue has two main components:

- **Front-end app** - Built with Nuxt.js, displays the curated list of repositories
- **Data population script** - Written in Python, fetches repository data from GitHub

## Setting Up Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/DeepSourceCorp/good-first-issue.git
   cd good-first-issue
   ```

2. **Set up Python environment**

   ```bash
   uv sync --all-extras
   ```

   This creates a virtual environment and installs all dependencies.

3. **Set up sample data files**

   The front-end app needs data files to display repositories. Copy the sample files to get started:

   ```bash
   cp data/generated.sample.json data/generated.json
   cp data/tags.sample.json data/tags.json
   ```

   These files contain:
   - `generated.json` - Repository metadata (stars, issues, languages, etc.)
   - `tags.json` - Language tags for filtering

4. **Install frontend dependencies**

   ```bash
   bun install
   ```

5. **Start the development server**

   ```bash
   bun dev
   ```

   The app will open at [http://localhost:3000](http://localhost:3000).

## Running Tests

To run the data sanity tests:

```bash
uv run python gfi/test_data.py
```

To run type checking:

```bash
uv run mypy gfi/*.py
```

Or run both with:

```bash
make test
```

## Formatting Code

```bash
make format
```

## Troubleshooting
| Issue | Solution |
| :--- | :--- |
| `bun` **not found in PATH** | Add Bun manually: `export PATH="$HOME/.bun/bin:$PATH"` then run `source ~/.zshrc`. |
| **Missing** `generated.json` **or** `tags.json` | Ensure you copied the `.sample.json` files in the `data/` directory. |
| **uv not found** | Install it using `sudo pacman -S uv` (Arch) or the official installer. |
| **Nuxt telemetry prompt or slow prepare** | This is normal; `bun install` triggers `nuxt prepare`. |
| **Python errors** | Use `uv run` to ensure the correct virtual environment is used. |


## Making Changes

1. Create a new branch for your changes
2. Make your changes and test them locally
3. Submit a pull request with a clear description of what you changed and why

## AI Usage Guidelines

If you use AI tools (Claude, Copilot, ChatGPT, etc.) when contributing:

- **Disclose AI usage** in your pull request description
- **Review and test** all AI-generated code before submitting
- **Ensure accuracy** - don't submit code you haven't verified works

Low-quality AI-generated PRs or issues will be closed without review.

_Inspired by [Ghostty's AI Policy](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md)._
