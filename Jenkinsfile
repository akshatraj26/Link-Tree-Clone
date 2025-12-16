pipeline {
    agent any 
    
    stages {
        stage("Pull code from git hub") {
            steps{
                git url: "https://github.com/akshatraj26/Link-Tree-Clone.git", branch: "main"
            }
        }
        stage("Build & Test your application"){
            steps{
                sh "docker build -t link-tree ."
            }
        }
        stage("Deploy you application on jenkins"){
            steps{
                sh "docker compose up -d"
            }
        }
    }
}