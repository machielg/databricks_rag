"""Data ingestion task."""

from pyspark.sql import SparkSession


def main():
    """Main ingestion task entry point."""
    spark = SparkSession.builder.appName("DB-RAG-Ingest").getOrCreate()
    
    # TODO: Implement data ingestion logic
    print("Starting data ingestion...")
    
    spark.stop()


if __name__ == "__main__":
    main()