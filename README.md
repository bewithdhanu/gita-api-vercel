# Bhagavad Gita API

A FastAPI-based REST API service that provides Bhagavad Gita verses in multiple languages (currently Telugu and Odia).

## Features

- Get list of all chapters with their names and verse counts
- Get all verses from a specific chapter
- Get a specific verse by chapter and verse number
- Get a verse by its serial number (1-700)
- Supports multiple languages (Telugu and Odia)

## API Endpoints

### 1. List All Chapters

```http
GET /{language}/chapters
```

Lists all chapters with their names and verse counts.

**Parameters:**
- `language`: Language code (`tel` for Telugu, `odi` for Odia)

**Response:**
```json
[
  {
    "chapter_no": 1,
    "chapter_name": "అర్జున విషాద యోగము",
    "verses_count": 47
  },
  ...
]
```

### 2. Get All Verses in a Chapter

```http
GET /{language}/chapter/{chapter_no}/verses
```

Returns all verses from a specific chapter.

**Parameters:**
- `language`: Language code (`tel` for Telugu, `odi` for Odia)
- `chapter_no`: Chapter number (1-18)

**Response:**
```json
[
  {
    "chapter_no": 1,
    "verse_no": 1,
    "language": "telugu",
    "verse": "...",
    "audio_link": "..."
  },
  ...
]
```

### 3. Get Specific Verse

```http
GET /{language}/verse/{chapter_no}/{verse_no}
```

Returns a specific verse by chapter and verse number.

**Parameters:**
- `language`: Language code (`tel` for Telugu, `odi` for Odia)
- `chapter_no`: Chapter number (1-18)
- `verse_no`: Verse number within the chapter

**Response:**
```json
{
  "chapter_no": 1,
  "verse_no": 1,
  "language": "telugu",
  "chapter_name": "అర్జున విషాద యోగము",
  "verse": "...",
  "transliteration": "...",
  "synonyms": "...",
  "audio_link": "...",
  "translation": "...",
  "purport": "..."
}
```

### 4. Get Verse by Serial Number

```http
GET /{language}/verse/{verse_no_serial}
```

Returns a verse by its serial number (1-700).

**Parameters:**
- `language`: Language code (`tel` for Telugu, `odi` for Odia)
- `verse_no_serial`: Serial number of the verse (1-700)

**Response:**
Same as the specific verse endpoint.

## Error Responses

The API returns appropriate error messages for invalid requests:

```json
{
  "error": "Error type",
  "message": "Detailed error message"
}
```

Common errors:
- Invalid chapter number (must be 1-18)
- Invalid verse number
- Unsupported language
- Resource not found

## Chapter Information

The Bhagavad Gita consists of 18 chapters with the following verse counts:
- Chapter 1: 47 verses
- Chapter 2: 72 verses
- Chapter 3: 43 verses
- Chapter 4: 42 verses
- Chapter 5: 29 verses
- Chapter 6: 47 verses
- Chapter 7: 30 verses
- Chapter 8: 28 verses
- Chapter 9: 34 verses
- Chapter 10: 42 verses
- Chapter 11: 55 verses
- Chapter 12: 20 verses
- Chapter 13: 35 verses
- Chapter 14: 27 verses
- Chapter 15: 20 verses
- Chapter 16: 24 verses
- Chapter 17: 28 verses
- Chapter 18: 78 verses

Total: 700 verses

## Development

### Requirements
- Python 3.6+
- FastAPI
- Uvicorn
- Other dependencies listed in requirements.txt

### Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Server
```bash
python main.py
```
The server will start at `http://localhost:8000`

## License

This project is licensed under the terms of the LICENSE file included in the repository. 

