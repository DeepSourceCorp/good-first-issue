<template>
  <div>
    <div class="pt-6">
      <h3 class="section-heading">Sort By</h3>
      <div>
        <button
          v-for="sortOption in sortOptions"
          :key="sortOption.id"
          @click="handleActiveSortOptionToggle(sortOption)"
          :class="{
            'active-pill': activeSortOption.id === sortOption.id,
            'border-slate hover:text-juniper hover:border-juniper':
              activeSortOption.id !== sortOption.id
          }"
          class="group mx-1 border px-2 py-1 inline-block rounded-sm my-1 text-sm"
        >
          {{ sortOption.name }}
          <span
            :class="{
              'text-vanilla-400 group-hover:text-juniper': activeSortOption.id !== sortOption.id
            }"
          ></span>
        </button>
      </div>
    </div>
    <div v-if="activeSortOption.id" class="pt-6">
      <h3 class="section-heading">Order By</h3>
      <div>
        <button
          v-for="orderByOption in activeSortOption.orderByOptions"
          :key="orderByOption.id"
          @click="handleOrderByToggle(orderByOption.isOrderByDesc)"
          :class="{
            'active-pill': isOrderByDesc === orderByOption.isOrderByDesc,
            'border-slate hover:text-juniper hover:border-juniper':
              isOrderByDesc !== orderByOption.isOrderByDesc
          }"
          class="group mx-1 border px-2 py-1 inline-block rounded-sm my-1 text-sm"
        >
          {{ orderByOption.name }}
          <span
            :class="{
              'text-vanilla-400 group-hover:text-juniper':
                isOrderByDesc !== orderByOption.isOrderByDesc
            }"
          ></span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import sortOptions from '~/data/sortOptions.json'
export default {
  data() {
    return {
      sortOptions: sortOptions
    }
  },
  computed: {
    ...mapState(['activeSortOption', 'isOrderByDesc'])
  },
  methods: {
    ...mapMutations(['handleActiveSortOptionToggle', 'handleOrderByToggle'])
  }
}
</script>

<style></style>
