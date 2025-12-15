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
                REM Start Python server in a new window without blocking
                start "" cmd /c python app.py
                REM Give it a few seconds to start
                timeout /t 10
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
