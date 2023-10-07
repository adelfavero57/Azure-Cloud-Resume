import logging
import json
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
            outputValue = value1["counter"]
    print()
    outputDict = {
        "id": "1",
        "counter": outputValue
    }

    return func.HttpResponse(
            json.dumps(outputDict),
            mimetype="application/json",
        )