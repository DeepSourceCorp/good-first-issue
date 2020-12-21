<template>
  <div class="bg-ink-400 flex flex-col min-h-screen antialiased text-vanilla-300">
    <navbar :tag="tag"></navbar>
    <main class="flex flex-1">
      <section class="max-w-6xl mx-auto flex flex-col md:flex-row">
        <sidebar></sidebar>
        <Nuxt />
      </section>
    </main>
  </div>
</template>

<script>
import Navbar from '~/components/Navbar.vue'
import Sidebar from '~/components/Sidebar.vue'

export default {
  data: function () {
    return {
      tag: {}
    }
  },
  components: {
    Navbar,
    Sidebar
  }
}
</script>
