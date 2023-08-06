from typing import List
from pydantic import BaseModel

# TODO: response models once stable

class Document(BaseModel):
    # data can be
    # - a string - for example  "This is a document"
    # TODO: currently only string is supported (later could be images, audio, multi/cross-modal)
    # etc.
    data: str
    metadata: dict


class AddRequest(BaseModel):
    documents: List[Document]
    store_data: bool = True


class DeleteRequest(BaseModel):
    ids: List[str]


class SearchRequest(BaseModel):
    query: str
    top_k: int = 6
