import fs from 'fs'
import path from 'path'
import https from 'https'

import { put, list } from '@vercel/blob'

const dirToSync = './data'
const filesToSync = ['generated.json', 'tags.json']

function ensureDirExists(filePath) {
  const dir = path.dirname(filePath)
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true })
  }
}

function downloadFile(url, dest) {
  return new Promise((resolve, reject) => {
    ensureDirExists(dest)
    const tempDest = `${dest}.tmp`
    const file = fs.createWriteStream(tempDest)

    https.get(url, (response) => {
      if (response.statusCode !== 200) {
        file.close()
        fs.existsSync(tempDest) && fs.unlinkSync(tempDest)
        return reject(new Error(`failed to download file: status code ${response.statusCode}`))
      }

      response.pipe(file)

      file.on('finish', () => {
        file.close()
        try {
          // replace atomically
          if (fs.existsSync(dest)) fs.unlinkSync(dest)
          fs.renameSync(tempDest, dest)
          resolve()
        } catch (err) {
          fs.existsSync(tempDest) && fs.unlinkSync(tempDest)
          reject(err)
        }
      })
    }).on('error', (err) => {
      file.close()
      fs.existsSync(tempDest) && fs.unlinkSync(tempDest)
      reject(err)
    })
  })
}

async function syncFilesUp() {
  for (const fileName of filesToSync) {
    const filePath = path.resolve(path.join(dirToSync, fileName))
    try {
      const stat = await fs.promises.stat(filePath)
      if (stat.isFile()) {
        const fileContent = await fs.promises.readFile(filePath)
        await put(fileName, fileContent, { access: 'public', addRandomSuffix: false })
      }
    } catch (err) {
      // skip missing files but log for visibility
      console.warn(`Skipping upload for ${fileName}: ${err.message}`)
    }
  }
}

async function syncFilesDown() {
  const response = await list()
  for (const blob of response.blobs) {
    const dest = path.resolve(path.join(dirToSync, blob.pathname))
    try {
      await downloadFile(blob.url, dest)
    } catch (err) {
      console.error(`Failed to download ${blob.pathname}: ${err.message}`)
    }
  }
}

if (!process.env.BLOB_READ_WRITE_TOKEN) {
  console.error('`BLOB_READ_WRITE_TOKEN` not set in env. exiting.')
  process.exit(1)
}

const cmd = process.argv[2]
;(async () => {
  try {
    switch (cmd) {
      case 'up':
        await syncFilesUp()
        console.info('syncing up successful.')
        break
      case 'down':
        await syncFilesDown()
        console.info('syncing down successful.')
        break
      default:
        console.error('must provide a valid sync direction (up|down). exiting.')
        process.exit(1)
    }
  } catch (err) {
    console.error('sync failed:', err)
    process.exit(1)
  }
})()
