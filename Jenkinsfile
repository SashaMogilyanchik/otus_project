pipeline {
    agent any

    environment {
        HEADLESS = 'true'
        PYTHONIOENCODING = 'UTF-8'
        ALLURE_VERSION = '2.30.0'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                bat '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('API Tests') {
            steps {
                bat 'pytest tests/api -m api --alluredir=reports/allure-results --clean-alluredir'
            }
        }

        stage('UI Tests') {
            steps {
                bat 'pytest tests/ui -m ui --alluredir=reports/allure-results'
            }
        }
    }

    post {
        always {
            powershell '''
                $ErrorActionPreference = "Stop"

                $resultsDir = Join-Path $env:WORKSPACE "reports/allure-results"
                if (-not (Test-Path $resultsDir)) {
                    Write-Host "No Allure results found, skipping report generation."
                    exit 0
                }

                $toolsDir = Join-Path $env:WORKSPACE "tools"
                $allureHome = Join-Path $toolsDir "allure-$env:ALLURE_VERSION"
                $allureBat = Join-Path $allureHome "bin/allure.bat"

                if (-not (Test-Path $allureBat)) {
                    New-Item -ItemType Directory -Force -Path $toolsDir | Out-Null
                    $zip = Join-Path $toolsDir "allure.zip"
                    $uri = "https://github.com/allure-framework/allure2/releases/download/$env:ALLURE_VERSION/allure-$env:ALLURE_VERSION.zip"
                    Write-Host "Downloading Allure $env:ALLURE_VERSION from $uri"
                    Invoke-WebRequest -Uri $uri -OutFile $zip
                    Expand-Archive -Path $zip -DestinationPath $toolsDir -Force
                    Remove-Item $zip
                }

                $reportDir = Join-Path $env:WORKSPACE "reports/allure-report"
                & $allureBat generate $resultsDir -o $reportDir --clean --single-file
            '''
            archiveArtifacts artifacts: 'reports/allure-report/index.html', allowEmptyArchive: true
        }
    }
}
