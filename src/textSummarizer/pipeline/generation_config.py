"""
Generation configuration for Pegasus model
Defines the parameters for text summarization
"""

GENERATION_CONFIG = {
    "max_length": 128,
    "min_length": 32,
    "num_beams": 8,
    "length_penalty": 0.8,
    "forced_eos_token_id": 1
}
