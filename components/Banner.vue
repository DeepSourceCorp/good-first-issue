<template>
  <header
    class="w-full py-4 px-6 border-b border-ink-200 transition-background duration-500"
    :class="[`${bannerActive ? 'bg-robin' : 'bg-ink-300'}`]"
  >
    <span class="flex items-center justify-center flex-wrap text-sm md:text-md font-medium">
      <span class="md:ml-2 mr-auto md:mr-0">
        <slot name="text"></slot>
      </span>
      <a
        v-if="$slots['cta']"
        :href="ctaLink"
        target="_blank"
        class="flex items-center md:ml-2 mr-auto md:mr-0 mt-2 md:mt-0"
      >
        <slot name="cta"></slot>
      </a>
    </span>
  </header>
</template>

<script>
const BANNER_ACTIVE_TIME = 2000

export default {
  props: {
    ctaLink: {
      type: String,
      default: ''
    }
  },
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
