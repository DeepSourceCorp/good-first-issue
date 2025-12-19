<!-- views/About.vue -->
<template>
  <div class="about-page max-w-4xl mx-auto px-4 py-8">
    <header class="mb-12 text-center">
      <h1 class="text-4xl font-bold text-juniper mb-4">About Good First Issue</h1>
      <p class="text-xl text-vanilla-300 max-w-3xl mx-auto">
        Making your first open-source contribution easier than ever before
      </p>
    </header>

    <section class="mb-12">
      <h2 class="text-2xl font-semibold text-vanilla-200 mb-4">What is Good First Issue?</h2>
      <div class="prose prose-invert max-w-none">
        <p class="mb-4">
          Good First Issue is a curated list of issues from popular open-source projects that are perfect for new
          contributors. We help developers make their first open-source contribution by highlighting issues that are
          well-documented and suitable for beginners.
        </p>
        <p class="mb-4">
          Our mission is to make open-source more accessible to everyone by reducing the barriers to entry and helping
          developers build their confidence through meaningful contributions.
        </p>
      </div>
    </section>

    <section class="grid md:grid-cols-2 gap-8 mb-12">
      <div class="bg-ink-500 p-6 rounded-lg shadow-lg">
        <h3 class="text-xl font-semibold text-juniper mb-4">For New Contributors</h3>
        <ul class="space-y-3">
          <li class="flex items-start">
            <span class="text-juniper mr-2">✓</span>
            <span>Find beginner-friendly issues from top open-source projects</span>
          </li>
          <li class="flex items-start">
            <span class="text-juniper mr-2">✓</span>
            <span>Learn how to make your first pull request</span>
          </li>
          <li class="flex items-start">
            <span class="text-juniper mr-2">✓</span>
            <span>Gain real-world experience and build your portfolio</span>
          </li>
        </ul>
      </div>

      <div class="bg-ink-500 p-6 rounded-lg shadow-lg">
        <h3 class="text-xl font-semibold text-juniper mb-4">For Maintainers</h3>
        <ul class="space-y-3">
          <li class="flex items-start">
            <span class="text-juniper mr-2">✓</span>
            <span>Get help with your open-source projects</span>
          </li>
          <li class="flex items-start">
            <span class="text-juniper mr-2">✓</span>
            <span>Connect with new contributors</span>
          </li>
          <li class="flex items-start">
            <span class="text-juniper mr-2">✓</span>
            <span>Grow your community</span>
          </li>
        </ul>
      </div>
    </section>

    <section class="mb-12">
      <h2 class="text-2xl font-semibold text-vanilla-200 mb-4">How It Works</h2>
      <div class="grid md:grid-cols-3 gap-6">
        <div class="bg-ink-500 p-6 rounded-lg">
          <div class="text-juniper text-2xl font-bold mb-2">1</div>
          <h3 class="text-lg font-medium mb-2">Browse Projects</h3>
          <p class="text-vanilla-300">Find projects that interest you and match your skills</p>
        </div>
        <div class="bg-ink-500 p-6 rounded-lg">
          <div class="text-juniper text-2xl font-bold mb-2">2</div>
          <h3 class="text-lg font-medium mb-2">Pick an Issue</h3>
          <p class="text-vanilla-300">Choose a well-documented, beginner-friendly issue</p>
        </div>
        <div class="bg-ink-500 p-6 rounded-lg">
          <div class="text-juniper text-2xl font-bold mb-2">3</div>
          <h3 class="text-lg font-medium mb-2">Make a Contribution</h3>
          <p class="text-vanilla-300">Submit your first pull request and become an open-source contributor</p>
        </div>
      </div>
    </section>

    <section class="text-center">
      <h2 class="text-2xl font-semibold text-vanilla-200 mb-4">Ready to Get Started?</h2>
      <p class="mb-6 max-w-2xl mx-auto">
        Join thousands of developers who have made their first open-source contribution through Good First Issue.
      </p>
      <a
        href="/"
        class="inline-block bg-juniper hover:bg-juniper-dark text-ink-400 font-bold py-3 px-6 rounded-md transition-colors"
      >
        Browse Issues
      </a>
    </section>
  </div>
</template>

<script setup>
// This is the About page component that provides information about the Good First Issue project
</script>

<style scoped>
.about-page {
  min-height: calc(100vh - 200px); /* Adjust based on your header/footer height */
}

.prose {
  color: #cbd5e0; /* text-vanilla-300 equivalent */
}

.prose a {
  color: #f6c358; /* text-juniper equivalent */
  text-decoration: none;
  border-bottom: 1px solid #f6c358;
  transition: all 0.2s ease;
}

.prose a:hover {
  color: #e2b34a; /* A slightly darker juniper for hover */
  border-bottom-color: transparent;
}
</style>
