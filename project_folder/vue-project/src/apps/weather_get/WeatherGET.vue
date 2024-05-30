<template>
    <div>
        <a :href="this.weather_list_url">Observation List</a><br/>
        <a :href="this.weather_update_url">Update Observation</a><br/>
        <h1>{{ this.weather.date }}</h1>
        Max: {{ this.weather.max_f }}<br/>
        Min: {{ this.weather.min_f }}<br/>
        Average humidity: {{ this.weather.humidity }}<br/>
        Notes: {{ this.weather.note }}
    </div><br/>
    <div>
       {{ this.weather.hourlys }}
        <span v-for="hourly in this.weather.hourlys">
            {{ convert_time_to_string(hourly.date)}} <br>
            Temperature: {{ hourly.temp_f }} <br>
            Condition: {{ hourly.condition }} <br>
            <!-- <img src={{hourly.condition_img }}><br> -->
            <br/></span>
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
                weathert_list_url: window.ext_weather_list_url,
                weather_update_url: window.ext_weather_update_url,
                weather: {}, 
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
            }
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