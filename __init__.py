from app_config import app
from controller import blue_prints
from flask import redirect, url_for

for bp in blue_prints:
    app.register_blueprint(bp[0], url_prefix=bp[1])


@app.route('/')
def hello_world():
    return "<script>location.href='/bank'</script>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
