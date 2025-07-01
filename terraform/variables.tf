variable "region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "s3_bucket" {
  description = "S3 bucket for data lake"
  type        = string
  default     = "sales-data-lake"
}