<template>
  <Coolapk :t="token" />
</template>

<script>
import Coolapk from './components/Coolapk.vue'
import { get_token } from './api/token.ts'

export default {
  name: 'App',
  components: {
    Coolapk
  },
  data() {
  return {
		token: get_token()
	}
  }
}
</script>
