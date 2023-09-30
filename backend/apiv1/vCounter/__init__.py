import logging

import azure.functions as func

def main(req: func.HttpRequest, docIn: func.DocumentList, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    for value in docIn:
        if value["id"] == "1":
            counter = value["counter"]
    counter+=1
    newdocs = func.DocumentList() 
    newproduct_dict = {
        "id": "1",
        "counter": counter
    }
    newdocs.append(func.Document.from_dict(newproduct_dict))
    doc.set(newdocs)

    for value1 in docIn:
        if value1["id"] == "1":
            counter = value1["counter"]

    return func.HttpResponse(f"Hello, you are visitor number {counter}. This HTTP triggered function executed successfully.")
