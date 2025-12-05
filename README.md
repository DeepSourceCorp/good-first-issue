<p align="center">
  <a href="https://goodfirstissue.dev" target="_blank">
    <img src="public/readme-logo.svg" alt="Good First Issue logo">
  </a>
</p>

<hr>

# Good First Issue

Welcome! 👋🏼

**Good First Issue** is an initiative to curate “easy pickings” from popular open-source projects, so developers who have never contributed before can get started quickly.

Open-source maintainers are always looking to get more people involved, but new developers often think it's challenging to become a contributor. We believe that helping developers fix super-easy issues removes the barrier for future contributions.

This is why **Good First Issue** exists. 💜

---

## 🚀 Adding a New Project

You're welcome to add a new project to Good First Issue, and we encourage all kinds of projects — old and new, big and small.

Please follow these steps:

### 1. Check that your repository meets the criteria

Our goal is to narrow down projects for new open-source contributors. To maintain the quality of projects shown on Good First Issue, make sure your GitHub repository satisfies **all** of the following:

- ✅ It has **at least three issues** with the `good first issue` label.  
  This label exists on all repositories by default. If you don’t see it, you can follow the steps in the [GitHub docs](https://help.github.com/en/github/managing-your-work-on-github/applying-labels-to-issues-and-pull-requests).

- ✅ It has **at least 10 contributors**.

- ✅ It contains:
  - A `README.md` with **clear, detailed setup instructions** for the project.
  - A `CONTRIBUTING.md` with **guidelines for new contributors**.

- ✅ It is **actively maintained** (for example, there have been recent commits or issues handled in the last few months).

### 2. Add your repository to the list

Once your repository meets the criteria:

1. Open the file [`data/repositories.toml`](data/repositories.toml).
2. Add your repository’s path **in lexicographic (alphabetical) order**.
3. Save the file.

If you’re not familiar with TOML: it’s a simple configuration file format. You can learn more at [https://toml.io](https://toml.io), but for most use cases, copying an existing entry and adjusting it will be enough.

### 3. Open a Pull Request

1. Commit your changes to `data/repositories.toml`.
2. Create a new pull request to this repository.
3. In the PR description, **include a link to the issues page** of your repository (e.g. `https://github.com/owner/repo/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22`).

Once your pull request is reviewed and merged, your project will appear on [goodfirstissue.dev](https://goodfirstissue.dev/). 🎉

---

## 🛠️ Setting Up the Project Locally

Good First Issue has two components:

1. A **front-end app** built with Nuxt.js.
2. A **data population script** written in Python.

If you want to contribute new features or changes to the website, you’ll likely want to run the app locally.

### 1. Prerequisites

Make sure you have the following installed on your computer:

- **Python 3**
- A recent version of **Node.js**
- **Bun**, the JavaScript runtime and package manager used by this project

You can download Node.js from the official website, and check your version with:

```bash
node -v
