pipeline {
    agent any
    stages {

        stage('Setup') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Start AI Server') {
            steps {
                bat '''
                echo Starting AI Chatbot...
                start /B python app.py
                timeout /t 5
                '''
            }
        }

        stage('Call AI Chatbot') {
            steps {
                bat '''
                echo Calling AI DevOps Chatbot...
                curl "http://127.0.0.1:8000/chat?query=jenkins%20build%20failed"
                '''
            }
        }
    }
}
