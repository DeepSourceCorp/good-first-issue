import { promises as fs } from 'fs'
import path from 'path'
import https from 'https'
import { pipeline } from 'stream/promises'

import { put, list } from '@vercel/blob'

const dirToSync = './data'
const filesToSync = ['generated.json', 'tags.json']

/**
 * Downloads a file from a given URL to a specified destination.
 *
 * @param {string} url
 * @param {string} dest
 */
async function downloadFile(url, dest) {
  await fs.mkdir(path.dirname(dest), { recursive: true })

  return new Promise((resolve, reject) => {
    https.get(url, async (response) => {
      if (response.statusCode !== 200) {
        response.resume()
        reject(
          new Error(`Failed to download file: status code ${response.statusCode}`)
        )
        return
      }

      try {
        const fileStream = await fs.open(dest, 'w')
        await pipeline(response, fileStream.createWriteStream())
        await fileStream.close()
        resolve()
      } catch (err) {
        reject(err)
      }
    }).on('error', reject)
  })
}

/**
 * Sync selected files from local to Vercel Blob
 */
async function syncFilesUp() {
  for (const fileName of filesToSync) {
    const filePath = path.resolve(dirToSync, fileName)

    try {
      const stat = await fs.stat(filePath)

      if (stat.isFile()) {
        const fileContent = await fs.readFile(filePath)
        await put(fileName, fileContent, {
          access: 'public',
          addRandomSuffix: false,
        })

        console.info(`Uploaded ${fileName}`)
      }
    } catch (err) {
      console.warn(`Skipping ${fileName}: ${err.message}`)
    }
  }
}

/**
 * Sync selected files from Vercel Blob to local
 */
async function syncFilesDown() {
  await fs.mkdir(dirToSync, { recursive: true })

  const response = await list()

  for (const blob of response.blobs) {
    if (filesToSync.includes(blob.pathname)) {
      const dest = path.resolve(dirToSync, blob.pathname)
      await downloadFile(blob.url, dest)
      console.info(`Downloaded ${blob.pathname}`)
    }
  }
}

async function main() {
  if (!process.env.BLOB_READ_WRITE_TOKEN) {
    console.error('BLOB_READ_WRITE_TOKEN not set in environment.')
    process.exit(1)
  }

  const direction = process.argv[2]

  try {
    switch (direction) {
      case 'up':
        await syncFilesUp()
        console.info('Sync up successful.')
        break

      case 'down':
        await syncFilesDown()
        console.info('Sync down successful.')
        break

      default:
        console.error('Must provide a valid sync direction: "up" or "down".')
        process.exit(1)
    }
  } catch (err) {
    console.error('Sync failed:', err)
    process.exit(1)
  }
}

await main()
