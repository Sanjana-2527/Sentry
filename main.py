

from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


app = Flask(__name__)

sentry_sdk.init(
    dsn="https://4ff8d4d35f22485291c0fc3281c90631@o1144295.ingest.sentry.io/6208282",
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

if __name__ == "__main__":
    app.run()
