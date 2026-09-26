import random
import time
import datetime

def process_refund(payment_id, amount):
    """
    FAKE refund function - does not connect to real Razorpay.
    Only mimics a real API response, for testing purposes.
    """
    print(f"Processing refund for payment: {payment_id}, amount: {amount}")

    time.sleep(1)  # simulate real API taking some time

    fake_refund_id = "rfnd_" + str(random.randint(100000, 999999))

    return {
        "id": fake_refund_id,
        "payment_id": payment_id,
        "amount": amount,
        "status": "processed"
    }


def check_payment_status(payment_id):
    """
    FAKE payment status checker - does not connect to real Razorpay.
    """
    statuses = ["captured", "failed", "pending"]
    status = random.choice(statuses)

    return {
        "payment_id": payment_id,
        "status": status,
        "amount": random.randint(100, 5000)
    }


def create_support_ticket(issue, customer_email):
    """
    FAKE ticket creation - saves to a text file (a real system would save to a DB/CRM).
    """
    ticket_id = "TICKET-" + str(random.randint(1000, 9999))

    with open("tickets.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now()}] {ticket_id} | {customer_email} | {issue}\n")

    return {
        "ticket_id": ticket_id,
        "status": "created"
    }


if __name__ == "__main__":
    result = process_refund("pay_12345", 500)
    print(result)