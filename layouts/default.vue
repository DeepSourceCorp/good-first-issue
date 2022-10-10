<template>
  <div class="bg-ink-400 flex flex-col min-h-screen antialiased text-vanilla-300">
    <navbar :tag="tag"></navbar>
    <main class="flex flex-1">
      <section class="container max-w-6xl mx-auto flex flex-col md:flex-row">
        <sidebar></sidebar>
        <Nuxt />
      </section>
    </main>
  </div>
</template>

<script>
import Navbar from '~/components/Navbar.vue'
import Sidebar from '~/components/Sidebar.vue'
import { ExternalLinkIcon } from 'vue-feather-icons'

export default {
  components: {
    Navbar,
    Sidebar,
    ExternalLinkIcon
  },
  data: function () {
    return {
      tag: {}
    }
  }
}
</script>
