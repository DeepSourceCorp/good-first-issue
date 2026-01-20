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

You're welcome to add a new project to Good First Issue, and we encourage all projects &mdash; old and new, big and small.

**[Submit your repository via this form](https://docs.google.com/forms/d/e/1FAIpQLSfHSt8UHvACokWv8uwiImidTIhuSCAUXnvSGs-TULshdLl9Qw/viewform?usp=header)**

To maintain the quality of projects in Good First Issue, please make sure your GitHub repository meets the following criteria:

| Requirement | Description |
|-------------|-------------|
| Good First Issues | At least 3 open issues with the `good first issue` label |
| Contributors | At least 10 contributors |
| README.md | Detailed setup instructions |
| CONTRIBUTING.md | Guidelines for new contributors |
| Active Maintenance | Recent commits and activity |
| License | Valid open source license |

Once your submission is reviewed and approved, it will be added to [goodfirstissue.dev](https://goodfirstissue.dev/).

## Setting up the project locally

Good First Issue has two components — the front-end app built with Nuxt.js and a data population script written in Python.

To contribute new features and changes to the website, you would want to run the app locally. Please follow these steps:

1. Clone the project locally. Make sure you have Python 3 and a recent version of Node.js installed on your computer.

2. Make a copy of the sample data files for your local app to use and rename them to the filename that the app expects. **This step is important, as the front-end app won't work without these data files.**

```bash
$ cp data/generated.sample.json data/generated.json
$ cp data/tags.sample.json data/tags.json
```

3. Build the front-end app and start the development server.

```bash
$ bun install # install the dependencies
$ bun dev # start the development server
```

The app should open in your browser.
