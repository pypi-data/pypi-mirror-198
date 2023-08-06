<h1 align="center">📻 Emitter</h1>

This library provides the emitter data type.
An emitter calls listening handlers whenever an event is emitted. This allows the separation of sourcing an event and reacting to it.

## 💻 Installation

This package is [published to PyPI as `babichjacob-emitter`](https://pypi.org/project/babichjacob-emitter/).

## 🛠 Usage

```py
from emitter import emittable

my_emitter = emittable()
my_emitter.listen(lambda event: print(f"Received the event {event}"))
my_emitter.emit(23) # "Received the event 23" gets printed
```

## 😵 Help! I have a question

Create an issue and I'll try to help.

## 😡 Fix! There is something that needs improvement

Create an issue or pull request and I'll try to fix.

## 📄 License

MIT

## 🙏 Attribution

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
