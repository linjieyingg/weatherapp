<template>
    <div v-if="form_error">
        <ul>
            <li v-for="(error, index) in form_error">
                {{error}}
            </li>
        </ul>
    </div>
    <div v-if="form_updated">
        {{ form_updated }}
    </div>

  <div>
      <form method="post" class="form">
        <input type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrf_token">
        <p>
          <label for="id_date">Date:</label><br>
          <input type="text" name="date" v-model="date" maxlength="100" required="" id="id_date">
        </p>
        <p>
          <label for="id_note">Note:</label><br>
          <input type="text" name="note" v-model="note" required="" id="id_note">
        </p>
        
        <button type="submit" class="btn btn-primary" @click.prevent="submit_form_fetch" :disabled="submitting_form">Submit</button>
      </form>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data: function () {
      return {
        submitting_form: false,
        form_error: [],
        form_updated: "",
        csrf_token: window.ext_csrf_token,
        form: window.ext_django_form,
        weather_dico: window.ext_weather_dico,
        // rest: window.ext_weather_dict.rest,
        note: window.ext_weather_dico.note,
        date:window.ext_weather_dico.date,
        update_bis_url: window.ext_update_bis_url,
        weather_detail_js_url: window.ext_weather_detail_js_url,
        submitting_form: false,
      }
    },
    methods: {
      submit_form_fetch() {
        this.form_error = []
        this.form_updated = ""
        let formData = new FormData()
        let form_data = {
          'csrfmiddlewaretoken': this.csrf_token,
          'note': this.note,
          'date': this.date
        }
        for (var key in form_data) {
          formData.append(key, form_data[key])
        }
        console.log("formData: ", formData)
        fetch(this.update_bis_url, {
          method: 'post',
          body: formData,
          headers: { 'X-CSRFToken': this.csrf_token },
          credentials: 'same-origin'
        }).then(function(response) {
          console.log('response', response)
          return response.json()}).then(
              this.handleResponse).catch(
                  (error) => {
                  console.log('error', String(error))
                  this.form_error=["error"]
          })
      },
      handleResponse(response) {
        console.log('json response', response)
        if ('success' in response) {
          if (response['success'] == true) {
            this.form_updated = 'notes has been updated!'
          } else {
            if ('errors' in response) {
              for (const [key, value] of Object.entries(response['errors'])) {
                for (const error of value) {
                  this.form_error.push(`${key}: ${error}`)
                }
              }
            } else {
              this.form_error = [
                'Update failed - An error occurred but do not have more information about it'
              ]
            }
          }
        } else {
          this.form_error = ['Update failed - It has been an error on the form request']
        }
      }
    }
  }
</script>