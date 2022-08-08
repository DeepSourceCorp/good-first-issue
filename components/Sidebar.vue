<template>
  <section
    class="masthead font-sans pt-6 border-r border-ink-200 px-6 text-vanilla-300 flex-none w-full md:max-w-sm"
  >
    <div>
      <h3 class="section-heading">About</h3>
      <p class="text-sm">
        Good First Issue curates easy pickings from popular open-source projects, and helps you make
        your first contribution to open-source.
      </p>
    </div>
    <div class="pt-6">
      <h3 class="section-heading">Browse by language</h3>
      <div>
        <nuxt-link
          v-for="tag in tags"
          :key="tag.slug"
          :to="'/language/' + tag.slug"
          :class="{
            'active-pill': $route.params.slug === tag.slug,
            'border-slate hover:text-juniper hover:border-juniper': $route.params.slug !== tag.slug
          }"
          class="group mx-1 border px-2 py-1 inline-block rounded-sm my-1 text-sm"
          >{{ tag.language }}
          <span
            :class="{
              'text-vanilla-400 group-hover:text-juniper': $route.params.slug !== tag.slug
            }"
            >&times; {{ tag.count }}</span
          ></nuxt-link
        >
      </div>
    </div>
    <div class="pt-6">
      <a
        class="block bg-juniper hover:bg-light_juniper text-ink-400 uppercase rounded-md font-bold text-center px-1 py-3"
        href="https://github.com/deepsourcelabs/good-first-issue#adding-a-new-project"
        target="_blank"
        rel="noopener noreferrer"
        >Add your project</a
      >
    </div>

    <div class="text-sm pt-6">
      <a
        class="flex flex-row justify-center items-center"
        target="_blank"
        rel="noopener noreferrer"
        href="https://deepsource.io?ref=gfi"
      >
        <img style="width: 14px" src="/social/heart.svg" alt="Heart" />
        <span class="ml-2"
          >A
          <span class="inline hover:underline text-juniper" title="Visit DeepSource website"
            >DeepSource</span
          >
          initative</span
        >
      </a>
    </div>
  </section>
</template>

<script>
import Tags from '~/data/tags.json'

export default {
  data: function () {
    return {
      tags: Tags
    }
  }
}
</script>

<style>
.section-heading {
  @apply text-sm font-bold uppercase tracking-wider mb-2 text-slate;
}
.active-pill {
  @apply text-juniper font-semibold border-juniper;
}

.active-pill > span {
  @apply text-juniper;
}
</style>
