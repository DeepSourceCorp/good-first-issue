<!-- Marco Fernandez -->

<template>
  <div class="p-4 w-full">
    <!-- Search Bar -->
    <input
      type="text"
      v-model="searchQuery"
      placeholder="Search repositories..."
      class="search-bar"
    />

    <!-- Display Filtered Repositories -->
    <RepoBox
      v-for="repo in filteredRepositories"
      :key="repo.id"
      :repo="repo"
    />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'; // Import necessary functions from Vue
import Repositories from '~/data/generated.json'; // Import the list of repositories from a JSON file

const searchQuery = ref(''); // Stores user input for filtering repositories

// Computed property that filters repositories based on the search input
const filteredRepositories = computed(() => {
  return Repositories.filter(repo =>
    repo.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

// Sets metadata for better SEO and accessibility
useHead({
  title: 'Good First Issue: Make your first open-source contribution',
  meta: [
    {
      name: 'description',
      /* Copied directly from the README file */
      content: 'Good First Issue is an initiative to curate easy pickings from popular projects, so developers who\'ve never contributed to open-source can get started quickly.'
    }
  ]
});
</script>

<style scoped>
/* Styling for the search bar */
.search-bar {
  width: 100%;         /* Makes the search bar full width */
  padding: 8px;        /* Adds space inside the input box */
  margin-bottom: 10px; /* Adds space below the search bar */
  border: 1px solid #000; /* Sets border color to black */
  border-radius: 4px;  /* Rounds the corners slightly */
  font-size: 16px;     /* Makes text easier to read */
  color: #000;         /* Sets the font color to black */
}
</style>
