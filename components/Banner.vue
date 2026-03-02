<template>
  <header
    class="w-full py-4 px-6 border-b border-ink-200 transition-background duration-1000"
    :class="{ 'bg-robin': bannerActive, 'bg-ink-300': !bannerActive }"
  >
    <span class="flex items-center justify-center flex-wrap text-sm font-medium">
      <span class="md:flex items-center">
        <slot></slot>
      </span>
    </span>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const BANNER_ACTIVE_TIME = 2000;
const bannerActive = ref(true);
let timeoutId;

onMounted(() => {
  timeoutId = setTimeout(() => {
    bannerActive.value = false;
  }, BANNER_ACTIVE_TIME);
});

onUnmounted(() => {
  clearTimeout(timeoutId);
});
</script>

