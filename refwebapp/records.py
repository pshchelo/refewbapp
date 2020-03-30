import json
import logging

import falcon

from .models import Record

LOG = logging.getLogger(__name__)


class RecordResourceCollection:
    def on_get(self, req, resp):
        LOG.debug("Listing Records ...")
        result = req.context.session.query(Record).all()
        LOG.info(f"Got {len(list(result))} Records")
        resp.body = json.dumps(dict(records=list(r.to_dict() for r in result)))

    def on_post(self, req, resp):
        LOG.debug("Creating Record ...")
        new_rec = Record()
        req.context.session.add(new_rec)
        LOG.debug("Committing Record ...")
        req.context.session.commit()
        LOG.info(f"Created record {new_rec.id} with data {new_rec.data}")
        resp.body = json.dumps(new_rec.to_dict())


class RecordResource:
    def on_get(self, req, resp, id):
        LOG.debug(f"Accessing Record {id} ...")
        result = req.context.session.query(Record).get(id)
        if result:
            resp.body = json.dumps(result.to_dict())
        else:
            LOG.info("No Record with id {id} found")
            resp.status = falcon.HTTP_404
