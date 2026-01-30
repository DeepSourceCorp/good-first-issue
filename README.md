<p align="center">
  <a href="https://goodfirstissue.dev" target="_blank">
    <img src="public/readme-logo.svg">
  </a>
</p>
<hr>

Welcome! 👋🏼

**Good First Issue** is an initiative to curate easy pickings from popular projects, so developers who've never contributed to open-source can get started quickly.

Open-source maintainers are always looking to get more people involved, but new developers generally think it's challenging to become a contributor. We believe getting developers to fix super-easy issues removes the barrier for future contributions. This is why Good First Issue exists.


## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | [Nuxt.js 3](https://nuxt.com/) (Vue.js) |
| Styling | [Tailwind CSS](https://tailwindcss.com/) |
| Data Pipeline | Python 3.12 |
| JS Package Manager | [Bun](https://bun.sh/) |
| Python Package Manager | [uv](https://docs.astral.sh/uv/) |
| Hosting | [Vercel](https://vercel.com/) |
| Data Storage | [Vercel Blob](https://vercel.com/docs/storage/vercel-blob) |

## How It Works

Good First Issue consists of two main parts:

1. **Data Pipeline (Python)** — A script (`gfi/populate.py`) reads the curated repository list from `data/repositories.toml` (~800+ repos), fetches metadata and beginner-friendly issues via the GitHub API, and outputs JSON data files.
2. **Frontend (Nuxt.js)** — A static site generated from the JSON data, allowing users to browse repositories and filter by programming language.

A daily cron job refreshes the data automatically and triggers a redeployment.

## Quick Start

```bash
# Clone and enter the project
git clone https://github.com/DeepSourceCorp/good-first-issue.git
cd good-first-issue

# Set up Python environment
uv sync --all-extras

# Copy sample data for local development
cp data/generated.sample.json data/generated.json
cp data/tags.sample.json data/tags.json

# Install frontend dependencies and start dev server
bun install
bun dev
```

The app will be available at [http://localhost:3000](http://localhost:3000). See [CONTRIBUTING.md](CONTRIBUTING.md) for full setup details.

## Project Structure

```
├── components/        # Vue components (Navbar, Sidebar, RepoBox, etc.)
├── composables/       # Shared Vue state
├── data/              # Repository list (TOML) and generated JSON data
├── gfi/               # Python data pipeline (populate.py, tests)
├── layouts/           # Nuxt layout templates
├── pages/             # Nuxt pages (index, language filter)
├── public/            # Static assets (icons, images)
├── Makefile           # Build automation commands
├── nuxt.config.ts     # Nuxt configuration
└── pyproject.toml     # Python project configuration
```

## Available Commands

| Command | Description |
|---------|-------------|
| `bun dev` | Start the development server |
| `bun generate` | Generate the static site |
| `make generate` | Fetch fresh data from GitHub (requires `GH_ACCESS_TOKEN`) |
| `make test` | Run data sanity tests and type checking |
| `make format` | Format code with Ruff and Prettier |
| `make pre-build` | Set up Python environment |

## Adding a new project

You're welcome to add a new project to Good First Issue, and we encourage all projects &mdash; old and new, big and small.

**[Submit your repository via this form](https://docs.google.com/forms/d/e/1FAIpQLSfHSt8UHvACokWv8uwiImidTIhuSCAUXnvSGs-TULshdLl9Qw/viewform?usp=header)**

To maintain the quality of projects in Good First Issue, please make sure your GitHub repository meets the following criteria:

| Requirement | Description |
|-------------|-------------|
| Good First Issues | At least 3 open issues with beginner-friendly labels (`good first issue`, `beginner`, `easy`, `help wanted`, etc.) |
| Contributors | At least 10 contributors |
| README.md | Detailed setup instructions |
| CONTRIBUTING.md | Guidelines for new contributors |
| Active Maintenance | Recent commits and activity |
| License | Valid open source license |

Once your submission is reviewed and approved, it will be added to [goodfirstissue.dev](https://goodfirstissue.dev/).

## Contributing

Want to contribute? See [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions and guidelines.

## License

This project is licensed under the [MIT License](LICENSE).
