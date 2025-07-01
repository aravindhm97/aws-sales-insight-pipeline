resource "aws_athena_workgroup" "analytics" {
  name = "sales_analytics"
  configuration {
    result_configuration {
      output_location = "s3://${var.s3_bucket}/athena-results/"
    }
  }
  state = "ENABLED"
  force_destroy = true
}