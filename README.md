# Hydra

Hydra is the public API for Janet.

## Making requests
Here is an example of a request to the `/health` route.
```bash
$ curl "janet.euii.xyz/api/health"
```

```json
{"status": "OK"}
```

## Having a conversation with  Janet
### cURL example
You can use the `/chat` route to have a conversation with Janet.
You need to include some JSON data in the body of the request. Here is an
example:
```json
{"message": "Hello"}
```
Here's an example of a POST request being made to `/chat`
```bash
$ curl --header "Content-Type: application/json" \
  --request POST
  --data '{"message": "Hello"}' \
  http://janet.euii.xyz/api/chat
```
The response you'd receive could look like this:
```json
{
    "recipient_id": "default",
    "text": "Hi! I'm Janet."
}
```

### Python example
```python
import requests

payload = {'message': 'What is the weather like today?'}
x = requests.post('http://janet.euii.xyz/api/chat', json=payload)

print(x.json())
```
Which would return
```json
{
    "recipient_id": "default",
    "text": "It is partly cloudy today, with an average temperature of 3.53°C,
    while the humidity is around 94.61%."
}
```
