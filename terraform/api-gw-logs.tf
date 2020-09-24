resource "aws_cloudwatch_log_group" "shipit_text_summarizer_api_access_logs" {
  name = "/shipit_text_summarizer_api/api_gw_access"
}
