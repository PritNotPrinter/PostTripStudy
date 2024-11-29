# To run this program

Back-end:
Run main.py as a python file (Testing environment for ORC and Claude AI, no complete implementation yet)

Chrome Extension:

- Go to chrome://extensions/
- Turn on developer mode
- Load unpacked
- Choose the file ./jacob-ext
- Try out the extension!

## Inspiration

- The struggle of catching up after missing days of school as a student

## What it does

- Summarises and compiles lessons and tasks based on priority (weight & due date) to ensure students get back on their feet after absences

## How we built it

- Utilized the Anthropic API with Claude AI for the OCR capabilities
- Created a Chrome Extension to track D2L input

## Challenges we Faced

- Pre-hackathon setup issues
- Time allocation

## What we Learned

- The framework behind many OCR and AI functions, and how to create a chrome extension.
- Along with this, we've learned how to adapt in situations where we run into dead ends.

## What's next for Jacob's Notes

- Implement scanning methods for Slideshows to Text, utilizing the Claude AI API
- Code our own OCR methods independently
- Add functionality to our Chrome Extension that reads from classroom sites such as D2L and Google Classroom
