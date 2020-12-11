<template>
<div class="">
<div id="content" style="margin:0 auto;background:orange;"> 
    <div @click="goFullScreen()">全屏</div> 
    <div @click="exitFullscreen()">退出</div> 
</div>
</div>
</template>

<script>
export default {
    name:"",
    data(){
        return{
        }
    },
    created(){
    },  
    methods:{
        goFullScreen(){
        　　var element = document.getElementById("content");
        　　var requestMethod = element.requestFullScreen || element.webkitRequestFullScreen || element.mozRequestFullScreen || element.msRequestFullScreen;
        　　if (requestMethod) {
        　　　　requestMethod.call(element);
        　　} else if (typeof window.ActiveXObject !== "undefined") {
        　　　　var wscript = new ActiveXObject("WScript.Shell");
        　　　　if (wscript !== null) {
        　　　　　　wscript.SendKeys("{F11}");
        　　　　}
        　　}
        },
        exitFullscreen(){
        　　if (document.exitFullscreen) {
        　　　　document.exitFullscreen();
        　　} else if (document.msExitFullscreen) {
        　　　　document.msExitFullscreen();
        　　} else if (document.mozCancelFullScreen) {
        　　    document.mozCancelFullScreen();
        　　} else if (document.webkitExitFullscreen) {
        　　    document.webkitExitFullscreen();
        　　}
        },
    },
}
</script>

<style>
</style>