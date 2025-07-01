resource "aws_redshiftserverless_namespace" "rs_ns" {
  namespace_name = "sales_namespace"
  admin_username = "admin"
  admin_user_password = "RedshiftP@ss123"
}

resource "aws_redshiftserverless_workgroup" "rs_workgroup" {
  workgroup_name = "sales_workgroup"
  namespace_name = aws_redshiftserverless_namespace.rs_ns.namespace_name
  publicly_accessible = true
  iam_roles = [aws_iam_role.redshift_role.arn]
}