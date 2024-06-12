<template>
    <div >
        <div>
            <div>
                <h1 class="py-4">Daily Weather - {{ this.weather.date }}</h1>
                
            </div>
            <div class="hr head">
                <div class="h">
                Max: {{ this.weather.max_f }}<br/>
                Min: {{ this.weather.min_f }}<br/>
                Average humidity: {{ this.weather.humidity }}<br/> 
                </div>
                <div class="h">
                    <a :href="this.weather_update_url">
                    <button >
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil" viewBox="0 0 16 16">
                    <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325"/>
                    </svg>
                        Notes!</button>
                    </a><br />
                    {{ this.weather.note }}
                    
                </div>
            </div>
            
        </div><br/>
        <div>
            <div class="head">
                <h4 class="h">Hour</h4>
                <h4 class="h">Temperature</h4>
                <h4 class="h">Condition</h4>
            </div><br />
            <div  v-for="(hourly,index) in this.weather.hourlys" @click="show[index] = !show[index]">
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
                    <div v-if= "!show[index]">
                       <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chevron-compact-down" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M1.553 6.776a.5.5 0 0 1 .67-.223L8 9.44l5.776-2.888a.5.5 0 1 1 .448.894l-6 3a.5.5 0 0 1-.448 0l-6-3a.5.5 0 0 1-.223-.67"/>
                    </svg>   
                    </div>
                    
                    <div v-if="show[index]">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chevron-compact-up" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M7.776 5.553a.5.5 0 0 1 .448 0l6 3a.5.5 0 1 1-.448.894L8 6.56 2.224 9.447a.5.5 0 1 1-.448-.894z"/>
                        </svg>
                    </div>
                    
                </div>

                <div v-if="show[index]" class="detail table">
                    <div class="c">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-thermometer-half" viewBox="0 0 16 16">
                        <path d="M9.5 12.5a1.5 1.5 0 1 1-2-1.415V6.5a.5.5 0 0 1 1 0v4.585a1.5 1.5 0 0 1 1 1.415"/>
                        <path d="M5.5 2.5a2.5 2.5 0 0 1 5 0v7.55a3.5 3.5 0 1 1-5 0zM8 1a1.5 1.5 0 0 0-1.5 1.5v7.987l-.167.15a2.5 2.5 0 1 0 3.333 0l-.166-.15V2.5A1.5 1.5 0 0 0 8 1"/>
                        </svg>
                        Feels like<br/> {{hourly.feels_like }}</div>
                    <div class="c">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-wind" viewBox="0 0 16 16">
                        <path d="M12.5 2A2.5 2.5 0 0 0 10 4.5a.5.5 0 0 1-1 0A3.5 3.5 0 1 1 12.5 8H.5a.5.5 0 0 1 0-1h12a2.5 2.5 0 0 0 0-5m-7 1a1 1 0 0 0-1 1 .5.5 0 0 1-1 0 2 2 0 1 1 2 2h-5a.5.5 0 0 1 0-1h5a1 1 0 0 0 0-2M0 9.5A.5.5 0 0 1 .5 9h10.042a3 3 0 1 1-3 3 .5.5 0 0 1 1 0 2 2 0 1 0 2-2H.5a.5.5 0 0 1-.5-.5"/>
                        </svg>
                        Wind <br/>{{ hourly.wind_mph }} mph</div>
                    <div class="c">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-droplet" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M7.21.8C7.69.295 8 0 8 0q.164.544.371 1.038c.812 1.946 2.073 3.35 3.197 4.6C12.878 7.096 14 8.345 14 10a6 6 0 0 1-12 0C2 6.668 5.58 2.517 7.21.8m.413 1.021A31 31 0 0 0 5.794 3.99c-.726.95-1.436 2.008-1.96 3.07C3.304 8.133 3 9.138 3 10a5 5 0 0 0 10 0c0-1.201-.796-2.157-2.181-3.7l-.03-.032C9.75 5.11 8.5 3.72 7.623 1.82z"/>
                        <path fill-rule="evenodd" d="M4.553 7.776c.82-1.641 1.717-2.753 2.093-3.13l.708.708c-.29.29-1.128 1.311-1.907 2.87z"/>
                        </svg>
                        Humidity <br/>{{ hourly.humidity }} %</div>
                   
                    <div class="c">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cloud-drizzle" viewBox="0 0 16 16">
                        <path d="M4.158 12.025a.5.5 0 0 1 .316.633l-.5 1.5a.5.5 0 0 1-.948-.316l.5-1.5a.5.5 0 0 1 .632-.317m6 0a.5.5 0 0 1 .316.633l-.5 1.5a.5.5 0 0 1-.948-.316l.5-1.5a.5.5 0 0 1 .632-.317m-3.5 1.5a.5.5 0 0 1 .316.633l-.5 1.5a.5.5 0 0 1-.948-.316l.5-1.5a.5.5 0 0 1 .632-.317m6 0a.5.5 0 0 1 .316.633l-.5 1.5a.5.5 0 1 1-.948-.316l.5-1.5a.5.5 0 0 1 .632-.317m.747-8.498a5.001 5.001 0 0 0-9.499-1.004A3.5 3.5 0 1 0 3.5 11H13a3 3 0 0 0 .405-5.973M8.5 2a4 4 0 0 1 3.976 3.555.5.5 0 0 0 .5.445H13a2 2 0 0 1 0 4H3.5a2.5 2.5 0 1 1 .605-4.926.5.5 0 0 0 .596-.329A4 4 0 0 1 8.5 2"/>
                        </svg>
                        Precipitation<br/> {{ hourly.precip_in }} in</div>
                    <div class="c">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-brightness-high" viewBox="0 0 16 16">
                        <path d="M8 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6m0 1a4 4 0 1 0 0-8 4 4 0 0 0 0 8M8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0m0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13m8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5M3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8m10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0m-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0m9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707M4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708"/>
                        </svg>
                        UV index<br/> {{ hourly.uv }}</div>
                    <div class="c">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star" viewBox="0 0 16 16">
                        <path d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.56.56 0 0 0-.163-.505L1.71 6.745l4.052-.576a.53.53 0 0 0 .393-.288L8 2.223l1.847 3.658a.53.53 0 0 0 .393.288l4.052.575-2.906 2.77a.56.56 0 0 0-.163.506l.694 3.957-3.686-1.894a.5.5 0 0 0-.461 0z"/>
                        </svg>
                        Condition <br/>
                        {{ hourly.condition }} </div>
                </div>
                <div v-else>
                </div>
                

                <!-- <img src={{hourly.condition_img }}><br> -->
            </div>
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
                show: [false, false,false,false,false,false,false,false,false,false,false,false,false, false,false,false,false,false,false,false,false,false,false,false],
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
        }, 
        beforeMount() {
            this.get_weather_info()
        },
        component(){
        }
    }
</script>
<style>

.container{
    background-color:white;
    /* min-height: 100%;
    bottom: 0;
    min-width:100%;
    margin:0; */
}
.detail{
    background-color:white;
    border-bottom:solid lightgray 1px;
    border-radius: 5px;
    display: flex;
    justify-content: space-evenly;
    margin: auto;
}
.head{
    /* background-color:white; */
    display: flex;
    justify-content: space-around;
    margin: auto;
}
.hr{
    background-color:#d3f2ee;
    border-radius: 2px;
    border:solid lightgray 1px;
    padding:5px;
}
.c{
    flex:1 1 30%;
    text-align: center;
    padding: 10px;
}
.h{
    flex: 1 1 50%;
    text-align: center;
}
.detail:hover{
    background-color: #1ea896;
}
.dropdown-content{
    display: none;
    position: absolute;
    background-color:white;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}
.show{
    display: block;
}
.table{
    width: 95%;
    margin: auto;
    margin-top: 5px;
    margin-bottom: 5px;
    padding: 1px;
    border-radius: 5px;
    border:solid gray 1px;
    display: grid;
    grid-template-columns: 200px 200px 200px;
    background-color:white;
}
.button{
    float: right;
    border-radius: 5px;
}

</style>