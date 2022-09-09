while True:
    text = input("Write something, or stop to quit: ")
    if text == "stop":
        break
    print(f'{text} has length: {len(text)}')
