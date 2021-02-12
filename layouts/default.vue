<template>
  <div class="bg-ink-400 flex flex-col min-h-screen antialiased text-vanilla-300">
    <banner cta-link="https://deepsource.io/discover">
      <span slot="text">Find issues in any open source repository and fix them automatically with Discover.</span>
      <template slot="cta">LEARN MORE <ExternalLinkIcon class="h-4 md:h-6 ml-1 md:ml-2 text-vanilla-400"/></template>
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

export default {
  components: {
    Navbar,
    Sidebar,
    Banner,
    ExternalLinkIcon
  },
  data: function () {
    return {
      tag: {}
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
