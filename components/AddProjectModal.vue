<template>
  <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50" @click="closeModal">
    <div class="bg-ink-400 border border-ink-200 rounded-lg p-6 max-w-md w-full mx-4" @click.stop>
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-xl font-bold text-vanilla-100">Add Your Project</h2>
        <button @click="closeModal" class="text-vanilla-300 hover:text-vanilla-100">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
      
      <form @submit.prevent="submitForm" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-vanilla-300 mb-2">GitHub Repository URL</label>
          <input
            v-model="formData.repoUrl"
            type="url"
            placeholder="https://github.com/username/repository"
            class="w-full px-3 py-2 bg-ink-300 border border-ink-200 rounded-md text-vanilla-100 placeholder-vanilla-400 focus:outline-none focus:ring-2 focus:ring-juniper focus:border-transparent"
            required
          />
          <p v-if="errors.repoUrl" class="text-cherry text-sm mt-1">{{ errors.repoUrl }}</p>
        </div>
        
        <div>
          <label class="block text-sm font-medium text-vanilla-300 mb-2">Contact Email</label>
          <input
            v-model="formData.email"
            type="email"
            placeholder="your@email.com"
            class="w-full px-3 py-2 bg-ink-300 border border-ink-200 rounded-md text-vanilla-100 placeholder-vanilla-400 focus:outline-none focus:ring-2 focus:ring-juniper focus:border-transparent"
            required
          />
          <p v-if="errors.email" class="text-cherry text-sm mt-1">{{ errors.email }}</p>
        </div>
        
        <div class="flex justify-end space-x-3 mt-6">
          <button
            type="button"
            @click="closeModal"
            class="px-4 py-2 text-vanilla-300 border border-ink-200 rounded-md hover:bg-ink-300"
          >
            Cancel
          </button>
          <button
            type="submit"
            :disabled="isSubmitting"
            class="px-4 py-2 bg-juniper hover:bg-light_juniper text-ink-400 rounded-md font-semibold disabled:opacity-50"
          >
            {{ isSubmitting ? 'Submitting...' : 'Submit Request' }}
          </button>
        </div>
      </form>
      
      <div v-if="successMessage" class="mt-4 p-3 bg-juniper bg-opacity-20 border border-juniper rounded-md">
        <p class="text-juniper text-sm">{{ successMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['close'])

const formData = ref({
  repoUrl: '',
  email: ''
})

const errors = ref({})
const isSubmitting = ref(false)
const successMessage = ref('')

function closeModal() {
  emit('close')
  // Reset form
  formData.value = { repoUrl: '', email: '' }
  errors.value = {}
  successMessage.value = ''
}

function validateForm() {
  errors.value = {}
  
  if (!formData.value.repoUrl) {
    errors.value.repoUrl = 'Repository URL is required'
  } else if (!formData.value.repoUrl.includes('github.com')) {
    errors.value.repoUrl = 'Please provide a valid GitHub URL'
  }
  
  if (!formData.value.email) {
    errors.value.email = 'Email is required'
  }
  
  return Object.keys(errors.value).length === 0
}

async function submitForm() {
  if (!validateForm()) return
  
  isSubmitting.value = true
  
  // Simulate API call
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    successMessage.value = 'Thank you! Your project submission has been received. We\'ll review it and get back to you.'
    formData.value = { repoUrl: '', email: '' }
  } catch (error) {
    errors.value.general = 'Something went wrong. Please try again.'
  } finally {
    isSubmitting.value = false
  }
}
</script>