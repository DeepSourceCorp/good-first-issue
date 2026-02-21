<p align="center">
  <a href="https://goodfirstissue.dev" target="_blank">
    <img src="public/readme-logo.svg" alt="Good First Issue logo">
  </a>
</p>
<hr>

Welcome! 👋🏼

**Good First Issue** curates easy pickings from popular open-source projects, so developers who've never contributed to open source can get started quickly.

Open-source maintainers are always looking to get more people involved, but new developers often find it challenging to become a contributor. We believe that helping developers fix super-easy issues removes the barrier for future contributions. This is why **Good First Issue** exists.

## ✨ Getting Started

### Prerequisites

Make sure you have the following tools installed before setting up the project:

| Tool | Version | Installation |
|------|---------|-------------|
| **Node.js** | v18+ | [nodejs.org](https://nodejs.org/) |
| **Bun** | Latest | `curl -fsSL https://bun.sh/install \| bash` |
| **uv** | Latest | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

### Quick Setup

```bash
# 1. Clone the repository
git clone https://github.com/DeepSourceCorp/good-first-issue.git
cd good-first-issue

# 2. Set up the Python environment
uv sync --all-extras

# 3. Copy sample data files so the front end can render
cp data/generated.sample.json data/generated.json
cp data/tags.sample.json data/tags.json

# 4. Install front-end dependencies
bun install

# 5. Start the development server
bun dev
```

The app will be available at **[http://localhost:3000](http://localhost:3000)**.

### Useful Commands

| Command | Description |
|---------|-------------|
| `bun dev` | Start the Nuxt development server |
| `bun generate` | Generate a static production build |
| `make test` | Run data sanity tests and type checking |
| `make format` | Format Python and front-end code |
| `uv run python gfi/populate.py` | Re-generate repository data from GitHub |
| `uv run python gfi/test_data.py` | Run data sanity tests only |
| `uv run mypy gfi/*.py` | Run type checking only |

## 📂 Project Structure

```
good-first-issue/
├── pages/            # Nuxt.js pages (front end)
├── components/       # Vue components (Navbar, Sidebar, RepoBox, etc.)
├── composables/      # Shared reactive state
├── data/             # Repository data & configuration (TOML, JSON)
├── gfi/              # Python scripts for data population & testing
├── layouts/          # Nuxt layout templates
├── public/           # Static assets (images, icons, manifest)
├── Makefile          # Common build, test, and format commands
├── nuxt.config.ts    # Nuxt configuration
└── pyproject.toml    # Python project & dependency configuration
```

## ➕ Adding a New Project

You're welcome to add a new project to Good First Issue — we encourage all projects, old and new, big and small.

### How to Add Your Project

1. **Check the eligibility criteria** — make sure your repository meets the requirements listed below.
2. **Submit the form** — fill out the submission form with your repository details.
3. **Wait for review** — a maintainer will review your submission and add it to the site.

**[📋 Submit your repository via this form](https://docs.google.com/forms/d/e/1FAIpQLSfHSt8UHvACokWv8uwiImidTIhuSCAUXnvSGs-TULshdLl9Qw/viewform?usp=header)**

### Eligibility Criteria

To maintain the quality of projects listed on Good First Issue, please make sure your GitHub repository meets the following criteria:

| Requirement | Description |
|-------------|-------------|
| **Good First Issues** | At least 3 open issues with beginner-friendly labels (e.g., `good first issue`, `beginner`, `easy`, `help wanted`) |
| **Contributors** | At least 10 contributors |
| **README.md** | Detailed setup instructions |
| **CONTRIBUTING.md** | Guidelines for new contributors |
| **Active Maintenance** | Recent commits and activity |
| **License** | A valid open-source license |

Once your submission is reviewed and approved, it will appear on [goodfirstissue.dev](https://goodfirstissue.dev/).

## 🤝 Contributing

We'd love your help! Whether it's fixing a bug, improving documentation, or adding a feature — every contribution counts.

1. Fork the repository and create a new branch.
2. Make your changes and test them locally.
3. Submit a pull request with a clear description of what you changed and why.

For detailed setup instructions and contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
