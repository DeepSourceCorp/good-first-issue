<template>
  <div class="bg-ink-400 flex flex-col min-h-screen antialiased text-vanilla-300">
    <banner>
      <a
        :href="BANNER.CTA.LINK"
        target="_blank"
        class="flex flex-row items-center text-center justify-center space-x-2"
      >
        <span>{{ BANNER.TEXT }}</span>
        <ExternalLinkIcon class="md:inline-block hidden" size="1x" />
      </a>
    </banner>
    <navbar :tag="tag"></navbar>
    <main class="flex flex-1">
      <section class="container max-w-6xl mx-auto flex flex-col md:flex-row">
        <sidebar></sidebar>
        <Nuxt />
      </section>
    </main>
  </div>
</template>

<script>
import Navbar from '~/components/Navbar.vue'
import Sidebar from '~/components/Sidebar.vue'
import Banner from '~/components/Banner.vue'
import { ExternalLinkIcon } from 'vue-feather-icons'

const BANNER = {
  TEXT: 'Find and fix code quality issues in 10,000+ open-source projects with DeepSource Discover',
  CTA: {
    LINK: 'https://deepsource.io/discover'
  }
}

export default {
  components: {
    Navbar,
    Sidebar,
    Banner,
    ExternalLinkIcon
  },
  data: function () {
    return {
      tag: {},
      BANNER
    }
  },
  mounted() {
    this.setupMailchimpPopup()
  },
  methods: {
    setupMailchimpPopup() {
      var mailchimpConfig = {
        baseUrl: 'mc.us7.list-manage.com',
        uuid: 'd6efa53a6b024c63837f2816e',
        lid: '2ca4b2aca5'
      }
      // No edits below this line are required
      var chimpPopupLoader = document.createElement('script')
      chimpPopupLoader.src =
        '//s3.amazonaws.com/downloads.mailchimp.com/js/signup-forms/popup/embed.js'
      chimpPopupLoader.setAttribute('data-dojo-config', 'usePlainJson: true, isDebug: false')
      var chimpPopup = document.createElement('script')
      chimpPopup.appendChild(
        document.createTextNode(
          'require(["mojo/signup-forms/Loader"], function (L) { L.start({"baseUrl": "' +
            mailchimpConfig.baseUrl +
            '", "uuid": "' +
            mailchimpConfig.uuid +
            '", "lid": "' +
            mailchimpConfig.lid +
            '"})});'
        )
      )

      chimpPopupLoader.onload = function () {
        document.body.appendChild(chimpPopup)
      }
      document.body.appendChild(chimpPopupLoader)
    }
  }
}
</script>
