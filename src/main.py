# Resolve the problem!!
import re

def run():
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        listMsg = re.findall('[a-z]', content)
        secretMessage = ''

        for char in listMsg:
            secretMessage += char

        print(secretMessage)


if __name__ == '__main__':
    run()
