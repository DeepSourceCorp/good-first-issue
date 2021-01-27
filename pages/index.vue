<template>
  <div class="p-4 w-full">
    <repo-box v-for="repo in repos" :key="repo.id" :repo="repo"></repo-box>
  </div>
</template>

<script>
import RepoBox from '~/components/RepoBox.vue'
import Repositories from '~/data/generated.json'

export default {
  components: {
    RepoBox
  },
  data: function () {
    return {
      repos: Repositories
    }
  }
}
</script>
