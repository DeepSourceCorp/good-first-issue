<template>
  <main class="text-white bg-gray-900 min-h-screen px-6 lg:px-20">
    <!-- Welcome Section -->
    <div class="text-center py-12 bg-light_juniper rounded-md shadow-md">
      <h1 class="text-4xl font-extrabold leading-tight">Welcome! 👋🏼</h1>
      <p class="text-xl mt-6 max-w-3xl mx-auto leading-relaxed">
        <strong class="text-black">"Good First Issue"</strong> curates easy pickings from popular projects so developers who've never contributed to open-source can get started quickly.
      </p>
      <p class="text-xl mt-4 max-w-3xl mx-auto leading-relaxed">
        Open-source maintainers are always looking to involve new people, but many think it's too challenging to contribute. We believe starting with easy issues removes barriers to future contributions.
      </p>
    </div>

    <!-- Adding a New Project -->
    <section class="mt-12">
      <h2 class="text-3xl font-bold text-light_juniper text-center mb-8">Adding a New Project</h2>
      <p class="text-lg leading-relaxed mb-6">
        You're welcome to add a new project in Good First Issue, and we encourage all projects &mdash; old and new, big and small.
      </p>
      <p class="text-lg leading-relaxed mb-6">Follow these steps:</p>

      <ul class="space-y-8 text-lg">
        <li class="flex items-start space-x-6">
          <span class="bg-light_juniper text-black w-8 h-8 rounded-full flex items-center justify-center font-bold">1</span>
          <p>
            Your repository must meet these criteria:
            <ul class="mt-2 ml-8 list-disc space-y-2">
              <li>
                It has at least three issues labeled <code class="bg-gray-800 text-white px-1 py-0.5 rounded">good first issue</code>. Learn how to add the label <a href="https://help.github.com/en/github/managing-your-work-on-github/applying-labels-to-issues-and-pull-requests" class="text-blue-400 underline" target="_blank">here</a>.
              </li>
              <li>It has at least 10 contributors.</li>
              <li>
                It contains a <code class="bg-gray-800 text-white px-1 py-0.5 rounded">README.md</code> with setup instructions and a <code class="bg-gray-800 text-white px-1 py-0.5 rounded">CONTRIBUTING.md</code> with contributor guidelines.
              </li>
              <li>It is actively maintained.</li>
            </ul>
          </p>
        </li>
        <li class="flex items-start space-x-6">
          <span class="bg-light_juniper text-black w-8 h-8 rounded-full flex items-center justify-center font-bold">2</span>
          <p>
            Add your repository path in <code class="bg-gray-800 text-white px-1 py-0.5 rounded">data/repositories.toml</code> (maintain lexicographic order).
          </p>
        </li>
        <li class="flex items-start space-x-6">
          <span class="bg-light_juniper text-black w-8 h-8 rounded-full flex items-center justify-center font-bold">3</span>
          <p>
            Create a pull request with a link to the repository's issues page in the PR description. Once merged, your project will appear on <a href="https://goodfirstissue.dev" class="text-blue-400 underline" target="_blank">goodfirstissue.dev</a>.
          </p>
        </li>
      </ul>
    </section>

    <!-- Setting Up the Project Locally -->
    <section class="mt-16">
      <h2 class="text-3xl font-bold text-light_juniper text-center mb-8">Setting up the Project Locally</h2>
      <p class="text-lg leading-relaxed mb-6">
        Good First Issue includes a Nuxt.js front-end and a Python data script. Follow these steps to run the app locally:
      </p>

      <ol class="list-decimal list-inside space-y-8 text-lg">
        <li>
          Clone the project locally. Ensure Python 3 and a recent Node.js version are installed.
        </li>
        <li>
          Create copies of sample data files and rename them for local use. This step is essential for the front-end to work:
          <div class="codes bg-gray-800 text-white text-sm rounded-md p-4 mt-2 font-mono">
            <p>$ cp data/generated.sample.json data/generated.json</p>
            <p>$ cp data/tags.sample.json data/tags.json</p>
          </div>
        </li>
        <li>
          Build the app and start the development server:
          <div class="codes bg-gray-800 text-white text-sm rounded-md p-4 mt-2 font-mono">
            <p>$ bun install # install dependencies</p>
            <p>$ bun dev # start the server</p>
          </div>
        </li>
      </ol>
      <p class="text-lg mt-8 leading-relaxed">The app will now open in your browser.</p>
    </section>

    <!-- Go Back Button -->
    <div class="flex justify-center mt-12">
      <button class="bg-light_juniper hover:bg-juniper text-black font-bold rounded-md px-6 py-3 shadow-md transition duration-200">
        <nuxt-link to="/" class="uppercase">Go Back</nuxt-link>
      </button>
    </div>

    <!-- Footer -->
    <footer class="text-center py-6 mt-16 border-t border-gray-700">
      <p class="text-sm text-gray-400">&copy; 2024 Good First Issue. All rights reserved.</p>
    </footer>
  </main>
</template>

<script>
definePageMeta({
  layout: 'details',
});
</script>

<style scoped>
.codes {
  box-shadow: 0 4px 8px rgba(51, 203, 154, 0.5);
  width: fit-content;
}

ul, ol {
  padding-left: 1.5rem;
}

li {
  line-height: 1.8;
}

button {
  transition: transform 0.2s;
}
button:hover {
  transform: scale(1.05);
}
</style>
