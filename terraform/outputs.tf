output "api_url" {
  value = "${aws_api_gateway_deployment.shipit_text_summarizer_api_apig_deployment.invoke_url}"
}

output "summarizer_url" {
  value = "${aws_lambda_function.text_summarizer_lambda.invoke_arn}"
}
