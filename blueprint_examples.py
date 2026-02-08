#!/usr/bin/env python3
"""
Example script demonstrating how to use blueprint_decoder module
to programmatically manipulate Factorio blueprints.
"""

import sys
sys.path.insert(0, '/home/claude')
from blueprint_decoder import decode_blueprint, encode_blueprint
import json


def example_modify_decider():
    """
    Example: Decode a decider combinator blueprint and modify its settings.
    """
    # Original blueprint string
    original = "0eJyVUdtKxEAM/ZVlnl3Yrq6rPizob4gM0zargc6FTKZYSv/dTFrQBxF8muSc5OQkM5t2KJAIA5un3WywiyFL9DqbjO/BDYrylEACgwze3OxMcF7zHjrsgfZd9C0Gx5HMIjSGHj6Fb5Y3ySAwMsKmqtlkQ/EtUK35W07YFLP0x6BOquxBwKm+dVaPBN1GV0L8M8XBtvDhRoykXZuwFbJXrazwFSmz/WXPEYmLYD+8rVX7Z12wHomdnmyd6ZMj9SuVl9oWC6fyT+2XTTtNYrQEtleK3mIQIam6uiHDsuhJ9R+k8fvvBByB8nqH40Nzd348nk/Nqbm9PyzLF/gIndQ="
    
    print("Original Blueprint:")
    print(original)
    print()
    
    # Decode
    blueprint_data, version_byte = decode_blueprint(original)
    
    # Access and modify the decider combinator settings
    entity = blueprint_data['blueprint']['entities'][0]
    conditions = entity['control_behavior']['decider_conditions']
    
    print("Original Settings:")
    print(f"  Input: {conditions['first_signal']['name']}")
    print(f"  Comparator: {conditions['comparator']}")
    print(f"  Constant: {conditions['constant']}")
    print(f"  Output: {conditions['output_signal']['name']}")
    print()
    
    # Modify the settings
    conditions['first_signal']['name'] = 'signal-red'
    conditions['comparator'] = '<'
    conditions['constant'] = 50
    conditions['output_signal']['name'] = 'signal-green'
    
    print("Modified Settings:")
    print(f"  Input: {conditions['first_signal']['name']}")
    print(f"  Comparator: {conditions['comparator']}")
    print(f"  Constant: {conditions['constant']}")
    print(f"  Output: {conditions['output_signal']['name']}")
    print()
    
    # Re-encode
    modified_blueprint = encode_blueprint(blueprint_data, version_byte)
    
    print("Modified Blueprint:")
    print(modified_blueprint)
    print()
    
    return modified_blueprint


def example_add_multiple_combinators():
    """
    Example: Create a blueprint with multiple decider combinators.
    """
    blueprint_data = {
        "blueprint": {
            "icons": [
                {
                    "signal": {
                        "type": "item",
                        "name": "decider-combinator"
                    },
                    "index": 1
                }
            ],
            "entities": [],
            "item": "blueprint",
            "version": 281479275151360
        }
    }
    
    # Add 5 decider combinators in a row
    for i in range(5):
        combinator = {
            "entity_number": i + 1,
            "name": "decider-combinator",
            "position": {
                "x": i * 2,  # Space them 2 tiles apart
                "y": 0
            },
            "direction": 0,
            "control_behavior": {
                "decider_conditions": {
                    "first_signal": {
                        "type": "virtual",
                        "name": f"signal-{i}"
                    },
                    "constant": i * 10,
                    "comparator": ">",
                    "output_signal": {
                        "type": "virtual",
                        "name": "signal-each"
                    },
                    "copy_count_from_input": True
                }
            }
        }
        blueprint_data['blueprint']['entities'].append(combinator)
    
    # Encode
    blueprint_string = encode_blueprint(blueprint_data)
    
    print("Created blueprint with 5 decider combinators:")
    print(blueprint_string)
    print()
    
    return blueprint_string


def example_inspect_blueprint():
    """
    Example: Decode and inspect a blueprint's structure.
    """
    blueprint_string = "0eJyVUdtKxEAM/ZVlnl3Yrq6rPizob4gM0zargc6FTKZYSv/dTFrQBxF8muSc5OQkM5t2KJAIA5un3WywiyFL9DqbjO/BDYrylEACgwze3OxMcF7zHjrsgfZd9C0Gx5HMIjSGHj6Fb5Y3ySAwMsKmqtlkQ/EtUK35W07YFLP0x6BOquxBwKm+dVaPBN1GV0L8M8XBtvDhRoykXZuwFbJXrazwFSmz/WXPEYmLYD+8rVX7Z12wHomdnmyd6ZMj9SuVl9oWC6fyT+2XTTtNYrQEtleK3mIQIam6uiHDsuhJ9R+k8fvvBByB8nqH40Nzd348nk/Nqbm9PyzLF/gIndQ="
    
    blueprint_data, version_byte = decode_blueprint(blueprint_string)
    
    print("Blueprint Structure:")
    print(json.dumps(blueprint_data, indent=2))
    print()
    
    # Extract useful information
    entities = blueprint_data['blueprint']['entities']
    print(f"Number of entities: {len(entities)}")
    
    for i, entity in enumerate(entities):
        print(f"\nEntity {i+1}:")
        print(f"  Type: {entity['name']}")
        print(f"  Position: ({entity['position']['x']}, {entity['position']['y']})")
        
        if 'control_behavior' in entity:
            print(f"  Has control behavior: Yes")


if __name__ == "__main__":
    print("="*60)
    print("Example 1: Modify a decider combinator")
    print("="*60)
    example_modify_decider()
    
    print("\n" + "="*60)
    print("Example 2: Create multiple combinators")
    print("="*60)
    example_add_multiple_combinators()
    
    print("\n" + "="*60)
    print("Example 3: Inspect blueprint structure")
    print("="*60)
    example_inspect_blueprint()