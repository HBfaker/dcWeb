from ..models import Document
from app import db


def getDoucumentByID(did):
    return db.session.query(Document).filter(Document.id == did).one()


def getDocumentByPage(page_index, per_page,type):
    pagination = Document.query.order_by(Document.created_time.desc()).paginate(page_index, per_page)
    documents = pagination.items
    return pagination,documents

