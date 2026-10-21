
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Test HTML Form') {
            steps {
                echo 'Running automated HTML form tests...'
                sh 'python3 -m unittest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed.'
        }
        failure {
            echo 'FAILURE: Pipeline or HTML form tests failed.'
        }
    }
}
