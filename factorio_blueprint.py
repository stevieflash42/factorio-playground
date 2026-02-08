#!/usr/bin/env python3
"""
Simple script to generate a Factorio blueprint for a decider combinator.
The blueprint can be imported directly into Factorio.
"""

import json
import zlib
import base64


def create_decider_combinator_blueprint():
    """
    Creates a blueprint containing a single decider combinator.
    Default settings: If signal-A > 0 then output signal-B = 1
    """
    blueprint = {
        "blueprint": {
            "icons": [
            {
                "signal": {
                "name": "constant-combinator"
                },
                "index": 1
            }
            ],
            "entities": [
            {
                "entity_number": 1,
                "name": "constant-combinator",
                "position": {
                "x": 989.5,
                "y": 455.5
                },
                "direction": 12,
                "control_behavior": {
                "sections": {
                    "sections": [
                    {
                        "index": 1,
                            "filters": [
                            {
                                "index": 1,
                                "name": "bob-ruby-4",
                                "quality": "normal",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 2,
                                "name": "bob-sapphire-4",
                                "quality": "normal",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 3,
                                "name": "bob-emerald-4",
                                "quality": "normal",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 4,
                                "name": "bob-amethyst-4",
                                "quality": "normal",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 5,
                                "name": "bob-topaz-4",
                                "quality": "normal",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 6,
                                "name": "bob-diamond-4",
                                "quality": "normal",
                                "comparator": "=",
                                "count": 1
                            },


                            {
                                "index": 7,
                                "name": "bob-ruby-4",
                                "quality": "uncommon",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 8,
                                "name": "bob-sapphire-4",
                                "quality": "uncommon",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 9,
                                "name": "bob-emerald-4",
                                "quality": "uncommon",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 10,
                                "name": "bob-amethyst-4",
                                "quality": "uncommon",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 11,
                                "name": "bob-topaz-4",
                                "quality": "uncommon",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 12,
                                "name": "bob-diamond-4",
                                "quality": "uncommon",
                                "comparator": "=",
                                "count": 1
                            },


                            {
                                "index": 13,
                                "name": "bob-ruby-4",
                                "quality": "rare",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 14,
                                "name": "bob-sapphire-4",
                                "quality": "rare",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 15,
                                "name": "bob-emerald-4",
                                "quality": "rare",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 16,
                                "name": "bob-amethyst-4",
                                "quality": "rare",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 17,
                                "name": "bob-topaz-4",
                                "quality": "rare",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 18,
                                "name": "bob-diamond-4",
                                "quality": "rare",
                                "comparator": "=",
                                "count": 1
                            },

                            {
                                "index": 19,
                                "name": "bob-ruby-4",
                                "quality": "epic",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 20,
                                "name": "bob-sapphire-4",
                                "quality": "epic",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 21,
                                "name": "bob-emerald-4",
                                "quality": "epic",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 22,
                                "name": "bob-amethyst-4",
                                "quality": "epic",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 23,
                                "name": "bob-topaz-4",
                                "quality": "epic",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 24,
                                "name": "bob-diamond-4",
                                "quality": "epic",
                                "comparator": "=",
                                "count": 1
                            },

                            {
                                "index": 25,
                                "name": "bob-ruby-4",
                                "quality": "legendary",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 26,
                                "name": "bob-sapphire-4",
                                "quality": "legendary",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 27,
                                "name": "bob-emerald-4",
                                "quality": "legendary",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 28,
                                "name": "bob-amethyst-4",
                                "quality": "legendary",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 29,
                                "name": "bob-topaz-4",
                                "quality": "legendary",
                                "comparator": "=",
                                "count": 1
                            },
                            {
                                "index": 30,
                                "name": "bob-diamond-4",
                                "quality": "legendary",
                                "comparator": "=",
                                "count": 1
                            }
                            ]
                        }
                    ]
                }
                }
            }
            ],
            "item": "blueprint",
            "version": 562949958205441
        }
    }
    
    # Convert to JSON string
    json_string = json.dumps(blueprint)
    
    # Compress with zlib
    compressed = zlib.compress(json_string.encode('utf-8'))
    
    # Encode to base64
    encoded = base64.b64encode(compressed).decode('utf-8')
    
    # Add version byte (0 for blueprints)
    blueprint_string = "0" + encoded
    
    return blueprint_string


def main():
    blueprint_string = create_decider_combinator_blueprint()
    
    print("Factorio Decider Combinator Blueprint:")
    print("=" * 60)
    print(blueprint_string)
    print("=" * 60)
    print("\nCopy the string above and paste it into Factorio to import the blueprint.")
    print("\nDefault settings:")
    print("  - Input: signal-A")
    print("  - Condition: > 0")
    print("  - Output: signal-B = 1")


if __name__ == "__main__":
    main()