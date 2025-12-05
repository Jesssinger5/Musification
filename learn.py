from music21 import *
environment.set('musicxmlPath','/Applications/MuseScore 4.app')
from flask import Flask, Response
from music21 import stream, note, corpus


s = stream.Stream()
s.append(meter.TimeSignature('4/4'))
one_sharp_ks = key.KeySignature(1)
s.append(note.Note('B4'))
s.append(note.Note('A4'))
s.append(note.Note('G4', duration=duration.Duration(2.0)))
s.append(note.Note('B4'))
s.append(note.Note('A4'))
s.append(note.Note('G4', duration=duration.Duration(2.0)))
s.append(note.Note('G4', type="eighth"))
s.append(note.Note('G4', type="eighth"))
s.append(note.Note('G4', type="eighth"))
s.append(note.Note('G4', type="eighth"))
s.append(note.Note('A4', type="eighth"))
s.append(note.Note('A4', type="eighth"))
s.append(note.Note('A4', type="eighth"))
s.append(note.Note('A4', type="eighth"))
s.append(note.Note('B4'))
s.append(note.Note('A4'))
s.append(note.Note('G4', duration=duration.Duration(2.0)))

s.show()

from music21 import stream, note, vexflow


# 2. Instantiate the VexflowPickler
vfp = vexflow.toMusic21j.VexflowPickler()

# 3. Convert the music21 Stream to a music21j HTML string
# This method handles both the conversion to JSON and embedding it in a complete HTML document.
html_string = vfp.getHTML(s, title='Example from Python')

# 4. Save the HTML string to a file
# You can save this file and open it in a web browser to see the result.
with open('my_vexflow_output.html', 'w') as f:
    f.write(html_string)

print('HTML page "my_vexflow_output.html" has been created.')
