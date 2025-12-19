<template>
  <div class="min-h-screen flex flex-col bg-ink-900 text-vanilla-200">
    <!-- Header -->
    <header class="bg-ink-800 shadow-md">
      <div class="container mx-auto px-4 py-4">
        <Navbar />
      </div>
    </header>

    <!-- Main Content -->
    <main class="flex-grow container mx-auto px-4 py-8">
      <div class="max-w-7xl mx-auto">
        <slot />
      </div>
    </main>

    <!-- Footer -->
    <footer class="bg-ink-800 py-8 mt-12">
      <div class="container mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between items-center">
          <div class="mb-4 md:mb-0">
            <p class="text-vanilla-300">© {{ new Date().getFullYear() }} Good First Issue</p>
          </div>
          <div class="flex space-x-6">
            <a href="/about" class="text-vanilla-300 hover:text-juniper transition-colors">About</a>
            <a href="/privacy" class="text-vanilla-300 hover:text-juniper transition-colors">Privacy Policy</a>
            <a href="/terms" class="text-vanilla-300 hover:text-juniper transition-colors">Terms of Service</a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import Navbar from '~/components/Navbar.vue'
</script>

<style scoped>
/* Add any specific styles for this layout here */
</style>
