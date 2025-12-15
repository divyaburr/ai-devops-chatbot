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
                '''
            }
        }

        stage('Wait for AI Server') {
            steps {
                echo 'Waiting for AI server to be ready...'
                bat '''
                REM Try connecting up to 10 times, wait 2 seconds between attempts
                set SERVER_UP=0
                for /L %%i in (1,1,10) do (
                    curl -s http://127.0.0.1:8000/chat?query=ping && set SERVER_UP=1 && goto :ready
                    ping 127.0.0.1 -n 3 > nul
                )
                :ready
                if "%SERVER_UP%"=="0" (
                    echo Server did not start in time
                    exit /b 1
                )
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
