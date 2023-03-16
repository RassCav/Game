pipeline {
    agent any
    triggers {
      pollSCM '*/5 * * * *'
    }
    options {
        timeout(time: 10, unit: 'MINUTES') 
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RassCav/Game.git']])
            }
        }
        stage('Build') {
            steps {
              pip install requirements.txt
              sh 'python dices.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
        
    }
    post {
        always {
                slackSend channel: 'dices', message: "Hello HAMZA SIAD  your project status is ${currentBuild.currentResult}"
                }
        }
}
