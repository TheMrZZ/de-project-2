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

    stage('Install requirements') {
      steps {
        powershell 'C:/Users/Florian/AppData/Local/Programs/Python/Python38/python.exe -m pip install -r requirements.txt'
      }
    }

    stage('Run integration & unit tests') {
      when {
        branch 'feature*'
      }
      steps {
        powershell 'C:/Users/Florian/AppData/Local/Programs/Python/Python38/python.exe backend/test_integration.py'
        powershell 'C:/Users/Florian/AppData/Local/Programs/Python/Python38/python.exe backend/test_unit.py'
      }
    }

    stage('Run stress test') {
      when {
        branch 'develop'
      }

      steps {
        powershell 'C:/Users/Florian/AppData/Local/Programs/Python/Python38/python.exe backend/test_stress.py'
      }
    }

    stage('Push on main') {
      when {
        branch 'develop'
      }

      steps {
        powershell 'git fetch --all'
        powershell 'git checkout -b main'
        powershell 'git pull'
        powershell 'git merge origin/develop'
        powershell 'git push origin main'
      }
    }
  }
}