<template>
    <div>
        This is the form coming from django, displayed in vue. <br><br>
    </div>

    With fetch this time
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

<<<<<<< Updated upstream
    <div>
      <form method="post" class="form">
        <input type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrf_token">
        <p>
          <label for="id_date">Date:</label><br>
          <input type="text" name="date" v-model="weather_date" maxlength="100" required="" id="id_date">
        </p>
        <p>
          <label for="id_teacher">Teacher:</label><br>
          <input type="text" name="teacher" v-model="course_teacher" maxlength="100" required="" id="id_teacher">
        </p>
        <p>
          <label for="id_grade">Grade:</label><br>
          <select name="grade" v-model="course_grade" maxlength="100" required="" id="id_grade">
            <option value="9">9</option>
            <option value="10">10</option>
            <option value="11">11</option>
            <option value="12">12</option>
          </select>
        </p>
        <p>
          <label for="id_students">Students:</label><br>
          <select hidden name="students" required="" id="id_students" multiple="">
            <option v-for="student in student_list" :value="student.id" selected=""></option>
          </select>
          <Multiselect v-model="student_list" :options="student_list_source" :multiple="true" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="Choose the student(s)" label="name" track-by="name" :preselect-first="true" style="display:inline-block;width: 300px;padding-bottom:10px;padding-left:10px">
            <template slot="selection" slot-scope="{ values, search, isOpen }"><span class="multiselect__single" v-if="values.length" v-show="!isOpen">{{ values.length }} options selected</span></template>
          </Multiselect>
        </p>
      <button type="submit" class="btn btn-primary" @click.prevent="submit_form_fetch" :disabled="submitting_form">Submit</button>
    </form>
  </div>
=======
>>>>>>> Stashed changes
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
        course_dico: window.ext_course_dico,
        course_name: window.ext_course_dico.name,
        course_teacher: window.ext_course_dico.teacher,
        course_grade: window.ext_course_dico.grade,
        student_list_source: window.ext_student_list,
        student_list: window.ext_course_dico.students,
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
                    'name': this.course_dico.name,
                    'teacher': this.course_dico.teacher,
                    'grade': this.course_dico.grade,
                    'students': this.course_dico.students,
                }
                for (var key in form_data) {
                    var html_field = document.createElement('input')
                    html_field.setAttribute('type', 'hidden')
                    html_field.setAttribute('name', key)
                    html_field.setAttribute('value', form_data[key])
                    form.appendChild(html_field)
                }
                document.body.appendChild(form);
                form.submit()
            },
      submit_form_fetch() {
        this.form_error = []
        this.form_updated = ""
        let formData = new FormData()
        let form_data = {
          'csrfmiddlewaretoken': this.csrf_token,
          'name': this.course_name,
          'teacher': this.course_teacher,
          'grade': this.course_grade,
        }
        for (var key in form_data) {
          formData.append(key, form_data[key])
        }
        this.student_list.map(dic => formData.append('students', dic.id))
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
<style src="vue-multiselect/dist/vue-multiselect.css"></style>
