# Reddit Data Engineering Pipeline

An ETL pipeline that extracts data from Reddit, processes it through AWS services, and loads it into a data warehouse. Built to learn modern data engineering practices and cloud technologies.

## 📋 Overview

This project implements an automated data pipeline that:

- Extracts Reddit posts and comments using Reddit's REST API
- Orchestrates workflows with Apache Airflow
- Stores raw data in Amazon S3
- Transforms data using AWS Glue and Athena
- Loads processed data into Redshift for analytics

**Note:** This implementation uses Reddit's direct API endpoints instead of the PRAW library since API tokens weren't available during development.

## 🏗️ Architecture

```
![alt text](assets/image.png)
```

## 🛠️ Tech Stack

- **Python 3.9+** - Core programming language
- **Apache Airflow** - Workflow orchestration
- **Celery** - Distributed task queue
- **PostgreSQL** - Airflow metadata storage
- **Docker & Docker Compose** - Containerization
- **AWS S3** - Data lake storage
- **AWS Glue** - Data catalog
- **Amazon Athena** - Query engine
- **Amazon Redshift** - Data warehouse
- **Reddit REST API** - Data source

## 🚀 Setup

### Prerequisites

- Docker Desktop
- Python 3.9+
- AWS Account
- Reddit Account

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/zainanis/reddit_datapipeline.git
cd reddit_datapipeline
```

2. **Configure credentials**

```bash
cp config/example.config.conf config/config.conf
mkdir logs data/output
```

Edit `config/config.conf` with your credentials:

```ini

[aws]
aws_access_key_id = your_key
aws_secret_access_key = your_secret
aws_region = us-east-1
aws_bucket_name = your-bucket

```

3. **Set up AWS resources**

   - Create S3 bucket
   - Configure IAM user with S3, Glue, Athena, Redshift permissions
   - Create Redshift cluster (optional for testing)

4. **Start services**

```bash
docker-compose up -d --build
```

4. **Initialize Airflow**

```bash
docker-compose up airflow-init
```

7. **Access Airflow**
   - URL: http://localhost:8080
   - Username: `admin`
   - Password: `admin`

## 📁 Project Structure

```
├── dags/                  # Airflow DAG definitions
├── pipelines/             # Data extraction logic
│   ├── reddit_pipeline_v02.py
│   └── upload_s3_pipeline.py
├── etls/                  # ETL transformations
│   ├── reddit_etl.py
│   └── aws_etl.py
├── config/                # Configuration files
├── docker-compose.yml     # Docker services
├── Dockerfile
└── requirements.txt       # Python dependencies
```

## 🔄 Pipeline Flow

1. **Extract**: Airflow triggers scheduled job to fetch Reddit data via API
2. **Store**: Raw JSON data uploaded to S3 bucket
3. **Catalog**: AWS Glue crawler scans and catalogs S3 data
4. **Transform**: Athena queries clean and structure the data
5. **Load**: Transformed data loaded into Redshift tables
6. **Automate**: Pipeline runs on defined schedule

## 🎯 Key Features

- Automated data extraction on schedule
- Scalable cloud storage with S3
- Serverless data transformation
- Containerized deployment
- Monitoring via Airflow UI
- Modular and extensible codebase

## 📚 What I Learned

- Building end-to-end ETL pipelines
- Workflow orchestration with Airflow
- AWS data services (S3, Glue, Athena, Redshift)
- Docker containerization
- REST API integration
- Data warehouse design

## 🙏 Acknowledgments

This project is a recreation of [airscholar/RedditDataEngineering](https://github.com/airscholar/RedditDataEngineering) for learning purposes.

## 📄 License

MIT License - Free to use for educational purposes.
