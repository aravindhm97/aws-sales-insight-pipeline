import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load raw transactions from Glue Catalog
dyf_raw = glueContext.create_dynamic_frame.from_catalog(
    database="sales_db",
    table_name="transactions"
)

# Transformations
dyf_transformed = dyf_raw \
    .rename_field("created_at", "transaction_time") \
    .resolveChoice(specs=[
        ("promo_amount", "cast:int"),
        ("shipment_fee", "cast:int"),
        ("total_amount", "cast:double")
    ]) \
    .drop_fields(["payment_status"])  # Assuming all are 'Success' as per the sample

# Write to S3 in Parquet format
glueContext.write_dynamic_frame.from_options(
    frame=dyf_transformed,
    connection_type="s3",
    connection_options={"path": "s3://sales-data-lake/processed/transactions/"},
    format="parquet"
)

job.commit()
