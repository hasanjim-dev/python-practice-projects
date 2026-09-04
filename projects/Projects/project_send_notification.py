from plyer import notification

notification.notify(
    title="Learning Time",
    message="Hello Hasan It's Time To Learn",
    app_name="Python App",
    timeout=5
)

notification.notify(
    title="Gaming Play Time",
    message="Hello Hasan It's Time To Play New Game",
    app_name="python App",
    timeout=10
)

print("✅ Notifications sent successfully!")