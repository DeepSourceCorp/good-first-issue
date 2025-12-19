<template>
  <div class="app-container">
    <header class="bg-ink-400 py-4 shadow-md">
      <div class="container mx-auto px-4 flex justify-between items-center">
        <h1 class="text-2xl font-bold text-vanilla-300">
          <NuxtLink to="/" class="hover:text-juniper transition-colors"> Good First Issue </NuxtLink>
        </h1>
        <nav class="flex items-center space-x-6">
          <NuxtLink
            to="/"
            class="relative px-2 py-2 text-vanilla-300 hover:text-juniper transition-colors"
            :class="{ 'text-juniper font-medium': $route.path === '/' }"
          >
            Home
            <span v-if="$route.path === '/'">
              <span class="absolute bottom-0 left-0 w-full h-0.5 bg-juniper transition-all duration-300"></span>
            </span>
          </NuxtLink>
          <NuxtLink
            to="/about"
            class="relative px-2 py-2 text-vanilla-300 hover:text-juniper transition-colors"
            :class="{ 'text-juniper font-medium': $route.path === '/about' }"
          >
            About
            <span v-if="$route.path === '/about'">
              <span class="absolute bottom-0 left-0 w-full h-0.5 bg-juniper transition-all duration-300"></span>
            </span>
          </NuxtLink>
          <a
            href="https://github.com/deepsourcelabs/good-first-issue"
            target="_blank"
            rel="noopener noreferrer"
            class="flex items-center px-2 py-2 text-vanilla-300 hover:text-juniper transition-colors"
          >
            GitHub
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-4 w-4 ml-1 transition-transform"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
              />
            </svg>
          </a>
          <a
            href="https://deepsource.com"
            target="_blank"
            rel="noopener noreferrer"
            class="flex items-center px-2 py-2 text-vanilla-300 hover:text-juniper transition-colors"
          >
            DeepSource
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-4 w-4 ml-1 transition-transform"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
              />
              fill="none" viewBox="0 0 24 24" stroke="currentColor" >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
              />
            </svg>
          </a>
        </nav>

        <router-view />
      </div>
    </header>

    <main class="flex-grow container mx-auto px-4 py-6">
      <slot></slot>
    </main>

    <footer class="bg-ink-400 py-6 border-t border-ink-300">
      <div class="container mx-auto px-4 text-center text-vanilla-400 text-sm">
        <p>
          Made with ❤️ by the
          <a href="https://deepsource.com" target="_blank" rel="noopener" class="text-juniper hover:underline"
            >DeepSource</a
          >
          team
        </p>
        <p class="mt-2">
          <a
            href="https://github.com/deepsourcelabs/good-first-issue"
            target="_blank"
            rel="noopener"
            class="text-vanilla-300 hover:text-juniper"
          >
            Contribute on GitHub
          </a>
        </p>
      </div>
    </footer>
  </div>
</template>

<script setup>
// This component serves as a layout wrapper for the application
// It includes the header, main content area, and footer
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Navigation link hover effect */
.router-link-active {
  color: #f6c358; /* text-juniper */
  font-weight: 500;
}

/* External link icon animation */
a:hover svg {
  transform: translate(2px, -2px);
}

/* Smooth scrolling for anchor links */
html {
  scroll-behavior: smooth;
}
</style>
