resource "aws_s3_bucket" "data_lake" {
  bucket = var.s3_bucket
  force_destroy = true
}