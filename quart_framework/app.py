from quart import Quart
from quart_motor import Motor

app  =Quart(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/free5gc"
mongo = Motor(app)

@app.get("/")
async def index():
    return "hello"

# if __name__ == "__main__":
#     app.run()