import random
from typing import Optional

import strawberry


@strawberry.type
class Schema:
    id: Optional[str] = None
    snippet: str
    language: str
    extension: Optional[str] = None


def generate_random_schema() -> Schema:
    snippets = [
        """{
  "$id": "https://example.com/AddedItemToCart.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "AddedItemToCart",
  "type": "object",
  "properties": {
    "metadata": {
      "type": "object",
      "properties": {
        "correlationId": {
          "type": "string",
          "description": "The ID of the user"
        },
        "domain": {
          "type": "string",
          "description": "The domain of the event"
        },
        "service": {
          "type": "string",
          "description": "The name of the service that triggered the event"
        }
      },
      "required": ["correlationId", "domain"]
    },
    "data": {
      "type": "object",
      "properties": {
        "userId": {
          "type": "string",
          "description": "The ID of the user"
        },
        "itemId": {
          "type": "string",
          "description": "The ID of the shopping item"
        },
        "quantity": {
          "type": "number",
          "description": "How many items the user wants to add to their shopping cart",
          "minimum": 1,
          "maximum": 1000,
          "default": 1
        }
      }
    }
  }
}
""",
        """{
  "$id": "https://example.com/AddedItemToCart.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "AddedItemToCart",
  "type": "object",
  "properties": {
    "metadata": {
      "type": "object",
      "properties": {
        "correlationId": {
          "type": "string",
          "description": "The ID of the user"
        },
        "domain": {
          "type": "string",
          "description": "The domain of the event"
        },
        "service": {
          "type": "string",
          "description": "The name of the service that triggered the event"
        }
      },
      "required": ["correlationId", "domain"]
    },
    "data": {
      "type": "object",
      "properties": {
        "userId": {
          "type": "string",
          "description": "The ID of the user"
        },
        "itemId": {
          "type": "string",
          "description": "The ID of the shopping item"
        },
        "quantity": {
          "type": "number",
          "description": "How many items the user wants to add to their shopping cart",
          "minimum": 1,
          "maximum": 1000,
          "default": 1
        }
      }
    }
  }
}
""",
        """{
  "$id": "https://example.com/AddedItemToCart.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "AddedItemToCart",
  "type": "object",
  "properties": {
    "metadata": {
      "type": "object",
      "properties": {
        "correlationId": {
          "type": "string",
          "description": "The ID of the user"
        },
        "domain": {
          "type": "string",
          "description": "The domain of the event"
        },
        "service": {
          "type": "string",
          "description": "The name of the service that triggered the event"
        }
      },
      "required": ["correlationId", "domain"]
    },
    "data": {
      "type": "object",
      "properties": {
        "userId": {
          "type": "string",
          "description": "The ID of the user"
        },
        "itemId": {
          "type": "string",
          "description": "The ID of the shopping item"
        },
        "quantity": {
          "type": "number",
          "description": "How many items the user wants to add to their shopping cart",
          "minimum": 1,
          "maximum": 1000,
          "default": 1
        }
      }
    }
  }
}
""",
    ]  # Replace with your actual snippets
    languages = [
        "json",
        "json",
        "json",
    ]  # Replace with your actual languages
    extensions = [
        ".json",
        ".json",
        ".json",
    ]  # Replace with your actual extensions

    random_snippet = random.choice(snippets)
    random_language = random.choice(languages)
    random_extension = random.choice(extensions)

    return Schema(
        snippet=random_snippet, language=random_language, extension=random_extension
    )
