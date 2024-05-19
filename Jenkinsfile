pipeline {
agent any
options { skipDefaultCheckout() }   
stages {
    stage('CleanWorkspace') {
        steps {
            cleanWs()
            }
        }
    stage("Code Checkout from Github") {
        steps {
            git branch: 'main',
            credentialsId: 'GitHub',
            url: 'git@github.com:Ashok7867/devops-python-assignment.git'
                }
            }
    stage('Build') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python3 app.py &> /dev/null &'
            }
        }
    stage('Code Analysis') {
            environment {
                scannerHome = tool 'Sonar'
            }
            steps {
                script {
                    withSonarQubeEnv('Sonar') {
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=python-sample-app \
                            -Dsonar.projectName=python-sample-app \
                            -Dsonar.projectVersion=1.0 \
                            -Dsonar.sources=."
                    }
                }
            }
        }
    }
}
