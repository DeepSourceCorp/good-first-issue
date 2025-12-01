<template>
  <form method="post" action="https://listmonk.deepsource.io/subscription/form" class="listmonk-form">
    <div class="flex flex-row space-x-2 w-full">
      <input
        class="bg-vanilla-200 dark:bg-ink-300 text-ink-300 dark:text-vanilla-100 flex flex-grow h-10 text-sm py-2 px-3 rounded-sm w-full outline-none transition-colors duration-200"
        type="text"
        name="email"
        placeholder="Enter your email"
        required
      />
      <div class="hidden">
        <input id="59f61" type="checkbox" name="l" checked value="59f61a48-5867-4861-bde0-59a9027420e3" />
        <label for="59f61">Good First Issue</label>
        <input id="4c2a7" type="checkbox" name="l" checked value="4c2a780e-f85b-4d28-8a60-9e2a43f0e0d4" />
        <label for="4c2a7">Community newsletter</label>
      </div>
      <!-- prettier-ignore -->
      <input class="bg-vanilla-200 dark:bg-ink-300 hover:bg-vanilla-300 dark:hover:bg-ink-200 text-ink-300 dark:text-vanilla-100 rounded-md font-semibold text-center h-10 px-4 py-2 text-sm space-x-2 leading-8 cursor-pointer transition-colors duration-200" type="submit" value="Subscribe" />
    </div>
  </form>
</template>
