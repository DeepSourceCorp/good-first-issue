import fs from 'fs/promises'
import path from 'path'
import https from 'https'
import { pipeline } from 'stream/promises'
import { createWriteStream } from 'fs'
import { put, list } from '@vercel/blob'
import dotenv from 'dotenv'

dotenv.config() // Load .env

const dirToSync = './data'
const filesToSync = ['generated.json', 'tags.json']

// Validate required env variable
if (!process.env.BLOB_READ_WRITE_TOKEN) {
  console.error('❌ BLOB_READ_WRITE_TOKEN not set in .env or env variables.')
  process.exit(1)
}

/**
 * Download a file from a given URL and save it locally
 */
async function downloadFile(url, destPath) {
  const fileStream = createWriteStream(destPath)

  return new Promise((resolve, reject) => {
    https.get(url, (response) => {
      if (response.statusCode !== 200) {
        reject(new Error(`Failed download: status code ${response.statusCode}`))
        return
      }

      pipeline(response, fileStream)
        .then(resolve)
        .catch((err) => {
          fs.unlink(destPath)
          reject(err)
        })
    }).on('error', reject)
  })
}

/**
 * Upload local files to Vercel Blob Storage
 */
async function syncFilesUp() {
  console.info('🔼 Starting sync up...')

  await Promise.all(
    filesToSync.map(async (fileName) => {
      const filePath = path.join(dirToSync, fileName)
      try {
        const content = await fs.readFile(filePath)
        await put(fileName, content, { access: 'public', addRandomSuffix: false })
        console.log(`✅ Uploaded: ${fileName}`)
      } catch (err) {
        console.error(`❌ Failed to upload ${fileName}:`, err.message)
      }
    })
  )
}

/**
 * Download files from Vercel Blob to local directory
 */
async function syncFilesDown() {
  console.info('🔽 Starting sync down...')

  try {
    const response = await list()

    await Promise.all(
      response.blobs.map(async (blob) => {
        const destPath = path.join(dirToSync, blob.pathname)
        try {
          await downloadFile(blob.url, destPath)
          console.log(`✅ Downloaded: ${blob.pathname}`)
        } catch (err) {
          console.error(`❌ Failed to download ${blob.pathname}:`, err.message)
        }
      })
    )
  } catch (err) {
    console.error('❌ Failed to fetch blob list:', err.message)
  }
}

// Entrypoint
const command = process.argv[2]

switch (command) {
  case 'up':
    await syncFilesUp()
    break
  case 'down':
    await syncFilesDown()
    break
  default:
    console.error('❗ Please specify "up" or "down" as argument.')
    process.exit(1)
}
