<template>
  <header
    class="w-full py-4 border-b
           bg-vanilla-100 dark:bg-ink-400
           border-vanilla-300 dark:border-ink-200"
  >
    <nav class="flex items-center justify-center flex-wrap">
      <NuxtLink to="/" class="flex items-center font-bold">
        <img
          src="~/assets/gfi-logo-white.svg"
          alt="Good First Issue"
          class="h-12 dark:block hidden"
        />
        <img
          src="~/assets/gfi-logo-dark.svg"
          alt="Good First Issue"
          class="h-12 block dark:hidden"
        />
      </NuxtLink>

      <span v-if="activeTag" class="text-2xl cursor-pointer ml-2">
        <span class="font-normal mr-1 text-slate dark:text-vanilla-300">/</span>
        <span class="font-semibold text-juniper">
          {{ activeTag.language }}
        </span>
      </span>
    </nav>
  </header>
</template>
