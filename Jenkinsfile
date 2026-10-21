
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Source code retrieved from GitHub.'
                checkout scm
            }
        }

        stage('Test HTML Form') {
            steps {
                echo 'Running automated HTML form tests...'
                bat '"C:\\Users\\ankit\\anaconda3\\python.exe" -m unittest -v test_form.py'
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
