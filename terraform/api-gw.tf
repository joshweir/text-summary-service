
resource "aws_api_gateway_deployment" "shipit_text_summarizer_api_apig_deployment" {
  rest_api_id       = "${aws_api_gateway_rest_api.shipit_text_summarizer_api.id}"
  stage_name        = "v1"
  stage_description = "${md5(file("api-gw.tf"))}"
  # variables {
  #   force_deploy = "${var.force_deploy}"
  # }
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_rest_api" "shipit_text_summarizer_api" {
  name        = "shipit_text_summarizer_api"
  description = "API gateway for shipit text summarizer"

  body = <<EOF
swagger: "2.0"
info:
  title: "shipit_text_summarizer_api"
  version: v1
schemes:
- "https"
paths:
  /public/text-summarizer:
    post:
      produces:
      - "application/json"
      responses:
        200:
          description: "200 response"
          schema:
            $ref: "#/definitions/Empty"
      x-amazon-apigateway-integration:
        uri: "arn:aws:apigateway:${var.aws_region}:lambda:path/2015-03-31/functions/${aws_lambda_function.text_summarizer_lambda.arn}/invocations"
        responses:
          default:
            statusCode: "200"
        passthroughBehavior: "when_no_match"
        httpMethod: "POST"
        contentHandling: "CONVERT_TO_TEXT"
        type: "aws_proxy"
  /public/text-summarizer-bert:
    post:
      produces:
      - "application/json"
      responses:
        200:
          description: "200 response"
          schema:
            $ref: "#/definitions/Empty"
      x-amazon-apigateway-integration:
        uri: "arn:aws:apigateway:${var.aws_region}:lambda:path/2015-03-31/functions/${aws_lambda_function.text_summarizer_bert_lambda.arn}/invocations"
        responses:
          default:
            statusCode: "200"
        passthroughBehavior: "when_no_match"
        httpMethod: "POST"
        contentHandling: "CONVERT_TO_TEXT"
        type: "aws_proxy"
definitions:
  Empty:
    type: "object"
    title: "Empty Schema"
EOF
}

resource "aws_api_gateway_method_settings" "shipit_text_summarizer_api_v1_settings" {
  rest_api_id = "${aws_api_gateway_rest_api.shipit_text_summarizer_api.id}"
  stage_name  = "v1"
  method_path = "*/*"

  settings {
    metrics_enabled = true
    logging_level   = "ERROR"
  }
}
