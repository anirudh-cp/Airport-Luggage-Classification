# Airport Luggage Classification

Classify objects as check-in baggage, carry on baggage or not permitted.

## Demo:
- Generate model from Notebook.
- Refactor and place `assets`, `variables`, `fingerprint.pb` and `saved_model.pb` within the folder `exported_model/saved_model/1/`
- Run `createContainer.sh`.
- `python ./website/wsgi.py`.
- Upload an image. Samples are in `Pics`.
- Get output.