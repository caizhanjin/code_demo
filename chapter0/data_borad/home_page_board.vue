<template>
<div class="hpb_body" id="content" style="height:100%;width:95.5%;margin:0;padding:0 2% 0 2.5%;overflow:hidden;">
    <div class="hpb_header" style="padding-top: .08rem;height: 8%;width: 100%;">
        <div class="mode_left" style="width:30%;float: left;padding-top: 1.5%;">
            <ul class="hpb_header_ul li_float_left">
                <li :class="{'hpb_header_ul_li_active' : li_list[0]==1}" @click="switchTab(0)">实时监控</li>
                <li :class="{'hpb_header_ul_li_active' : li_list[1]==1}" @click="switchTab(1)">切换2</li>
                <li :class="{'hpb_header_ul_li_active' : li_list[2]==1}" @click="switchTab(2)">切换3</li>
            </ul>
        </div>

        <div class="mode_middle hpb_title" style="width: 40%;height:100%;float: left;">
            <span>TDMS监控系统</span>
        </div>

        <div class="mode_right" style="width:30%;padding-top: 1.5%;float: right;">
            <ul class="hpb_header_ul li_float_right">
                <li :class="{'hpb_header_ul_li_active' : li_list[5]==1}" @click="switchTab(5)">{{ is_full_screen?'退出全屏':'进入全屏' }}</li>
                <li :class="{'hpb_header_ul_li_active' : li_list[4]==1}" @click="switchTab(4)">切换2</li>
                <li :class="{'hpb_header_ul_li_active' : li_list[3]==1}" @click="switchTab(3)">切换3</li>
            </ul>
        </div>
    </div>
    <div class="hpb_main" style="height:92%;">
        <div class="hpb_left" style="width:25%;height: 100%;float: left;">
            <div class="hpb_left_top hpb_all_box" style="width:97%;height:60%;">
                <div class="hpb_title_father"> 
                    <h2 class="hpb_title_h2">待处理异常</h2>
                </div>
                <div class="hpb_list_ul">
                    <div style="padding:.06rem 0.05rem;font-size: .06rem;">
                        <span>状态：待处理</span>
                        <span class="hpb_color1 float_right">2018/06/22</span>
                    </div>
                    <div id="hpb_ul_review_box" style="height: 800px;overflow: hidden;">
                        <ul id="hpb_ul_roll1">
                            <li :class="{'hpb_list_ul_bg1': key%2==0, 'hpb_list_ul_bg2': key%2!=0}" v-for="(item, key) in order_list" :key="key">
                                <p><span>单号：{{ item.num }}</span><span class="hpb_color1 float_right">{{ item.date }}</span></p>
                                <p class="hpb_color1" style="padding-top:.03rem;">{{ item.detail }}</p>
                            </li>
                        </ul>
                        <ul id="hpb_ul_roll1">
                            <li :class="{'hpb_list_ul_bg1': key%2==0, 'hpb_list_ul_bg2': key%2!=0}" v-for="(item, key) in order_list" :key="key">
                                <p><span>单号：{{ item.num }}</span><span class="hpb_color1 float_right">{{ item.date }}</span></p>
                                <p class="hpb_color1" style="padding-top:.03rem;">{{ item.detail }}</p>
                            </li>
                        </ul>
                        <ul id="hpb_ul_roll2"></ul>
                    </div>
                </div>
            </div>
            <div class="hpb_left_down hpb_all_box" style="width:97%;height:33%;margin-top:3%;">
                <div class="hpb_title_father"> 
                    <h2 class="hpb_title_h2">我是模块标题</h2>
                </div>
                <div @click="test()">test websocket connect</div>
            </div>
        </div>
        <div class="hpb_middle" style="width: 55%;height: 100%;float: left;">
            <div class="hpb_middle_top" style="width:98.5%;height:60%;">
                <h2 class="hpb_title_h2">我是模块标题</h2>
                <div id="chart_contain_h1" :style="{width: '100%', height: '90%'}"></div>
            </div>
            <div class="hpb_middle_down hpb_all_box" style="width:98.5%;height:32.8%;margin-top:1.6%;">
                <div class="hpb_title_father"> 
                    <h2 class="hpb_title_h2">我是模块标题</h2>
                </div>
                <div id="chart_contain_test" :style="{width: '100%', height: '90%'}"></div>
            </div>
        </div>
        <div class="hpb_right" style="width:20%;height: 100%;float: right;">
            <div class="hpb_right_top hpb_all_box" style="width: 100%;height: 15%; display: table;">
                <div class="hpb_clock" style="vertical-align: middle;display: table-cell;">
                    <div class="hpb_time">{{ clock_time }}</div>
                    <div class="hpb_date" >
                        <span>{{ clock_date }}</span>
                        <span>{{ clock_day_part }}</span>
                        <span>{{ clock_week }}</span>
                    </div>
                </div>

            </div>
            <div class="hpb_right_middle hpb_all_box" style="width:100%;height:42%;margin-top:3.6%;">
                <div class="hpb_title_father"> 
                    <h2 class="hpb_title_h2">电芯测试完成率</h2>
                </div>
                <div id="chart_contain_h2" :style="{width: '100%', height: '90%'}"></div>
            </div>
            <div class="hpb_right_down hpb_all_box" style="width:100%;height:33.5%;margin-top:3.6%;">
                <div class="hpb_title_father"> 
                    <h2 class="hpb_title_h2">我是模块标题</h2>
                </div>
            </div>

        </div>
    </div>
</div>
</template>

<script>


export default {
    name:"",
    data(){
        return{
            li_list: [1, 2, 2, 2, 2, 2],

            is_full_screen: false,
            sday: "",

            clock_time: "",
            clock_date: "",
            clock_week: "",
            clock_day_part: "",
            week_day: ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"],

            order_list: [
                {num: "C202002128726", date: "2018/06/22 12:20", detail: "审核过程中，出现数据异常，请XX实验室某某人员及时前往现场处理。"},
                {num: "C202002128726", date: "2018/06/22 12:20", detail: "审核过程中，出现数据异常，请XX实验室某某人员及时前往现场处理。"},
            ],

            chart_dict:{
                "h1":{
                    width: 1000,
                    heigth: 300,
                    data: "",
                },

            },
        }
    },
    mounted(){
        var _this = this
        this.timeId = setInterval(function() { _this.dynamicClock() }, 1000)
        this.listRoll(50)

        this.drawChartH1()
        this.drawChartH2()
    }, 
    beforeDestroy: function() {
        if (this.timeId) {
            clearInterval(this.timeId);
        }
    },
    methods:{
        test(){
            this.$fetch(this.$path + "review/HongFTPRawDataViewSet/get_test/"
            ).then(res => {
                var series = []
                var legends = []
                for(var key in res.dataInfo){
                    series.push({
                        "name": key,
                        "type": "line",
                        "data": res.dataInfo[key],
                    })
                    legends.push(key)
                }

                var xAxis = new Array(10000).fill('').map( (item, index) => index+1)

                console.log(series)
                console.log(legends)
                console.log(xAxis)

            var chart_contain_h2 = this.$echarts.init(document.getElementById("chart_contain_h1"))
            var option = {
                backgroundColor: '#2c343c',
                title: {
                    text: '折线图堆叠'
                },
                textStyle: {
                    color: '#FFFFFF'
                },
                tooltip: {
                    trigger: 'axis'
                },
                dataZoom: [
                    {   // 这个dataZoom组件，默认控制x轴。
                        type: 'slider', // 这个 dataZoom 组件是 slider 型 dataZoom 组件
                        start: 10,      // 左边在 10% 的位置。
                        end: 60         // 右边在 60% 的位置。
                    }
                ],
                legend: {
                    data: legends
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                toolbox: {
                    feature: {
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: xAxis
                },
                yAxis: {
                    type: 'value'
                },
                series: series
            };

   
            chart_contain_h2.setOption(option, true);
            

            window.addEventListener('resize', () => {
                chart_contain_h2.resize();
            })


            })
        },
        createWebSocket(){
            this.ws = ''
            // WebSocket长连接
            if(typeof WebSocket != 'undefined'){
                // var path = this.$path.replace(/http/g, 'ws')
                // var ws_path = path + 'errors/listen_abnormal_change/'
                var ws_path = "ws://127.0.0.1:8001/test/Websocket"
                this.ws = new WebSocket(ws_path);
                this.initEventHandle()
            }else{
                this.$message.error('当前浏览器不支持WebSocket，请更换浏览器')
            }
        },
        reconnect(){
            //没连接上会一直重连，设置延迟避免请求过多
            if(this.lockReconnect) return
            this.lockReconnect = true
            var _this = this
            setTimeout(function () {     
                _this.createWebSocket()
                _this.lockReconnect = false;
            }, 2000);
        },
        initEventHandle(){
            var _this = this
            if(this.heartCheck){
                window.clearTimeout(this.heartCheck.timeoutObj)
                window.clearTimeout(this.heartCheck.serverTimeoutObj)
            }

            // 心跳检测
            // 发送心跳，后端收到返回回应心跳消息
            // onmessage拿到心跳消息，说明连接正常，重启心跳检测
            // 如果超出时间没有重连，说明服务器主动断开，重新连接
            this.heartCheck = {
                timeout: 1*1000,      // 发送心跳信息时间间隔 目前5s
                reconnectTime: 3*1000,  // 给服务端应答时间 目前3s
                timeoutObj: null,
                serverTimeoutObj: null,
                reset: function(){
                    clearTimeout(this.timeoutObj);
                    clearTimeout(this.serverTimeoutObj);
                    return this;
                },
                start: function(){
                    var self = this;
                    self.timeoutObj = setTimeout(function(){
                        if(_this.ws.readyState==1){
                            _this.ws.send('ping')
                            self.serverTimeoutObj = setTimeout(function(){ 
                                _this.reconnect()
                            }, self.reconnectTime)
                        }
                    }, self.timeout)
                }
            }

            this.ws.onopen = function(event){
                // 开启心跳机制
                _this.heartCheck.reset().start()
                _this.$message.success('语音反馈已经开启')
            }

            this.ws.onmessage = function(event){
                // 拿到任何来自服务端的消息说明连接正常，重启心跳
                _this.heartCheck.reset().start()
                if(event.data != 'pong'){
                    console.log("收到服务信息："+event.data)
                }
            }

            this.ws.onclose = function(event){
                _this.$message.success('语音反馈已经关闭')
            }

            this.ws.onerror = function(event) {
                // 不是客户端主动关闭，重新连接
                _this.reconnect()
            }
        },
        drawChartH1(){
            var chart_contain_h1 = this.$echarts.init(document.getElementById("chart_contain_h1"))
            chart_contain_h1.setOption({
                textStyle: {
                    color: '#FFFFFF'
                },
                // title: {
                //     text: '堆叠区域图'
                // },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross',
                        label: {
                            backgroundColor: '#6a7985'
                        }
                    }
                },
                legend: {
                    data: ['邮件营销', '联盟广告', '视频广告', '直接访问', '搜索引擎'],
                    color: '#FFFFFF'
                },
                toolbox: {
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: [
                    {
                        type: 'category',
                        boundaryGap: false,
                        data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                    }
                ],
                yAxis: [
                    {
                        type: 'value'
                    }
                ],
                series: [
                    {
                        name: '邮件营销',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {},
                        data: [120, 132, 101, 134, 90, 230, 210]
                    },
                    {
                        name: '联盟广告',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {},
                        data: [220, 182, 191, 234, 290, 330, 310]
                    },
                    {
                        name: '视频广告',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {},
                        data: [150, 232, 201, 154, 190, 330, 410]
                    },
                    {
                        name: '直接访问',
                        type: 'line',
                        stack: '总量',
                        areaStyle: {},
                        data: [320, 332, 301, 334, 390, 330, 320]
                    },
                    {
                        name: '搜索引擎',
                        type: 'line',
                        stack: '总量',
                        label: {
                            normal: {
                                show: true,
                                position: 'top'
                            }
                        },
                        areaStyle: {},
                        data: [820, 932, 901, 934, 1290, 1330, 1320]
                    }
                ]
            })

            window.addEventListener('resize', () => {
                chart_contain_h1.resize();
            })
        },
        drawChartH2(){
            var chart_contain_h2 = this.$echarts.init(document.getElementById("chart_contain_h2"))
            var option = {
                textStyle: {
                    color: '#FFFFFF'
                },
                tooltip: {
                    formatter: '{a} <br/>{b} : {c}%'
                },
                toolbox: {
                    feature: {
                        restore: {},
                        saveAsImage: {}
                    }
                },
                series: [
                    {
                        name: '业务指标',
                        type: 'gauge',
                        detail: {formatter: '{value}%'},
                        data: [{value: 50, name: '完成率'}],
                    }
                ]
            }

            setInterval(function () {
                option.series[0].data[0].value = (Math.random() * 100).toFixed(2) - 0;
                chart_contain_h2.setOption(option, true);
            },2000);

            window.addEventListener('resize', () => {
                chart_contain_h2.resize();
            })
        },
        rollStart(){
            var ul1 = document.getElementById("hpb_ul_roll1");
            var ulbox = document.getElementById("hpb_ul_review_box");
            if (ulbox.scrollTop >= ul1.scrollHeight) {
                ulbox.scrollTop = 0;
            } else {
                ulbox.scrollTop++;
            }
        },
        listRoll(roll_time){
            while(this.order_list.length < 15){
                this.order_list = this.order_list.concat(this.order_list)
            }
            var _this = this
            var ul1 = document.getElementById("hpb_ul_roll1")
            var ul2 = document.getElementById("hpb_ul_roll2")
            var ulbox = document.getElementById("hpb_ul_review_box")
            ul2.innerHTML = ul1.innerHTML
            ulbox.scrollTop = 0
            var timer = setInterval(_this.rollStart, roll_time)
            ulbox.onmouseover = function () {
                clearInterval(timer);
            }
            ulbox.onmouseout = function () {
                timer = setInterval(_this.rollStart, roll_time);
            }
        },
        dynamicClock(){
            var now_date = new Date()
            var hour = now_date.getHours() 
            if(hour > 12){
                this.clock_day_part = "PM"
                hour -=  12
            }else{
                this.clock_day_part = "AM"
            }
            hour = hour>12 ? (hour - 12) : hour

            this.clock_time = this.addZero(hour) + ":" + this.addZero(now_date.getMinutes()) + ":" + this.addZero(now_date.getSeconds())
            this.clock_date = now_date.getFullYear() + "/" + this.addZero((now_date.getMonth()+1)) + "/" + this.addZero(now_date.getDate())
            this.clock_week = this.week_day[now_date.getDay()]
        },
        addZero(num){
            if(num < 10){
                num = "0" + num
            }
            return num
        },
        switchTab(tab_num){
            if(tab_num == 5){
                if(this.is_full_screen == false){
                    this.goFullScreen()
                }else{
                    this.exitFullscreen()
                }
            }else{
                this.li_list = [2, 2, 2, 2, 2, 2]
                this.li_list[tab_num] = 1
            }
        },
        goFullScreen(){
            this.is_full_screen = true
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
            this.is_full_screen = false
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
.hpb_body{
    color: rgb(255, 255, 255);
    font-family:microsoft yahei;
    background: url("../../../assets/images/home_page_backgroud.png") 0px 0px / 100% 100% no-repeat rgb(0, 6, 91);
    background-position: 0px 0px;
    background-repeat: no-repeat
}

.hpb_title{
    text-align: center;
    display: table-cell;
    vertical-align: middle;
}

.hpb_title span{
    height: 100%;
    font-size: .22rem;
    font-weight: bolder;
    cursor: text;
}

.hpb_all_box {
    background: rgba(255, 255, 255, 0.1);
    border-radius: .06rem .06rem 0.03rem 0.03rem;
}

.hpb_title_h2{
    text-align: center;
    width: 100%;
    font-size: .06rem;
    line-height: 0.13rem;
    font-weight: normal;
    letter-spacing: .015rem;
    overflow: hidden;

}

.hpb_header_ul, .hpb_list_ul ul{
    list-style: none;
    font-style: normal;
}

.hpb_header_ul li{
    background: url("../../../assets/images/bnt.png") center;
    font-size: .08rem;
    line-height: .2rem;
    background-repeat: no-repeat;
    width: 18%;
    height: .2rem;
    text-align: center;
    cursor:pointer;
}

.li_float_left li{
    float: left;
    margin-left: 5%;
}

.li_float_right li{
    float: right;
    margin-right: 5%;
}

.hpb_header_ul_li_active{
    background: url("../../../assets/images/bntactive.png") no-repeat center !important;
}

.hpb_title_father{
    background:rgb(44, 74, 130);
    border-radius: .1rem .1rem 0 0;
}

.hpb_time, .hpb_date{
    color: #cdddf7;
    text-align: center;
    margin: 0;
}

.hpb_time{
    font-size: .36rem;
}

.hpb_date{
    font-size: .13rem;
}

.hpb_right_top {
    border: 1px solid #0E94EA;
}

.hpb_list_ul ul li{
    padding: .08rem;
    font-size: .05rem;
}

.hpb_list_ul_bg1{
    background: rgba(0,255,255,.4) url("../../../assets/images/icosjx.png") no-repeat top left;
}

.hpb_list_ul_bg2{
    background: rgba(1,202,217,.2) url("../../../assets/images/icosjx.png") no-repeat top left;
}

.hpb_color1{
    color: rgba(255,255,255,.7)
}

.float_right{
    float: right;
}

.hpb_left_top{
    overflow: hidden;
}

</style>