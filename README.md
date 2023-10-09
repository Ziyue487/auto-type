# Auto-type
The program simulates human input by automatically typing the text from the clipboard, avoid pasting large blocks. It is targeted to counter detections such as [_Draftback_](https://chrome.google.com/webstore/detail/draftback/nnajoiemfpldioamchanognpjmocgkbg).
## Installation and running
Make sure the required dependencies are met and follow the instructions:<br>
* [python](dependencies.md)
* [pip](dependencies.md)
### Installation on MacOS
1. Install the dependencies
```python
pip3 install pynput paperclip
pip3 install pygetwindow
```
2. Open terminal at folder `AutoType` and run `python3 local.py` 
3. To start auto-typing, press `ctrl + shift + g`
4. To end the program, press `ctrl + c` in the terminal
