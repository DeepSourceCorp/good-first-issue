<template>
  <div class="bg-ink-400 flex flex-col min-h-screen antialiased text-vanilla-300">
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

export default {
  data: function() {
    return {
      tag: {}
    }
  },
  components: {
    Navbar,
    Sidebar
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

      chimpPopupLoader.onload = function() {
        document.body.appendChild(chimpPopup)
      }
      document.body.appendChild(chimpPopupLoader)
    }
  }
}
</script>
