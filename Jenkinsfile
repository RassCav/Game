pipeline {
    agent any
    environment {
      dockerImage = ''
      registry = 'rascav/dicesApp'
    }
    triggers {
      pollSCM 'H/2 * * * *'
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
              sh 'pip install -r requirements.txt'
              sh 'python dices.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
        stage('Build Docker Image') {
            steps {
               script {
                  dockerImage = docker.build registry
               }
            }
        }
        
    }
    post {
        always {
                slackSend channel: 'dices', message: "Hello HAMZA SIAD  your project status is ${currentBuild.currentResult}"
                }
        }
}
