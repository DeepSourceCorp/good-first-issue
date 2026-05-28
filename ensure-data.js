import fs from 'fs'
import path from 'path'

const files = [
  ['data/generated.sample.json', 'data/generated.json'],
  ['data/tags.sample.json', 'data/tags.json']
]

for (const [source, destination] of files) {
  const sourcePath = path.resolve(source)
  const destinationPath = path.resolve(destination)

  if (fs.existsSync(destinationPath)) {
    continue
  }

  if (!fs.existsSync(sourcePath)) {
    throw new Error(`Missing sample data file: ${source}`)
  }

  fs.copyFileSync(sourcePath, destinationPath)
  console.info(`Created ${destination} from ${source}`)
}
