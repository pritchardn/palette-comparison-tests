"""
Some preliminary tests around building signatures for DALiuGE palettes
@author Nicholas Pritchard
"""
import json

from blockdag import build_block_dag, compare_dags


def load_palette(filename: str) -> dict:
    with open(filename, "r", encoding="utf-8") as ifile:
        return json.load(ifile)


def palette_vertices(loaded_palette: dict) -> dict:
    nodes = loaded_palette["nodeDataArray"]
    output = {}
    for i in range(len(nodes)):
        output[i] = nodes[i]
    return output


if __name__ == "__main__":
    palette = load_palette("DALiuGE Components.palette")
    print(json.dumps(palette, indent=4))

    vertices = palette_vertices(palette)

    data_fields = ["inputPorts", "outputPorts", "applicationArgs", "category", "fields"]
    original_signature = build_block_dag(vertices, [], data_fields=data_fields)
    print(json.dumps(original_signature, indent=4))
    # Make a change to a component
    vertices[0]["category"] = "banana-pie"
    new_signature = build_block_dag(vertices, [], data_fields=data_fields)
    print(
        f"original:\t{original_signature['signature']}\nnew:\t\t{new_signature['signature']}"
    )
    # Run provided comparison routine
    print(compare_dags(original_signature, new_signature))
