pipeline {
    agent any
    stages {

        stage('Setup') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Start AI Server') {
            steps {
                echo 'Starting AI Chatbot server...'
                bat '''
                REM Start Python server in a new window (non-blocking)
                start "" cmd /c python app.py
                REM Wait ~10 seconds for server to start using ping
                ping 127.0.0.1 -n 10 > nul
                '''
            }
        }

        stage('Call AI Chatbot') {
            steps {
                echo 'Calling AI DevOps Chatbot...'
                bat '''
                curl "http://127.0.0.1:8000/chat?query=jenkins%20build%20failed"
                '''
            }
        }
    }
}
