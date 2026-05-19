<template>
  <div class="min-h-screen w-full px-6 py-8">

    <!-- Hero / About Section -->
    <section class="max-w-3xl mx-auto text-center mb-10">
      <h1 class="text-3xl font-bold mb-4">
        Good First Issue
      </h1>

      <p class="text-gray-600 leading-relaxed">
        Good First Issue helps you discover beginner-friendly tasks from popular open-source projects.
        It makes starting your open-source journey simple, guided, and less overwhelming.
      </p>

      <p class="text-gray-600 mt-3">
        Browse repositories by programming language and start contributing easily.
      </p>
    </section>

    <!-- Browse Section Header -->
    <section class="max-w-6xl mx-auto mb-6">
      <h2 class="text-xl font-semibold mb-2">
        Explore Repositories
      </h2>

      <p class="text-gray-500 text-sm">
        Find beginner-friendly issues and start contributing to open-source projects.
      </p>
    </section>

    <!-- Repositories List -->
    <section class="max-w-6xl mx-auto grid gap-4">
      <RepoBox
        v-for="repo in Repositories"
        :key="repo.id"
        :repo="repo"
      />
    </section>

  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'

useHead({
  title: 'Good First Issue - Start Your Open Source Journey',
  meta: [
    {
      name: 'description',
      content:
        'Discover beginner-friendly open-source issues and start contributing easily with Good First Issue.'
    }
  ]
})
</script>