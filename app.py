from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)

@app.route('/test')
def test_route():
    return "This is a test route."


@app.route('/home')
def get_landing():
    # print("Request received for /home")
    return render_template('base.html')
    
@app.route('/story')
def form():
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural_noun = request.args['plural-noun']

    my_story = Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
           large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )

    generated_story = my_story.generate({
        "place": place,
        "noun": noun,
        "verb": verb,
        "adjective": adjective,
        "plural_noun": plural_noun
    })

    return render_template('story.html', generated_story=generated_story)
    # return render_template('story.html', place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)

#     # noun = request.args['noun']
#     # adjective = request.args['adjective']
#     return render_template('base.html', place = place)