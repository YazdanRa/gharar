# Gharar Python Client

This is a python adaptor for interact with 
[Gharar](https://http://gharar.ir) service.

# Installation

You can easily install the package via command line below:

```commandline
pip install pygharar
```

# Usage

```python
from pygharar import Gharar

my_gharar = Gharar(
    service_url="https://gharar.ir/",
    authorization_token="PUT YOUR OWN TOKEN HERE", 
    max_retry=3
)
```
