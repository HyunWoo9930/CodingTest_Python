import mido
import sys
import json

def extract_instrument_names(file_path):
    try:
        midi_file = mido.MidiFile(file_path)
        instrument_names = {}

        for i, track in enumerate(midi_file.tracks):
            for msg in track:
                if msg.type == 'instrument_name':
                    instrument_names[i] = msg.name

        return {"instrument_names": instrument_names}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "MIDI file path not provided"}))
        sys.exit(1)

    midi_file_path = sys.argv[1]
    result = extract_instrument_names(midi_file_path)
    print(json.dumps(result))
