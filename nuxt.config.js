import Tags from './data/tags.json'
import { map } from 'lodash'

export default {
  // Target (https://go.nuxtjs.dev/config-target)
  target: 'static',

  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'Good First Issue: Issues for your first open-source contribution',
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/images/icon.png' }],
    script: [
      {
        hid: 'plausible',
        src: 'https://plausible.io/js/plausible.js',
        async: true,
        'data-domain': 'goodfirstissue.dev'
      }
    ],
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content:
          'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can fix easily. Start today!'
      },
      {
        hid: 'keywords',
        name: 'keywords',
        content:
          'good first issue, open source, github, beginner, pull requests, help wanted, deepsource'
      },
      {
        hid: 'og:image',
        property: 'og:image',
        content: '/images/meta.jpg'
      },
      {
        hid: 'og:title',
        name: 'twitter:title',
        content: 'Good First Issue: Issues for your first open-source contribution'
      },
      {
        hid: 'og:description',
        name: 'twitter:description',
        content:
          'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can fix easily. Start today!'
      },
      {
        hid: 'twitter:site',
        name: 'twitter:site',
        content: '@DeepSourceHQ'
      },
      {
        hid: 'twitter:card',
        name: 'twitter:card',
        content: 'summary'
      }
    ]
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: ['@nuxtjs/tailwindcss', '@nuxtjs/google-fonts'],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    // https://go.nuxtjs.dev/content
    '@nuxt/content',
    '@nuxtjs/sitemap'
  ],

  // Content module configuration (https://go.nuxtjs.dev/config-content)
  content: {},

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {},

  googleFonts: {
    families: {
      Inter: [400, 500, 600, 700]
    }
  },
  googleAnalytics: {
    id: 'UA-125031134-3'
  },
  generate: {
    routes: [
      ...map(Tags, (tag) => {
        return `/language/${tag.slug}`
      })
    ]
  },
  sitemap: {
    hostname: 'https://goodfirstissue.dev',
    gzip: true,
    defaults: {
      changefreq: 'daily',
      lastmod: new Date()
    }
  }
}
