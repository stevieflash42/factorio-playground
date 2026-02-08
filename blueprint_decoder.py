#!/usr/bin/env python3
"""
Script to decode and expand Factorio blueprint strings.
Takes a blueprint string and converts it to readable/editable JSON format.
Can also re-encode modified blueprints back to blueprint strings.
"""

import json
import zlib
import base64
import sys


def decode_blueprint(blueprint_string):
    """
    Decodes a Factorio blueprint string into a Python dictionary.
    
    Args:
        blueprint_string: The encoded blueprint string from Factorio
        
    Returns:
        dict: The decoded blueprint data
    """
    # Remove the version byte (first character, usually '0')
    version_byte = blueprint_string[0]
    encoded_data = blueprint_string[1:]
    
    # Decode from base64
    compressed_data = base64.b64decode(encoded_data)
    
    # Decompress with zlib
    json_string = zlib.decompress(compressed_data).decode('utf-8')
    
    # Parse JSON
    blueprint_data = json.loads(json_string)
    
    return blueprint_data, version_byte


def encode_blueprint(blueprint_data, version_byte='0'):
    """
    Encodes a blueprint dictionary back into a Factorio blueprint string.
    
    Args:
        blueprint_data: The blueprint data as a Python dictionary
        version_byte: The version byte to use (default '0')
        
    Returns:
        str: The encoded blueprint string
    """
    # Convert to JSON string
    json_string = json.dumps(blueprint_data)
    
    # Compress with zlib
    compressed = zlib.compress(json_string.encode('utf-8'))
    
    # Encode to base64
    encoded = base64.b64encode(compressed).decode('utf-8')
    
    # Add version byte
    blueprint_string = version_byte + encoded
    
    return blueprint_string


def print_blueprint_summary(blueprint_data):
    """
    Prints a summary of what's in the blueprint.
    """
    print("\n" + "="*60)
    print("BLUEPRINT SUMMARY")
    print("="*60)
    
    if 'blueprint' in blueprint_data:
        bp = blueprint_data['blueprint']
        
        # Print label if it exists
        if 'label' in bp:
            print(f"Label: {bp['label']}")
        
        # Print entities
        if 'entities' in bp:
            print(f"\nEntities: {len(bp['entities'])}")
            
            # Count entity types
            entity_types = {}
            for entity in bp['entities']:
                name = entity.get('name', 'unknown')
                entity_types[name] = entity_types.get(name, 0) + 1
            
            print("\nEntity breakdown:")
            for entity_type, count in sorted(entity_types.items()):
                print(f"  - {entity_type}: {count}")
        
        # Print tiles if they exist
        if 'tiles' in bp:
            print(f"\nTiles: {len(bp['tiles'])}")
        
        # Print version
        if 'version' in bp:
            print(f"\nVersion: {bp['version']}")
    
    elif 'blueprint_book' in blueprint_data:
        book = blueprint_data['blueprint_book']
        print("Type: Blueprint Book")
        if 'label' in book:
            print(f"Label: {book['label']}")
        if 'blueprints' in book:
            print(f"Contains {len(book['blueprints'])} blueprints")
    
    print("="*60 + "\n")


def save_to_file(data, filename):
    """
    Saves the blueprint data to a JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Blueprint data saved to: {filename}")


def load_from_file(filename):
    """
    Loads blueprint data from a JSON file.
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    print(f"Blueprint data loaded from: {filename}")
    return data


def main():
    print("Factorio Blueprint Decoder/Encoder")
    print("="*60)
    
    if len(sys.argv) > 1:
        # If argument provided, treat it as blueprint string or filename
        arg = sys.argv[1]
        
        if arg.endswith('.json'):
            # Load from file and encode
            print(f"Loading from file: {arg}")
            blueprint_data = load_from_file(arg)
            blueprint_string = encode_blueprint(blueprint_data)
            print("\nEncoded Blueprint String:")
            print("-"*60)
            print(blueprint_string)
            print("-"*60)
        else:
            # Decode blueprint string
            print("Decoding blueprint string...")
            blueprint_data, version_byte = decode_blueprint(arg)
            
            print_blueprint_summary(blueprint_data)
            
            # Pretty print the JSON
            print("Full Blueprint Data (JSON):")
            print("-"*60)
            print(json.dumps(blueprint_data, indent=2))
            print("-"*60)
            
            # Offer to save
            filename = "blueprint_decoded.json"
            save_to_file(blueprint_data, filename)
            print(f"\nYou can now edit '{filename}' and run:")
            print(f"  python3 {sys.argv[0]} {filename}")
            print("to re-encode it back to a blueprint string.")
    else:
        # Interactive mode
        print("\nUsage:")
        print(f"  Decode: python3 {sys.argv[0]} <blueprint_string>")
        print(f"  Encode: python3 {sys.argv[0]} <blueprint_file.json>")
        print("\nExample blueprint string:")
        example = "0eJyVUdtKxEAM/ZVlnl3Yrq6rPizob4gM0zargc6FTKZYSv/dTFrQBxF8muSc5OQkM5t2KJAIA5un3WywiyFL9DqbjO/BDYrylEACgwze3OxMcF7zHjrsgfZd9C0Gx5HMIjSGHj6Fb5Y3ySAwMsKmqtlkQ/EtUK35W07YFLP0x6BOquxBwKm+dVaPBN1GV0L8M8XBtvDhRoykXZuwFbJXrazwFSmz/WXPEYmLYD+8rVX7Z12wHomdnmyd6ZMj9SuVl9oWC6fyT+2XTTtNYrQEtleK3mIQIam6uiHDsuhJ9R+k8fvvBByB8nqH40Nzd348nk/Nqbm9PyzLF/gIndQ="
        print(f"\n  python3 {sys.argv[0]} '{example}'")


if __name__ == "__main__":
    main()