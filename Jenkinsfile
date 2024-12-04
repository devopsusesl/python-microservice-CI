pipeline {
    agent any

    stages {
        stage('tag docker image') {
            steps {
                echo 'tag docker image'
                script {
                    def dockerTagInput = input(
                        id: 'userInput', message: 'Enter Docker Tag', parameters: [
                            string(name: 'DOCKER_TAG', defaultValue: 'latest', description: 'Docker Tag')
                        ]
                    )
                    env.DOCKER_TAG = dockerTagInput
                }
            }
        }
        stage('build & push docker image') {
            steps {
                echo 'build & push docker image'
                script {
                        withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker') {
                            sh "docker build -t devopsuses/myfrontend:${env.DOCKER_TAG} ."
                            sh "docker push devopsuses/myfrontend:${env.DOCKER_TAG}"
                    }
                }
            }
        }
        
    }
}
