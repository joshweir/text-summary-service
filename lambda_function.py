import requests
import json
import traceback
import nltk

from sumy_service import SumyService
sumy_service = SumyService()

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

  if "sentences" not in body:
    return {
      "ok": False,
      "error": "input 'sentences' must be integer > 0, got input: {0}".format(event["body"]),
      "parsed": body
    }

  if not isinstance(body["sentences"], int) or body["sentences"] <= 0:
    return {
      "ok": False,
      "error": "input 'sentences' must be integer > 0, got input: {0}".format(event["body"]),
      "parsed": body
    }

  return {
    "ok": is_ok,
    "error": error_message,
    "parsed": body
  }

def lambda_handler(event, context):
  try:
    nltk.data.path.append("/tmp")
    nltk.data.find('tokenizers/punkt')
  except LookupError:
    print('downloading punkt..')
    nltk.download('punkt', download_dir = '/tmp')
    print('done downloading punkt')

  parsed_input = validate_input(event)
  if not parsed_input["ok"]:
    return {
      "statusCode": 500,
      "headers": {},
      "body": parsed_input["error"],
      "isBase64Encoded": False
    }
 
  try:
    sumy_service_result = sumy_service.call(parsed_input["parsed"]["text"], parsed_input["parsed"]["sentences"])
  except Exception: 
    error_message = traceback.format_exc()
    print('error occurred:', error_message)
    return {
      "statusCode": 500,
      "headers": {},
      "body": error_message,
      "isBase64Encoded": False
    }

  return {
    "statusCode": 200,
    "headers": {},
    "body": json.dumps(sumy_service_result),
    "isBase64Encoded": False
  }


if __name__ == '__main__':
  result = lambda_handler(
    json.dumps({}),
    json.dumps({})
  )
  print('result:', result)
