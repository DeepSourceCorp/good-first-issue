export default {
  // Target (https://go.nuxtjs.dev/config-target)
  target: "static",

  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: "Good First Issue: Issues for your first open-source contribution",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "description",
        name: "description",
        content:
          "Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can fix easily. Start today!"
      },
      {
        hid: "keywords",
        name: "keywords",
        content:
          "good first issue, open source, github, beginner, pull requests, help wanted, deepsource"
      },
      {
        hid: "og:image",
        property: "og:image",
        content: "/images/meta.jpg"
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
  buildModules: ["@nuxtjs/tailwindcss", "@nuxtjs/google-fonts"],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/pwa
    "@nuxtjs/pwa",
    // https://go.nuxtjs.dev/content
    "@nuxt/content"
  ],

  // Content module configuration (https://go.nuxtjs.dev/config-content)
  content: {},

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {},

  googleFonts: {
    families: {
      Inter: [400, 500, 600, 700]
    }
  }
};
