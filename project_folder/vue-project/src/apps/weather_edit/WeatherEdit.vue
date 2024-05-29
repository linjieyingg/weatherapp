<template>
  <div>
      This is the form coming from django, displayed in vue. <br><br>
  </div>
    <!-- With fetch this time
    <div v-if="form_error">
        <ul>
            <li v-for="(error, index) in form_error">
                {{error}}
            </li>
        </ul>
    </div>
    <div v-if="form_updated">
        {{ form_updated }}
    </div> -->
  
  <p>dico:{{ weather_dico }}</p>
  {{ test }}
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
        
        <button type="submit" class="btn btn-primary" @click.prevent="submit_form" :disabled="submitting_form">Submit</button>
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
        weather_dico: window.ext_weather_dict,
        // rest: window.ext_weather_dict.rest,
        // note: window.ext_weather_dico.note,
        update_bis_url: window.ext_update_bis_url,
      }
    },
    methods: {
      submit_form(){
            if (this.submitting_form === true) {
            return;
            }
            this.submitting_form = true
            var form = document.createElement('form');
            form.setAttribute('method', 'post');
            let form_data = {
                'csrfmiddlewaretoken': this.csrf_token,
                'note': this.weather_dico.note
            }
            console.log('data', form_data)
          
            for (var key in form_data) {
                var html_field = document.createElement('input')
                html_field.setAttribute('type', 'hidden')
                html_field.setAttribute('name', key)
                html_field.setAttribute('value', form_data[key])
                form.appendChild(html_field)
            }
            form.appendChild(actor_field)
            document.body.appendChild(form);
            form.submit()
        },
      submit_form_fetch() {
        this.form_error = []
        this.form_updated = ""
        let formData = new FormData()
        let form_data = {
          'csrfmiddlewaretoken': this.csrf_token,
          'note': this.note
        }
        for (var key in form_data) {
          formData.append(key, form_data[key])
        }
        // this.student_list.map(dic => formData.append('students', dic.id))
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
            this.form_updated = 'course has been updated'
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
