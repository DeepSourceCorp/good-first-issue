<template>
    <nuxt-link
      :to="`/tags/${tag.slug}`"
      :class="[
        'group mx-1 px-2 py-1 inline-block rounded-sm text-sm relative',
        isActive ? 'active-pill' : 'border-slate hover:text-juniper hover:border-juniper'
      ]"
      :title="tag.tooltip"
    >
      <span>{{ tag.language }} &times; {{ tag.count }}</span>
      <span
        class="tooltip-text invisible absolute bottom-0 right-0 translate-x-full translate-y-full bg-black bg-opacity-100 text-white text-xs rounded px-2 py-1 group-hover:visible transition-opacity duration-200"
      >
        {{ tag.language }}
      </span>
    </nuxt-link>
  </template>
  
  <script setup>
  import { computed, toRefs } from 'vue'
  const props = defineProps({
    tag: Object,
    isActive: Boolean
  })
  </script>
  
  <style scoped>
  .tooltip-text {
    opacity: 0;
  }
  .group:hover .tooltip-text {
    opacity: 1;
  }
  </style>