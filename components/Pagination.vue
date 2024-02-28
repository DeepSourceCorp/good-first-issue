<template>
  <div class="flex justify-center items-center mt-4">
    <button
      class="px-4 py-2 rounded text-ink-400 font-bold bg-juniper hover:bg-light_juniper"
      @click="goToPrevPage"
      :disabled="currentPage <= 1"
    >
      Previous
    </button>

    <span class="mx-4 font-bold">Page {{ currentPage }} of {{ totalPages }}</span>

    <button
      class="px-4 py-2 rounded text-ink-400 font-bold bg-juniper hover:bg-light_juniper"
      @click="goToNextPage"
      :disabled="currentPage >= totalPages"
    >
      Next
    </button>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  currentPage: Number,
  totalPages: Number
});

const emit = defineEmits(['update:currentPage']);

function goToPrevPage() {
  if (props.currentPage > 1) {
    emit('update:currentPage', props.currentPage - 1);
  }
}

function goToNextPage() {
  if (props.currentPage < props.totalPages) {
    emit('update:currentPage', props.currentPage + 1);
  }
}
</script>
