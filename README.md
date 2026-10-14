#  Secret Language Encoder & Decoder in Python

A clean, beginner-friendly yet professional command-line interface (CLI) program written in Python that encodes and decodes secret messages using custom string manipulation and randomization rules.

##  Features
- **Encoding (`1`):** 
  - Words with 3 or more characters have their first letter moved to the end, and 3 random lowercase characters are prepended and appended.
  - Words with fewer than 3 characters are simply reversed.
- **Decoding (`0`):** 
  - Safely reverses the encoding process to retrieve the original message.
- **Sentence Support:** Handles entire sentences smoothly by splitting them into individual words.
- **Clean Python Practices:** Utilizes built-in modules like `string` and `random`, along with clean variable naming and input sanitation (`.strip()`).

##  How to Run the Code
1. Make sure you have Python installed on your system.
2. Clone this repository or download the `main.py` file.
3. Run the script using your terminal or VS Code:
   ```bash
   python main.py
