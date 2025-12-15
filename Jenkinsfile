pipeline {
    agent any

    environment {
        PYTHON = "python"
        OPENAI_API_KEY = credentials('OPENAI_API_KEY')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                echo 'Installing Python dependencies...'
                bat '''
                %PYTHON% -m pip install --upgrade pip
                %PYTHON% -m pip install -r requirements.txt
                '''
            }
        }

        stage('Start AI Server') {
            steps {
                echo 'Starting FastAPI server...'
                bat '''
                REM Kill any process using port 8000
                for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do taskkill /PID %%a /F

                REM Start uvicorn in background and log output
                start "AI_SERVER" cmd /c "%PYTHON% -m uvicorn app:app --host 127.0.0.1 --port 8000 --log-level info > server.log 2>&1"
                '''
            }
        }

        stage('Wait for Server') {
            steps {
                echo 'Waiting for AI server to become ready...'
                bat '''
                set SERVER_UP=0
                for /L %%i in (1,1,15) do (
                    curl -s http://127.0.0.1:8000/health && set SERVER_UP=1 && goto :ready
                    ping 127.0.0.1 -n 3 > nul
                )
                :ready
                if "%SERVER_UP%"=="0" (
                    echo Server did not start
                    type server.log
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

    post {
        always {
            echo 'Pipeline completed'
            bat 'type server.log || echo No server log'
        }
    }
}
