<template>
  <title>主页 - coolapk</title>
  <body class="mdui-bottom-nav-fixed mdui-theme-primary-green">
    <div class="mdui-appbar">
      <div class="mdui-toolbar mdui-color-theme">
        <a href="javascript:;" class="mdui-typo-title">酷安</a>
        <div class="mdui-toolbar-spacer"></div>
        <a href="javascript:;" class="mdui-btn mdui-btn-icon"
          ><i class="mdui-icon material-icons">search</i></a
        >
        <a href="javascript:location.replace();" class="mdui-btn mdui-btn-icon"
          ><i class="mdui-icon material-icons">refresh</i></a
        >
      </div>
      <div class="mdui-tab mdui-color-theme" mdui-tab>
        <a href="#example3-tab1" class="mdui-ripple mdui-ripple-white">头条</a>
        <a href="#example3-tab1" class="mdui-ripple mdui-ripple-white">热榜</a>
      </div>
    </div>
    <Card MessageInfo="tetst" MessageInfoHtml="<p>jsnsjsjsnssjsksjdidjdbdxidujdjsjs" device="ysys" :MessageContent="t" />
    <div
      class="mdui-bottom-nav mdui-bottom-nav-text-auto mdui-color-theme mdui-bottom-nav-scroll-hide"
    >
      <a
        href="javascript:void(0);"
        class="mdui-ripple mdui-ripple-white mdui-bottom-nav-active"
      >
        <i class="mdui-icon material-icons mdui-color">home</i>
        <label>首页</label>
      </a>
      <a href="javascript:void(0);" class="mdui-ripple mdui-ripple-white">
        <i class="mdui-icon material-icons">view_compact</i>
        <label>酷图</label>
      </a>
    </div>
  </body>
</template>

<script>
import Card from "./Card.vue";
export default {
  name: "Coolapk",
  components: {
    Card,
  },
  props: {
	t: String
  }
};
</script>
