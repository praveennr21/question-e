from flask import Flask,jsonify
from datetime import datetime
from dateutil.tz import tzlocal
import pytz

app = Flask(__name__)

@app.route('/date', methods=['GET'])
def get_date():
    
    date = datetime.now(tzlocal())
    return jsonify({'date': date.strftime("%a %b %d %H:%M:%S %Z %Y")})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
