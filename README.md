# Auto Type
The program simulates human input by automatically typing the text from the clipboard, avoid pasting large blocks. It is targeted to counter detections such as [_Draftback_](https://chrome.google.com/webstore/detail/draftback/nnajoiemfpldioamchanognpjmocgkbg).
## Installation and running
Make sure the required dependencies are met and follow the instructions:<br>
* [python](dependencies.md)
* [pip](dependencies.md)

### Installation on Windows and MacOS
1. Install the dependencies
```python
pip install pyperclip
pip install pynput
```

### Run
1. Open terminal at folder `AutoType` and run `python type.py` 
2. To start auto-typing, press `ctrl + shift + g`
3. To end the program, press `ctrl + c` in the terminal
