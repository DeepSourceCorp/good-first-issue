<template>
  <!-- Main container for the page content with padding and full width. -->
  <div class="p-4 w-full">
    <!-- Iterates through the filtered list of repositories and renders a RepoBox component for each repository. -->
    <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
// Importing the list of repositories from a dynamically generated JSON file.
// This file likely contains metadata and information about open-source repositories.
import Repositories from '~/data/generated.json'

// Importing tags metadata, which provides additional information about languages or categories.
import Tags from '~/data/tags.json'

// Accessing the current route parameters using the useRoute composable from Nuxt.js.
const route = useRoute()

// Filtering the list of repositories to include only those matching the current route's slug.
const repositories = Repositories.filter(repository => repository.slug === route.params.slug)

// Finding the specific tag that matches the current route's slug for additional metadata.
const tag = Tags.find(t => t.slug === route.params.slug)

// Setting the page's head metadata using Nuxt's useHead API.
// This includes the dynamic title and description based on the tag's language.
useHead({
  title: `${tag.language} | Good First Issue`,  // Dynamic title based on the tag's language.
  meta: [{
    name: 'description',  // Dynamic meta description for SEO purposes.
    content: `Curated list of issues in ${tag.language} from popular open-source projects that you can easily fix.`
  }]
})
</script>
