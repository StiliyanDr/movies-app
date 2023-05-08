import os

from frontendapp.app import create_app


if __name__ == "__main__":
    do_debug = os.environ.get("DEBUG").lower() == "true"
    host = os.environ.get("DASH_HOST", "localhost")
    port = int(os.environ.get("DASH_PORT", 8080))

    app = create_app()
    app.run_server(debug=do_debug, host=host, port=port)
