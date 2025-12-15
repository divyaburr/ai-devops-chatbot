pipeline {
    agent any

    stages {
        stage('AI DevOps Support') {
            steps {
                bat '''
                  echo Calling AI DevOps Chatbot...
                  curl "http://localhost:8000/chat?query=jenkins build failed"
                '''
            }
        }
    }
}
