pipeline {
  agent {
    docker {
      image 'python:3'
      args '-p 8080:8080 -p 5000:5000'
    }
  }

  stages {
    stage('Pull Data') {
      steps {
        sh '''MODEL_FILE=backend/model_file
if [ -f "$MODEL_FILE" ]; then
    echo "$MODEL_FILE exists."
else 
    wget -O $MODEL_FILE https://infallible-boyd-e34277.netlify.app/model_file_complicated_no_stopwords
fi

BACKEND_FILE=backend/tweets.csv
if [ -f "$BACKEND_FILE" ]; then
    echo "$BACKEND_FILE exists."
else 
    wget -O $BACKEND_FILE https://infallible-boyd-e34277.netlify.app/tweets.csv
fi
'''
      }
    }

    stage('Archive data') {
      steps {
        archiveArtifacts 'backend/model_file'
        archiveArtifacts 'backend/tweets.csv'
      }
    }

    stage('Run integration & unit tests') {
      when {
        branch 'feature/*'
      }
      steps {
        sh 'python backend/test_integration.py'
      }
    }

  }
}