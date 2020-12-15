pipeline {
  agent any

  stages {
    stage('Pull Data') {
      steps {
        powershell '''
cp C:/Users/Florian/Documents/de-project-2/backend/model_file_complicated_no_stopwords ./backend/model_file
cp C:/Users/Florian/Documents/de-project-2/backend/tweets.csv ./backend/tweets.csv
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
        branch 'feature*'
      }
      steps {
        powershell '''
C:/Users/Florian/AppData/Local/Programs/Python/Python39/python.exe -m pip install -r requirements.txt
C:/Users/Florian/AppData/Local/Programs/Python/Python39/python.exe backend/test_integration.py
'''
      }
    }

  }
}