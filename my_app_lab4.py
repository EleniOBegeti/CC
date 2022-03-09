from flask import Flask, jsonify, json

with open('record.json') as f:
    all_records = json.load(f)

app = Flask(__name__)

@app.route('/records', methods=['GET'])
def get_all_records():
	return jsonify(all_records)

@app.route('/records/<bandname>', methods=['GET','DELETE'])
def get_albums_by_band(bandname):
    albums = [band['albums'] for band in all_records if band['name'] == bandname]
    if len(albums)==0:
        return jsonify({'error':'band name not found!'}), 404
    else:
        response = [album['title'] for album in albums[0]]
        return jsonify(response), 200
    

@app.route('/records/<bandname>/<albumtitle>', methods=['GET'])
def get_songs_by_band_and_album(bandname, albumtitle):
    albums = [band['albums'] for band in all_records if band['name'] == bandname]
    if len(albums)==0:
        return jsonify({'error':'band name not found!'}), 404      
    else:
        songs = [album['songs'] for album in albums[0] if album['title'] == albumtitle]
        if len(songs)==0:
            return jsonify({'error':'album title not found!'}), 404
        else:
            return jsonify(songs[0]), 200
    

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

