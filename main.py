from flask import Flask,request
from packets.SwaggerApi import blueprint as swaggerBlueprint
from packets.Database import engine as engine
from packets.Database import models as models
app = Flask(__name__)
app.config.setdefault("RESTX_MASK_SWAGGER",False)

app.register_blueprint(swaggerBlueprint)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

if __name__ == "__main__":
    app.run()