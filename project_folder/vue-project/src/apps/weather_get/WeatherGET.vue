<template>

    <div>
        <a :href="this.weather_list_url">Observation List</a><br/>
        <a :href="this.weather_update_url">Update Observation</a><br/>
        <h1>{{ this.weather.date }}</h1>
        Max: {{ this.weather.max_f }}<br/>
        Min: {{ this.weather.min_f }}<br/>
        GPA: {{ this.weather.gpa }}<br/>
    </div>

</template>
    
<script>
    export default { 
        name: 'App', 
        data: function() {
            return {
                weather_error: [],
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
        }, 
        beforeMount() {
            this.get_weather_info()
        },
    }
</script>