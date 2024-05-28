<template>
here
    <div>
        This is the form coming from django, displayed in vue. <br><br>
    </div>

    With fetch this time

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
