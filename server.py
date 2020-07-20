from app import create_app, config, db

app = create_app(config.DevConfig)


# remove during production
if __name__ == "__main__":
    app.run(debug=True)
    # socketio.run(app, debug=True)