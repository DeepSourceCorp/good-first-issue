<template>
  <header class="w-full py-4 border-b bg-ink-400 border-ink-200">
    <nav class="flex items-center justify-between px-4 lg:px-8">
      <NuxtLink to="/" class="flex items-center text-gray-700 font-bold">
        <img src="~/assets/gfi-logo-white.svg" alt="Good First Issue" class="h-12" />
      </NuxtLink>
      <span v-if="activeTag" class="text-2xl cursor-pointer">
        <span class="font-normal mx-1 text-slate">/</span>
        <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
      </span>
    </nav>
  </header>
</template>

<script setup>
import { computed } from 'vue';
import Tags from '~/data/tags.json';

const route = useRoute();
const activeTag = computed(() => Tags.find(tag => tag.slug === route.params.slug));
</script>

<style>
.section-heading {
  @apply text-sm font-bold uppercase tracking-wider mb-2 text-slate;
}
</style>
