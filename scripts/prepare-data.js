import fs from 'fs'
import path from 'path'

const root = path.resolve(new URL(import.meta.url).pathname, '..', '..')
const dataDir = path.join(root, 'data')

function copyIfMissing(src, dest) {
  if (fs.existsSync(dest)) return false
  if (!fs.existsSync(src)) return false
  fs.mkdirSync(path.dirname(dest), { recursive: true })
  fs.copyFileSync(src, dest)
  return true
}

const ops = [
  { src: path.join(dataDir, 'generated.sample.json'), dest: path.join(dataDir, 'generated.json') },
  { src: path.join(dataDir, 'tags.sample.json'), dest: path.join(dataDir, 'tags.json') },
]

let created = 0
for (const op of ops) {
  if (copyIfMissing(op.src, op.dest)) {
    console.log(`Created ${path.relative(root, op.dest)}`)
    created++
  }
}

if (created === 0) console.log('No data files needed creating')
