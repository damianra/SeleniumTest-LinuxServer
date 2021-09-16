from flask_restful import Resource, reqparse
from flask import jsonify, request
from view.scrap_carrefour import carr_scrap


class CarrefourScrap(Resource):
    # POST method 
    def post(self):
        links = request.json['links_data']

        context = carr_scrap()

        return jsonify(context)
