<template>
        <div>
            <div class="detail">
            <a :href="this.weather_list_url">Observation List</a><br/>
            <a :href="this.weather_update_url">Update Observation</a><br/> 
            </div>
           

            <h1>Hourly Weather - {{ this.weather.date }}</h1>
            Max: {{ this.weather.max_f }}<br/>
            Min: {{ this.weather.min_f }}<br/>
            Average humidity: {{ this.weather.humidity }}<br/>
            Notes: {{ this.weather.note }}
        </div><br/>
        <div>
            <div class="detail">
                <h4 class="c">Hour</h4>
                <h4 class="c">Temperature</h4>
                <h4 class="c">Condition</h4>
            </div><br />
            <div @click="show = !show" v-for="hourly in this.weather.hourlys" >
                <div class="detail" >
                    <div class="c">{{ ((hourly.date).toString().split("T"))[1].replace('Z', ' ').split(":")[0] }}
                    </div>
                <!-- {{ (convert_time_to_string(hourly.date)).replace('GMT-0400 (Eastern Daylight Time)', ' ')}} <br> -->
                    <div class="c">   
                        {{ hourly.temp_f }} 
                    </div>
                    <div class="c">
                        {{ hourly.condition }} 
                    </div>
                </div>

                <div v-if="show" class="detail">
                    <div class="c">feels like {{hourly.feels_like }}</div>
                    <div class="c">wind {{ hourly.wind_mph }}</div>
                    <div class="c">humidity {{ hourly.humidity }}</div>
                    
                    <div class="c">Precipitation {{ hourly.precip_in }}</div>
                    <div class="c">UV index {{ hourly.uv }}</div>
                    <div class="c">Pressure {{ hourly.pressure_in }}</div>
                </div>
                <div v-else>
                </div>
                

                <!-- <img src={{hourly.condition_img }}><br> -->
            </div>
        </div>  
    
</template>
    
<script>
    export default { 
        name: 'App', 
        data: function() {
            return {
                weather_error: [],
                // hourlys: window.ext_hourlys,
                weather_id: window.ext_weather_id,
                weather_detail_js_url: window.ext_weather_detail_js_url,
                weather_list_url: window.ext_weather_list_url,
                weather_update_url: window.ext_weather_update_url,
                weather: {}, 
                show: false,
            }
        },
        methods: {
            get_weather_info() {
                fetch(this.weather_detail_js_url,
                    {
                        method: "get",
                        credentials: 'same-origin'
                    }
                ).then(function(response) {
                    console.log('response', response)
                    return response.json()}
                ).then((weather_json) => {
                    this.assign_weather(weather_json)}
                ).catch(
                    (error) => { 
                    console.log('error', error)
                    this.weather_error=["Error when loading weather information"]
                })
            },
            assign_weather(weather_json) {
                console.log("assign weather is working too")
                console.log('json', weather_json)
                this.weather = weather_json['weather']
            },
            convert_time_to_string(timo){
                if (timo) {
                    timo = new Date(timo)
                    // return `${timo.getHours()}:00`
                    return `${timo}`
                }
            },
            // show_content(){
            //     if (this.show){
            //         this.show = false
            //     }else{
            //         this.show=true

            //     }
                
            // }
        }, 
        beforeMount() {
            this.get_weather_info()
        },
        // mounted(){
        //     this.weather_detail_js_url=ext_weather_detail_js_url;
        //     this.weather_list_url=ext_weather_list_url;  
        //     this.weather_update_url= ext_weather_update_url;
        //     this.hourlys = JSON.parse(ext_hourlys);
        //     this.homework = ext_reminder_dict.homework;
        // },
    }
</script>
<style>
.detail{
    background-color: aliceblue;
    display: flex;
    justify-content: space-around;
    margin: auto;
}
.c{
    flex:1 1 30%;
    /* border:solid red 1px; */
    text-align: center;
    padding: 20px
}
.detail:hover{
    background-color: #b2c9f4;
}
.dropdown-content{
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}
/* .dropcheck:checked ~ .dropdown-content {
  display: block;
} */
.show{
    display: block;
}
</style>