import json
import uuid

def lambda_handler(event, context):
    body = json.loads(event.get("body") or "{}")
    student_id = body.get("studentId")
    answers = body.get("answers", [])

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "attemptId": str(uuid.uuid4()),
            "message": "Responses recorded",
            "answersReceived": len(answers)
        })
    }
