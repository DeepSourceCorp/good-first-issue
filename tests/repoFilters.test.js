import assert from 'node:assert/strict'
import test from 'node:test'

import { filterAndSortRepositories } from '../utils/repoFilters.js'

const repositories = [
  { id: '1', slug: 'python', stars: 500, last_modified: '2026-05-01T00:00:00Z' },
  { id: '2', slug: 'python', stars: 500, last_modified: '2026-05-10T00:00:00Z' },
  { id: '3', slug: 'python', stars: 100, last_modified: '2026-04-20T00:00:00Z' },
  { id: '4', slug: 'python', stars: 50, last_modified: '2025-12-01T00:00:00Z' },
  { id: '5', slug: 'javascript', stars: 1000, last_modified: '2026-05-15T00:00:00Z' }
]

test('filters by language slug and sorts by stars then last_modified', () => {
  const result = filterAndSortRepositories(repositories, { slug: 'python' })
  assert.deepEqual(result.map(repo => repo.id), ['2', '1', '3', '4'])
})

test('applies minimum stars filter', () => {
  const result = filterAndSortRepositories(repositories, { slug: 'python', minStars: 200 })
  assert.deepEqual(result.map(repo => repo.id), ['2', '1'])
})

test('applies recent activity filter with fixed now date', () => {
  const result = filterAndSortRepositories(repositories, {
    slug: 'python',
    activityMonths: 3,
    now: new Date('2026-05-16T00:00:00Z')
  })
  assert.deepEqual(result.map(repo => repo.id), ['2', '1', '3'])
})

test('combines minimum stars and recent activity filters', () => {
  const result = filterAndSortRepositories(repositories, {
    slug: 'python',
    minStars: 200,
    activityMonths: 1,
    now: new Date('2026-05-16T00:00:00Z')
  })
  assert.deepEqual(result.map(repo => repo.id), ['2', '1'])
})
