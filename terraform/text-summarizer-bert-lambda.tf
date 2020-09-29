resource "aws_lambda_function" "text_summarizer_bert_lambda" {
  filename      = "bundle.zip"
  source_code_hash = "${base64sha256(file("bundle.zip"))}"
  function_name = "shipit_text_summarizer_bert"
  role          = "${aws_iam_role.role_for_text_summarizer_bert_lambda.arn}"
  handler       = "lambda_function_bert.lambda_handler"
  runtime       = "python3.8"
  timeout       = "60"
  memory_size   = "3008"
  layers        = ["arn:aws:lambda:ap-southeast-2:888686886224:layer:text_summarizer:2"]
}

resource "aws_iam_role" "role_for_text_summarizer_bert_lambda" {
  name = "role_shipit_text_summarizer_bert"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

data "aws_iam_policy_document" "policy_for_text_summarizer_bert_lambda" {
  statement {
    sid = "CreateLogGroups"
    actions = ["logs:CreateLogGroup"]
    resources = ["arn:aws:logs:${var.aws_region}:${var.aws_account}:*"]
  }
  statement {
    sid = "CreateLogStreams"
    actions = ["logs:CreateLogStream", "logs:PutLogEvents"]
    resources = ["arn:aws:logs:${var.aws_region}:${var.aws_account}:log-group:/aws/lambda/${aws_lambda_function.text_summarizer_bert_lambda.function_name}:*"]
  }
  statement {
    sid = "EC2Interfaces"
    actions = ["ec2:CreateNetworkInterface","ec2:DescribeNetworkInterfaces","ec2:DetachNetworkInterface","ec2:DeleteNetworkInterface"]
    resources = ["*"]
  }
  statement {
    sid = "SelfInvoke"
    actions = ["lambda:InvokeFunction"]
    resources = [
      "${aws_lambda_function.text_summarizer_bert_lambda.arn}", "${aws_lambda_function.text_summarizer_bert_lambda.arn}:$LATEST"
    ]
  }
}

resource "aws_cloudwatch_log_group" "logging_for_text_summarizer_bert_lambda" {
  name = "/aws/lambda/${aws_lambda_function.text_summarizer_bert_lambda.function_name}"
}

resource "aws_iam_policy" "policy_for_text_summarizer_bert_lambda" {
  name = "policy_shipit_text_summarizer_bert"
  # role = "${aws_iam_role.role_for_text_summarizer_bert_lambda.id}"
  policy = "${data.aws_iam_policy_document.policy_for_text_summarizer_bert_lambda.json}"
}

resource "aws_iam_role_policy_attachment" "policy_for_text_summarizer_bert_lambda" {
  role       = "${aws_iam_role.role_for_text_summarizer_bert_lambda.name}"
  policy_arn = "${aws_iam_policy.policy_for_text_summarizer_bert_lambda.arn}"
}

resource "aws_lambda_permission" "allow_apig_call_api_bert_lambda" {
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.text_summarizer_bert_lambda.function_name}"
  principal     = "apigateway.amazonaws.com"
  source_arn    = "arn:aws:execute-api:${var.aws_region}:${var.aws_account}:${aws_api_gateway_rest_api.shipit_text_summarizer_api.id}/*/POST/public/*"
}
