output "bucket_name" {
  value = aws_s3_bucket.data_lake.bucket
}

output "glue_role_arn" {
  value = aws_iam_role.glue_role.arn
}

output "redshift_workgroup_name" {
  value = aws_redshiftserverless_workgroup.rs_workgroup.workgroup_name
}