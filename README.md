<p align="center">
  <a href="https://goodfirstissue.dev" target="_blank">
    <img src="public/readme-logo.svg">
  </a>
</p>
<hr>

Welcome! 👋🏼

**Good First Issue** is an initiative to curate easy pickings from popular projects, so developers who've never contributed to open-source can get started quickly.

Open-source maintainers are always looking to get more people involved, but new developers generally think it's challenging to become a contributor. We believe getting developers to fix super-easy issues removes the barrier for future contributions. This is why Good First Issue exists.

## Adding a new project

You're welcome to add a new project in Good First Issue, and we encourage all projects &mdash; old and new, big and small.

Follow these simple steps:

- Our goal is to narrow down projects for new open-source contributors. To maintain the quality of projects in Good First Issue, please make sure your GitHub repository meets the following criteria:

  - It has at least three issues with the `good first issue` label. This label is already present on all repositories by default. If not, you can follow the steps [here](https://help.github.com/en/github/managing-your-work-on-github/applying-labels-to-issues-and-pull-requests).

  - It has at least 10 contributors.

  - It contains a README.md with detailed setup instructions for the project, and a CONTRIBUTING.md with guidelines for new contributors.

  - It is actively maintained.

- Add your repository's path (in lexicographic order) in [data/repositories.toml](data/repositories.toml).

- Create a new pull-request. Please add the link to the issues page of the repository in the PR description. Once the pull request is merged, the changes will be live on [goodfirstissue.dev](https://goodfirstissue.dev/).

## Setting up the project locally

Good First Issue has two components — the front-end app built with Nuxt.js and a data population script written in Python.

Follow the steps below to get the app running locally.

# prerequistes

-node.js
-python
-bun
-git

# Verify installations 
-node -v
-python3 --version
-bun -v
-git --version

# Install frontend dependencies
$ bun install

# Start the Nuxt.js development server
$ bun dev or bun dev --host

> Note: If you do not have Bun installed, install it from https://bun.sh/.
The project currently uses Bun for dependency management and development.

## Troubleshooting

- If the app fails to start, ensure the data files are created correctly:
  - data/generated.json
  - data/tags.json

## The frontend will not work without these files.

cp data/generated.sample.json data/generated.json
cp data/tags.sample.json data/tags.json

- Make sure no other service is running on port 3000.

- Run `bun install` again if dependencies fail.

