# Art works
Supports viewing art works.

## Get list

**Request**:

`GET` `/art-works/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
type       | string | No       | One of: <ul><li>"bas-relief"</li>, <li>"sculpture"</li>, <li>"pictures"</li></ul>

**Response**:

```json
Content-Type application/json
200 OK

{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "image": "http://127.0.0.1:8000/media/54b35949d5502ca6be86403c0992e324.jpeg",
      "title": "My best sculpture",
      "description": "sad",
      "type": "sculpture",
      "show": true
    }
  ]
}
```

## Retrieve art work

**Request**:

`GET` `/art-work/:id`

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 1,
  "image": "http://127.0.0.1:8000/media/54b35949d5502ca6be86403c0992e324.jpeg",
  "title": "My best sculpture",
  "description": "sad",
  "type": "sculpture",
  "show": true
}
```
