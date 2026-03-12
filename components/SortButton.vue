<template>
  <button
    type="button"
    @click="$emit('toggle')"
    class="px-4 py-2 text-xs font-mono uppercase tracking-wider rounded border transition-all duration-200 mb-4 mr-2"
    :class="active 
      ? 'bg-juniper text-ink-400 border-juniper' 
      : 'bg-ink-300 text-vanilla-300 border-ink-200 hover:border-juniper'"
  >
    <slot />
  </button>
</template>

<script setup>
defineProps({
  active: Boolean
})
defineEmits(['toggle'])
</script>