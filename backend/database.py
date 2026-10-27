import os
import uuid
from datetime import datetime, timezone

import boto3

dynamodb = boto3.resource("dynamodb")

complaints = dynamodb.Table(os.environ["COMPLAINTS_TABLE"])
sessions = dynamodb.Table(os.environ["SESSIONS_TABLE"])


def init_db():
    # DynamoDB tables are created in the AWS Console.
    pass


def get_history(user_id):
    response = sessions.get_item(
        Key={"user_id": user_id}
    )
    return response.get("Item", {}).get("history", "")


def save_history(user_id, history):
    sessions.put_item(
        Item={
            "user_id": user_id,
            "history": history
        }
    )


def save_complaint(
    user_id,
    message,
    ai_response,
    is_escalated=False,
    refund_issued=False
):
    negative_words = [
        "bad", "cold", "late", "angry", "burnt"
    ]

    sentiment = (
        "Negative"
        if any(word in message.lower() for word in negative_words)
        else "Neutral"
    )

    complaints.put_item(
        Item={
            "complaint_id": str(uuid.uuid4()),
            "user_id": user_id,
            "message": message,
            "ai_response": ai_response,
            "sentiment": sentiment,
            "is_escalated": bool(is_escalated),
            "refund_issued": bool(refund_issued),
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }
    )
