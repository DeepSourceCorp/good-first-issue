// THIS FILE SHOULD NOT BE VERSION CONTROLLED

// https://github.com/NekR/self-destroying-sw

self.addEventListener('install', function () {
  self.skipWaiting()
})

self.addEventListener('activate', function () {
  self.registration
    .unregister()
    .then(function () {
      return self.clients.matchAll()
    })
    .then(function (clients) {
      clients.forEach((client) => client.navigate(client.url))
    })
})
