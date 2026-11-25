<template>
  <form
    method="post"
    :action="actionUrl"
    aria-label="Newsletter subscription"
    class="listmonk-form"
  >
    <div class="flex flex-row gap-2 w-full">
      <label :for="inputId" class="sr-only">Email address</label>
      <input
        :id="inputId"
        v-model.trim="email"
        class="bg-ink-300 text-vanilla-100 placeholder-vanilla-400 flex-grow h-10 text-sm py-2 px-3 rounded-sm w-full border border-ink-200/60 focus:border-juniper focus:outline-none focus:ring-2 focus:ring-juniper/30 transition-colors"
        type="email"
        name="email"
        autocomplete="email"
        placeholder="Enter your email"
        required
      />

      <div class="hidden">
        <template v-for="list in lists" :key="list.id">
          <input
            :id="`${inputId}-${list.id}`"
            type="checkbox"
            name="l"
            :checked="list.checked ?? true"
            :value="list.id"
          />
          <label :for="`${inputId}-${list.id}`">{{ list.label }}</label>
        </template>
      </div>

      <button
        type="submit"
        class="bg-ink-300 hover:bg-ink-200 active:scale-[0.99] text-vanilla-100 rounded-md font-semibold text-center h-10 px-4 py-2 text-sm shrink-0 cursor-pointer transition-all focus:outline-none focus:ring-2 focus:ring-juniper/60"
      >
        {{ submitLabel }}
      </button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { ref, useId } from 'vue'

export interface SubscriptionList {
  id: string
  label: string
  checked?: boolean
}

interface Props {
  actionUrl?: string
  submitLabel?: string
  lists?: SubscriptionList[]
}

const DEFAULT_LISTS: SubscriptionList[] = [
  {
    id: '59f61a48-5867-4861-bde0-59a9027420e3',
    label: 'Good First Issue',
    checked: true
  },
  {
    id: '4c2a780e-f85b-4d28-8a60-9e2a43f0e0d4',
    label: 'Community newsletter',
    checked: true
  }
]

withDefaults(defineProps<Props>(), {
  actionUrl: 'https://listmonk.deepsource.io/subscription/form',
  submitLabel: 'Subscribe',
  lists: () => DEFAULT_LISTS
})

const inputId = useId()
const email = ref('')
</script>