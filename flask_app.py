from flask import Flask, render_template, request, redirect, Response
from models import MatchModel
from Constants import *
from utils import *
import json

app = Flask(__name__)

@app.route("/api/matches/<match_id>", methods=['GET'])
def match_data(match_id: str):
  if match_id == "c8d8bc50-c030-4abf-a27e-66b1c157429c":
    match_data = json.loads(open("example_split_game.json").read())
  match: MatchModel = MatchModel(match_data)
  return {"players": match.get_players(), "kill_data": match.duel_data, "map_details": MAP[match.get_map()]}

@app.route("/api/utils/filter", methods=['POST'])
def get_filtered_data():
  kill_data = request.get_json()["kill_data"]
  options = request.get_json()["options"]
  return { "data": filter_data(kill_data, options) }

@app.route("/api/utils/plot", methods=['POST'])
def get_plotted_image():
  kills = request.get_json()["data"]
  map_details = request.get_json()["map_details"]
  return plot_image(kills, map_details)

if __name__ == "__main__":
  port = 5000
  app.run(port=port, debug=True)