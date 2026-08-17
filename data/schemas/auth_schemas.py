LOGIN_SUCCESS_SCHEMA = {
    "type": "object",
    "properties": {
        "access_token": {"type": "string"},
        "token_type": {"type": "string"},
        "expires_in": {"type": "integer"}
    },
    # Ensure all three fields are always present
    "required": ["access_token", "token_type", "expires_in"],
    # Strictly fail if unexpected fields (like debug data) appear in production
    "additionalProperties": False  
}

LOGIN_ERROR_SCHEMA = {
    "type": "object",
    # Depending on the framework, validation errors might have different shapes.
    # We will start loose and tighten it once we see the exact error shape.
    "properties": {
        "error": {"type": "string"},
        "message": {"type": "string"}
    },
    "anyOf": [
        {"required": ["error"]},
        {"required": ["message"]}
    ]
}