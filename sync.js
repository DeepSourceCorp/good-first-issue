import fs from 'fs'
import path from 'path'
import https from 'https'

import { put, list } from '@vercel/blob'

const dirToSync = './data'
const filesToSync = ['generated.json', 'tags.json']

/**
 * Downloads a file from a given url to a specified destination.
 *
 * @param {string} url - The URL of the file to download.
 * @param {string} dest - The destination where the file should be saved.
 * @return {Promise} A Promise that resolves when the file has been downloaded.
 */
function downloadFile(url, dest) {
  return new Promise((resolve, reject) => {
    // Check if the file already exists
    const fileExists = fs.existsSync(dest)

    const file = fs.createWriteStream(dest, { flags: 'w' }) // 'w' flag for write mode

    https
      .get(url, (response) => {
        if (response.statusCode !== 200) {
          reject(new Error(`failed to download file: status code ${response.statusCode}`))
          return
        }

        response.pipe(file)

        if (fileExists) {
          console.log(`file ${dest} already exists. overwriting.`)
        }
      })
      .on('error', (err) => {
        reject(err)
      })

    file.on('finish', () => {
      resolve()
    })

    file.on('error', (err) => {
      fs.unlink(dest) // delete the file on error
      reject(err)
    })
  })
}

/**
 * Sync files from local to Vercel Blob
 */
async function syncFilesUp() {
  for (const fileName of filesToSync) {
    const filePath = path.resolve(path.join(dirToSync, fileName))
    const stat = await fs.statSync(filePath)

    if (stat.isFile()) {
      const fileContent = await fs.readFileSync(filePath)
      await put(fileName, fileContent, { access: 'public', addRandomSuffix: false })
    }
  }
}

/**
 * Sync files from Vercel Blob to local
 */
async function syncFilesDown() {
  const response = await list()
  for (const blob of response.blobs) {
    await downloadFile(blob.url, path.resolve(path.join(dirToSync, blob.pathname)))
  }
}

if (!("BLOB_READ_WRITE_TOKEN" in process.env)) {
  console.error('`BLOB_READ_WRITE_TOKEN` not set in env. exiting.')
  process.exit(1)  // skicq: JS-0263
}

switch (process.argv[2]) {
  case 'up':
    await syncFilesUp()
    console.info('syncing up successful.')
    break
  case 'down':
    await syncFilesDown()
    console.info('syncing down successful.')
    break
  default:
    console.error('must provide a valid sync direction. exiting.')
}
