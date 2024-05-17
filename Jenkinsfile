pipeline {
agent any
stages {
 stage("Code Checkout from Github") {
  steps {
   git branch: 'main',
    credentialsId: 'GitHub',
    url: 'git@github.com:Ashok7867/devops-python-assignment.git'
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
