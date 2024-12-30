<template>

  <div class="banner-container ">
    <div class="banner-content">
      <h1 class="banner-title">
        <slot >Make your first open-source contribution</slot>
      </h1>
      <div class="banner-text text-ink-400">
        Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can easily fix. Start today!
      </div>
      <div class="pt-6">
        <nuxt-link to='/Get_Started'>
        <div class="bg-juniper hover:bg-light_juniper text-ink-400 uppercase rounded-md font-bold text-center px-1 py-3 flex flex-row items-center justify-center space-x-1 ">
          Get Started
        </div>
      </nuxt-link>
    </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const BANNER_ACTIVE_TIME = 2000
const bannerActive = ref(true)

onMounted(() => {
  setTimeout(() => {
    bannerActive.value = false
  }, BANNER_ACTIVE_TIME)
})
</script>

<style scoped>
/* Banner container styling */
.banner-container {
  display: flex;
  justify-content: center;
  align-items: center;
  /* background: linear-gradient(90deg, #1f1f1f, #2a2a2a); */
  padding: 2rem 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(51, 203, 154, 0.5);
  text-align: center;
  color: #e0e0e0; /* Light gray for text contrast */
}

/* Content layout */
.banner-content {
  max-width: 800px;
}

/* Title styling */
.banner-title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1rem;
  color: #ffffff; /* White for better readability */
}

/* Text styling */
.banner-text {
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  line-height: 1.6;
  color: #d3d3d3; /* Soft gray for supporting text */
}

/* Button styling */
.banner-button {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: bold;
  color: #1f1f1f; /* Dark text on light button */
  background-color: #ffffff; /* Light button for contrast */
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

</style>