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

# Load data from Glue Catalog
dyf_orders = glueContext.create_dynamic_frame.from_catalog(
    database="sales_db",
    table_name="orders"
)

# Data cleaning and transformation
dyf_cleaned = dyf_orders.drop_fields(["unnecessary_column"])     .rename_field("cust_id", "customer_id")     .rename_field("amt", "order_value")     .resolveChoice(specs=[('order_value', 'cast:double')])

# Write the cleaned data back to S3 in Parquet format
glueContext.write_dynamic_frame.from_options(
    frame=dyf_cleaned,
    connection_type="s3",
    connection_options={"path": "s3://sales-data-lake/processed/orders/"},
    format="parquet"
)

job.commit()
