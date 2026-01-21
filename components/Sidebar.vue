<template>
  <section class="masthead font-sans pt-6 border-r border-ink-200 px-6 text-vanilla-300 flex-none w-full md:max-w-sm">
    <div>
      <h3 class="section-heading">About</h3>
      <p class="text-sm">
        Good First Issue curates easy pickings from popular open-source projects, and helps you make your first
        contribution to open-source.
      </p>
    </div>

    <div class="pt-6">
      <h3 class="section-heading">Browse by language</h3>
      <div class="mb-4">
        <select
          v-model="selectedLang"
          class="w-full bg-ink-300 text-vanilla-100 px-3 py-2 rounded-sm text-sm"
          @change="onLanguageChange"
        >
          <option value="">-- Select a language --</option>
          <option value="__all__">Show all languages</option>
          <option v-for="tag in sortedTags" :key="tag.slug" :value="tag.slug">
            {{ tag.language }}
          </option>
        </select>

        <div class="pt-2">
          <div
            v-if="selectedTag && selectedLang !== '__all__'"
            class="group mx-1 border border-slate hover:text-juniper hover:border-juniper px-2 py-1 inline-block rounded-sm my-1 text-sm text-vanilla-100"
          >
            {{ selectedTag.language }}
            <span class="ml-1 text-vanilla-400 group-hover:text-juniper">&times; {{ selectedTag.count }}</span>
          </div>

          <div v-else-if="selectedLang === '__all__'">
            <div
              v-for="tag in sortedTags"
              :key="tag.slug"
              class="group mx-1 border border-slate hover:text-juniper hover:border-juniper px-2 py-1 inline-block rounded-sm my-1 text-sm text-vanilla-100"
            >
              {{ tag.language }}
              <span class="ml-1 text-vanilla-400 group-hover:text-juniper">&times; {{ tag.count }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="pt-6">
      <a
        class="bg-juniper hover:bg-light_juniper text-ink-400 uppercase rounded-md font-bold text-center px-1 py-3 flex flex-row items-center justify-center space-x-1"
        href="https://github.com/deepsourcelabs/good-first-issue#adding-a-new-project"
        target="_blank"
        rel="noopener noreferrer"
      >
        <PlusCircleIcon class="h-5 w-5 stroke-2" />
        <span>Add your project</span>
      </a>
    </div>

    <div class="text-sm pt-6">
      <a
        class="flex flex-row justify-center items-center"
        target="_blank"
        rel="noopener noreferrer"
        href="https://deepsource.com?ref=gfi"
      >
        <HeartIcon class="w-4 h-4 text-cherry" />
        <span class="ml-2">
          A <span class="inline hover:underline text-juniper" title="Visit DeepSource website">DeepSource</span> initiative
        </span>
      </a>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Tags from '~/data/tags.json'
import { PlusCircleIcon } from '@heroicons/vue/24/outline'
import { HeartIcon } from '@heroicons/vue/24/solid'

const sortedTags = [...Tags].sort((a, b) => a.language.localeCompare(b.language))

const route = useRoute()
const router = useRouter()

const selectedLang = ref(route.params.slug || '')

const selectedTag = computed(() =>
  Tags.find(tag => tag.slug === selectedLang.value)
)

function onLanguageChange() {
  if (selectedLang.value === '' || selectedLang.value === '__all__') {
    router.push('/')
  } else {
    router.push(`/language/${selectedLang.value}`)
  }
}
</script>

<style>
.section-heading {
  @apply text-sm font-bold uppercase tracking-wider mb-2 text-slate;
}
</style>
