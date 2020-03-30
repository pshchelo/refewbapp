import logging

from sqlalchemy import create_engine
import falcon
import falcon_sqla

from . import models
from . import records
from . import root

db_engine = create_engine("sqlite://")
models.init(db_engine)
sa_manager = falcon_sqla.Manager(db_engine)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s:%(lineno)d -> %(message)s",
)


def create_app():
    app = falcon.API(middleware=[sa_manager.middleware],)
    app.add_route("/", root.RootResource())
    app.add_route("/records", records.RecordResourceCollection())
    app.add_route("/records/{id}", records.RecordResource())
    return app
