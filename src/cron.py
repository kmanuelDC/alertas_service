from jobs.events_jobs import alerts_pre_config,generate_alerts
from flask import Flask

app = Flask(__name__)
#     generate_events_ms4m_critical,
#     generate_events_ms4m_normal
# )
# from notifications_jobs import generate_notifications, generate_notifications_cpu
# import time
# import threading

# def setup():
#     create_connection()

def run_jobs():
    # alerts_pre_config()
    with app.app_context():
     generate_alerts()
#     generate_events_ms4m_critical()
    # print('holis')


def main():
#     setup()
    run_jobs()

#     # Start the notifications job in a separate thread
#     notification_thread = threading.Thread(target=notification_job)
#     notification_thread.daemon = True
#     notification_thread.start()

#     generate_notifications_cpu()

if __name__ == "__main__":
    main()
