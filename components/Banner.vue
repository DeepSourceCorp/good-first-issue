<template>
  <header
    class="w-full py-4 px-6 border-b border-ink-200 transition-background duration-1000"
    :class="[`${bannerActive ? 'bg-robin' : 'bg-ink-300'}`]"
  >
    <span class="flex items-center justify-center flex-wrap text-sm font-medium">
      <span class="md:flex items-center">
        <slot></slot>
      </span>
    </span>
  </header>
</template>

<script>
const BANNER_ACTIVE_TIME = 2000

export default {
  data() {
    return {
      bannerActive: true
    }
  },
  mounted() {
    setTimeout(() => {
      this.bannerActive = false
    }, BANNER_ACTIVE_TIME)
  }
}
</script>
