<template>
  <div class="mdui-card mdui-m-a-1 mdui-shadow-0 mdui-color-blue-grey">
    <div class="mdui-card-header">
      <img class="mdui-card-header-avatar" src="" />
      <div class="mdui-card-header-title">{{ MessageInfo }}</div>
      <div class="mdui-card-header-subtitle">
        {{ MessageInfoHtml }} x {{ device }}
      </div>
    </div>

    <div class="mdui-card-media">
      <div class="mdui-card-content" style="max-height:200px">
        {{ MessageContent }}
      </div>
      <div class="mdui-divider"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    MessageInfo: String,
    MessageInfoHtml: String,
    device: String,
    MessageContent: String,
  },
};
</script>
