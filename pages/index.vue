<template>
  <!-- Main container for the page content with padding and full width. -->
  <div class="p-4 w-full">
    <!-- Iterates through the list of repositories and renders a RepoBox component for each. -->
    <RepoBox v-for="repo in Repositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
// Importing the list of repositories from a generated JSON file.
// This file is dynamically created, likely containing data for open-source projects.
import Repositories from '~/data/generated.json'

// Sets the metadata for the page using Nuxt's useHead API.
// This helps with SEO and sets the page title and description.
useHead({
  title: 'Good First Issue: Make your first open-source contribution',  // The title displayed in the browser tab.
  meta: [
    {
      name: 'description',  // Description meta tag for SEO purposes.
      content: 'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can easily fix. Start today!'
    }
  ]
})
</script>