def convert_to_bytes(input_string, encoding):
    try:
        encoded_bytes = input_string.encode(encoding)
        return encoded_bytes
    except Exception as e:
        print("Error:", e)
        return None

def main():
    try:
        input_string = "Python Exercises!"
        
        encodings = ["utf-8", "utf-16", "ascii"]
        for encoding in encodings:
            encoded_bytes = convert_to_bytes(input_string, encoding)
            if encoded_bytes is not None:
                print(f"Encoding: {encoding.upper()}")
                print("Original String:", input_string)
                print("Encoded Bytes:", encoded_bytes)
                print("Decoded String:", encoded_bytes.decode(encoding))
                print("=" * 40)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
