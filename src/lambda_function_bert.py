import requests
import json
import traceback

import hfapi
from sb_email_text_parser import SbEmailTextParser

def validate_input(event):
  print('input event:', event)
  body = json.loads(event["body"])
  print('parsed body:', body)

  is_ok = True
  error_message = ""

  if "text" not in body:
    return {
      "ok": False,
      "error": "input 'text' is required, got input: {0}".format(event["body"]),
      "parsed": body
    }

  if len(body["text"]) <= 0:
    return {
      "ok": False,
      "error": "input 'text' is required, got input: {0}".format(event["body"]),
      "parsed": body
    }

  return {
    "ok": is_ok,
    "error": error_message,
    "parsed": body
  }

def lambda_handler(event, context):
  parsed_input = validate_input(event)
  if not parsed_input["ok"]:
    return {
      "statusCode": 500,
      "headers": {
        "Access-Control-Allow-Origin": "*",
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      "body": parsed_input["error"],
      "isBase64Encoded": False
    }
 
  try:
    client = hfapi.Client()
    email_text_parser = SbEmailTextParser()
    parsed_text = email_text_parser(parsed_input["parsed"]["text"]).replace('\r', '')
    print('sending text to summarizer:', json.dumps(parsed_text))
    summarization_result = client.summarization(
      parsed_text,
      model="sshleifer/distilbart-cnn-12-6"
    )
    print('got result: ', summarization_result)
    service_result = {
      'result': [
        summarization_result[0]['summary_text']
      ]
    }

  except Exception: 
    error_message = traceback.format_exc()
    print('error occurred:', error_message)
    return {
      "statusCode": 500,
      "headers": {
        "Access-Control-Allow-Origin": "*",
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      "body": error_message,
      "isBase64Encoded": False
    }

  return {
    "statusCode": 200,
    "headers": {
      "Access-Control-Allow-Origin": "*",
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    },
    "body": json.dumps(service_result),
    "isBase64Encoded": False
  }


if __name__ == '__main__':
  result = lambda_handler(
    json.dumps({}),
    json.dumps({})
  )
  print('result:', result)
