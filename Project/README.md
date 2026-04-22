# Universal Converter in Python

Welcome to the **Universal Converter**, a simple Python project that performs unit conversions directly in the terminal. It provides an interactive interface and supports Brazilian currency formatting. You can convert:

* Temperature: Celsius → Fahrenheit
* Speed: Km/h → Mph
* Currency: Brazilian Real (BRL) → US Dollar (USD)
* Time: Minutes → Hours

---

## Features

* Unit conversion with user input
* Loop for repeated conversions
* Currency formatting using `locale`
* Compatible with Windows, macOS, and Linux

---

## How to Run

**Requirements:** Python 3.13.5 installed
Optional: `requests` library (install with `pip install requests` if used in your code)

1. Clone the repository:

```bash
git clone https://github.com/DaviFeitosaBastos/Conversores-Universais.git
cd Conversores-Universais
```

2. Run the script:

```bash
python conversor.py
```

---

## Project Structure

```
Functions.py   # Functions for each operations
main.py    # Main script with all converters
README.md       # Project documentation
```

---

## Locale Configuration

The project uses the `locale` module to format Brazilian currency correctly:

* Linux/macOS: `pt_BR.UTF-8`
* Windows: `Portuguese_Brazil.1252`

---

## Exchange Rate

```
real / 5.4759
```

You can update the exchange rate manually if needed.

---

## Author

Davi Feitosa Bastos
