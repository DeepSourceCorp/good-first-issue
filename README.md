<p align="center">
  <a href="https://goodfirstissue.dev" target="_blank">
    <img src="public/readme-logo.svg">
  </a>
</p>
<hr>


# 🌟 Good First Issue — Beginner-Friendly Guide


## 👋 Welcome to Good First Issue!

**Good First Issue** helps new developers make their *first open-source contribution* by collecting beginner-friendly issues from popular GitHub projects.

Many developers want to contribute but feel open-source is too difficult.
This platform removes that barrier by highlighting issues that are easy, clear, and perfect for first-time contributors.

---

# 📌 Add Your Project to Good First Issue

We welcome all kinds of projects — new or old, small or large.
Before adding your repository, make sure it meets these requirements:

### ✅ Requirements for Adding a Project

* Your GitHub repository must have **at least 3 issues** with the label `good first issue`.
* The repository should have **at least 10 contributors**.
* A clear **README.md** explaining:

  * What the project does
  * How to set it up
* A **CONTRIBUTING.md** file with guidelines for new contributors.
* The project should be **actively maintained**.

### 📥 Steps to Submit Your Project

1. Add your repository (in alphabetical order) inside
   **`data/repositories.toml`**.
2. Open a **Pull Request**.
3. Include a link to your repository’s **issues page** in the PR description.

Once your PR is merged, your project will appear on
👉 [https://goodfirstissue.dev/](https://goodfirstissue.dev/)

---

# 🛠️ Setting Up the Project Locally (Beginner-Friendly)

The project has two main parts:

1. **Frontend Website** – built using Nuxt.js
2. **Data Generator Script** – written in Python

Follow these steps to run the website on your computer:

---

## 1️⃣ Clone the Repository

Make sure you have **Python 3** and **Node.js / Bun** installed.

```bash
git clone <repository-url>
cd good-first-issue
```

---

## 2️⃣ Prepare the Required Data Files

The app needs two data files to run.
Copy the sample files and rename them:

```bash
cp data/generated.sample.json data/generated.json
cp data/tags.sample.json data/tags.json
```

🔹 *This step is important — the app will not work without these files.*

---

## 3️⃣ Install Dependencies & Start the Development Server

```bash
bun install     # installs packages
bun dev         # starts the local server
```

Your browser will automatically open the site.

---



