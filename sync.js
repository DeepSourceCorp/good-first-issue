import fs from 'fs';
import path from 'path';
import https from 'https';
import { put, list } from '@vercel/blob';

const dirToSync = './data';
const filesToSync = ['generated.json', 'tags.json'];

/**
 * Downloads a file from a given URL to a specified destination with retries.
 * @param {string} url - The URL of the file to download.
 * @param {string} dest - The destination where the file should be saved.
 * @param {number} retries - Number of retry attempts.
 * @return {Promise} Resolves when the file is downloaded successfully.
 */
async function downloadFile(url, dest, retries = 3) {
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      await new Promise((resolve, reject) => {
        const file = fs.createWriteStream(dest, { flags: 'w' });
        https
          .get(url, (response) => {
            if (response.statusCode !== 200) {
              reject(new Error(`Failed to download file: status ${response.statusCode}`));
              return;
            }
            response.pipe(file).on('finish', resolve).on('error', reject);
          })
          .on('error', reject);
      });
      console.log(`Downloaded ${url} to ${dest}`);
      return;
    } catch (error) {
      console.error(`Attempt ${attempt} failed: ${error.message}`);
      if (attempt === retries) throw new Error(`Failed to download ${url} after ${retries} attempts`);
    }
  }
}

/**
 * Sync files to Vercel Blob Storage.
 */
async function syncFiles() {
  try {
    const existingFiles = await list();
    console.log('Existing files:', existingFiles);

    await Promise.all(
      filesToSync.map(async (file) => {
        const filePath = path.join(dirToSync, file);
        if (fs.existsSync(filePath)) {
          const fileContent = fs.readFileSync(filePath);
          await put(file, fileContent);
          console.log(`Synced ${file} to blob storage.`);
        } else {
          console.warn(`File ${filePath} does not exist.`);
        }
      })
    );
  } catch (error) {
    console.error('Error syncing files:', error);
  }
}

// Example usage
(async () => {
  const url = 'https://example.com/data.json';
  const dest = path.join(dirToSync, 'data.json');
  await downloadFile(url, dest);
  await syncFiles();
})();
