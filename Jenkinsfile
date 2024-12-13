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
                            sh "docker build -t devopsuses/mycategories-service:${env.DOCKER_TAG} ."
                            sh "docker push devopsuses/mycategories-service:${env.DOCKER_TAG}"
                    }
                }
            }
        }
        stage('Clone and Update k8-manifest.yml') {
            steps {
                script {
                    // Check if the directory exists and delete if it does
                    if (fileExists('python-microservice-CD')) {
                        sh 'rm -rf python-microservice-CD'
                    }

                    // Clone the repository securely using HTTPS
                    withCredentials([usernamePassword(credentialsId: 'github-cred', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
                        sh 'git clone https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/devopsusesl/python-microservice-CD.git'
                        sh 'pwd'
                        sh 'ls -a'
                    }

                    // Update trending.yaml with the new Docker tag using sed
                    dir('python-microservice-CD') {
                        sh "sed -i 's|image: devopsuses/mycategories-service:.*|image: devopsuses/mycategories-service:${env.DOCKER_TAG}|g' application/K8/CANARY-DEPLOYMENT-WITH-ARGO-ISTIO/my-categories.yaml"

                        // Configure Git user and commit the changes
                        sh 'git config user.name "devopsusesl"'
                        sh 'git config user.email "devopsuse@gmail.com"'
                        sh 'git add application/K8/CANARY-DEPLOYMENT-WITH-ARGO-ISTIO/my-categories.yaml'
                        sh "git commit -m 'Updated Docker image tag to ${env.DOCKER_TAG}'"

                        // Push the changes back to the repository using credentials
                        withCredentials([usernamePassword(credentialsId: 'github-cred', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
                            sh 'git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/devopsusesl/python-microservice-CD.git'
                        }
                    }
                }
            }
        }
        
    }
}

