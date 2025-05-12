<p align="center">
  <a href="https://goodfirstissue.dev" target="_blank">
    <img src="public/readme-logo.svg">
  </a>
</p>
<hr>

# Good First Issue

Welcome! 👋🏼

**Good First Issue** is an initiative to curate easy pickings from popular projects, enabling developers who've never contributed to open-source to get started quickly.

Open-source maintainers are always looking to get more people involved, but new developers often find contributing intimidating. We believe that fixing super-easy issues clears that hurdle—helping you make your first PR in minutes.

---

## 🛠️ Adding a New Project

You're welcome to add a new project to Good First Issue, and we encourage all projects—old and new, big and small.

To maintain the quality of projects in Good First Issue, please ensure your GitHub repository meets the following criteria:

1. At least three issues labeled **good first issue**.
2. A minimum of 10 contributors.
3. A `README.md` with detailed setup instructions and a `CONTRIBUTING.md` with guidelines for new contributors.
4. Active maintenance (recent commits, prompt issue responses).

To add your project:

- Add your repository's path (in lexicographic order) to `data/repositories.toml`.
- Create a new pull request and link your repo’s issues page in the description.

Once the pull request is merged, your project will appear on [goodfirstissue.dev](https://goodfirstissue.dev/).

---

## 🚀 Quick Start
To contribute new features and changes to the website, you would want to run the app locally.
Follow these steps to set up the project locally:

1. **Clone the repository**:
Clone the project locally. Make sure you have Python 3 and a recent version of Node.js installed on your computer.
   ```bash
   git clone https://github.com/DeepSourceCorp/good-first-issue.git
   cd good-first-issue
   ```

2. **Install Bun** (a fast JavaScript runtime and package manager):

   ```bash
   curl -fsSL https://bun.sh/install | bash
   ```

3. **Install dependencies**:

   ```bash
   bun install
   ```

4. **Prepare sample data files**:
Make a copy of the sample data files for your local app to use and rename them to the filename that the app expects.
   **This step is important, as the front-end app won't work without these data files.**
   ```bash
   cp data/generated.sample.json data/generated.json
   cp data/tags.sample.json data/tags.json
   ```

   These JSON files serve as bootstrapped data for the front-end:

   - **`data/generated.json`**: Contains an array of repository objects with properties like `name`, `url`, `stars`, `open_issues_count`, and `last_updated`. This data populates the repository listings on the site.

   - **`data/tags.json`**: Contains an array of tag objects (e.g., `{ "name": "JavaScript", "count": 120 }`) used to filter and categorize issues by language or topic.

5. **Start the development server**:

   ```bash
   bun dev
   ```

   The front-end (built with Nuxt 3) will launch at [http://localhost:3000](http://localhost:3000).

   The app should open in your browser.

---

## 🔧 Project Structure

Good First Issue consists of:

- **Front-end**: A Nuxt 3 application with Unhead-powered `<head>` meta management for enhanced SEO.
- **Data script**: A Python tool to regenerate `data/` JSON files from live GitHub issues.

---

## 🔍 SEO Enhancements

To improve the discoverability of the website, consider adding meta tags in your Nuxt configuration. For example, in `nuxt.config.ts`:

```ts
export default defineNuxtConfig({
  app: {
    head: {
      title: "Good First Issue",
      meta: [
        {
          name: "description",
          content: "A curated list of beginner-friendly open-source issues.",
        },
        {
          name: "keywords",
          content:
            "good first issue, open source, first contribution, beginner",
        },
      ],
    },
  },
});
```

Nuxt's Unhead engine will merge these into your HTML `<head>` for improved SEO visibility.

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](https://opensource.guide/) for guidelines on how to get started.

---
