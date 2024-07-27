from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

# HTML template with input field for user identification
html_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Log User Identification</title>
  </head>
  <body>
    <h1>Log User Identification</h1>
    <form action="/log_id" method="post">
      <label for="user_id">Enter your ID:</label>
      <input type="text" id="user_id" name="user_id" required>
      <button type="submit">Log ID</button>
    </form>
  </body>
</html>
'''

# Route for the main page
@app.route('/')
def index():
    return render_template_string(html_template)

# Route to log the user identification
@app.route('/log_id', methods=['POST'])
def log_id():
    user_id = request.form['user_id']
    log_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Write to log file
    log_entry = f'User ID: {user_id}, Time: {log_time}\n'
    with open('id_log.txt', 'a') as log_file:
        log_file.write(log_entry)

    return 'User ID logged successfully!'

if __name__ == '__main__':
    app.run(host='172.16.128.100', port=5000, debug=True)
