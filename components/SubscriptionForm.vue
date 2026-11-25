<template>
  <form
    method="post"
    action="https://listmonk.deepsource.io/subscription/form"
    class="listmonk-form"
  >
    <div class="flex flex-row gap-2 w-full">
      <input
        class="bg-ink-300 text-vanilla-100 flex-grow h-10 text-sm py-2 px-3 rounded-sm w-full focus:outline-none focus:ring-2 focus:ring-juniper/60"
        type="email"
        name="email"
        autocomplete="email"
        placeholder="Enter your email"
        required
      />

      <div class="hidden">
        <input
          id="59f61"
          type="checkbox"
          name="l"
          checked
          value="59f61a48-5867-4861-bde0-59a9027420e3"
        />
        <label for="59f61">Good First Issue</label>
        <input
          id="4c2a7"
          type="checkbox"
          name="l"
          checked
          value="4c2a780e-f85b-4d28-8a60-9e2a43f0e0d4"
        />
        <label for="4c2a7">Community newsletter</label>
      </div>

      <button
        type="submit"
        class="bg-ink-300 hover:bg-ink-200 text-vanilla-100 rounded-md font-semibold text-center h-10 px-4 py-2 text-sm shrink-0 cursor-pointer transition-colors focus:outline-none focus:ring-2 focus:ring-juniper/60"
      >
        Subscribe
      </button>
    </div>
  </form>
</template>
