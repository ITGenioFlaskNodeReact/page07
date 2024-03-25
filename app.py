from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
history = {}


@app.route('/')
def index():
    global history, step
    history = {}
    step = 0
    return render_template('index.html', step=step)


@app.route("/<int:step>:<int:choice>")
def quest(step, choice):
    global history
    message = ''
    if step == 0:
        message = 'There are 2 roads.On the left - you will find gold, ont the right - you will lose your horse.' \
                  'Go to the left?'
    elif step == 1:
        if choice == 1:
            message = "You have found a gold coin.It looks like someone has ben here before you.Lets go after him?"
        elif choice == 0:
            message = "Ok, you dont have a horse now.But there is one eating grass, so you are now with a horse." \
                      "Start over?"
        history['1'] = choice
    elif step == 2:
        if history['1'] == 0:
            if choice == 1:
                return redirect(url_for('index'))
            elif choice == 0:
                return redirect(url_for('quest', step=1, choice=0))
        elif history['1'] == 1 and choice == 1:
            message = '3 Days and 3 nights you followed his path.In the morning, dying from thirst,' \
                      ' you came to a swamp where Baba-Yaga lived.She gave you water, food and gave you a ' \
                      'wife.Last, but not least she shared a part of the gold with you and now you are a part of ' \
                      'the story mafia.Start over?'
        elif history['1'] == 1 and choice == 0:
            message = "Going away with a coin in your hand you see a village of gnomes." \
                      "when they saw that you have a coin they thought that you were the one who stole the treasure." \
                      "Now you have to work in the gold mines for the gnomes, but you will be living in gold," \
                      " literally.Start over?"
        history['2'] = choice
    elif step == 3:
        if choice == 0 and history['2'] == 0:
            return redirect(url_for('quest', step=2, choice=0))
        elif choice == 0 and history['2'] == 1:
            return redirect(url_for('quest', step=2, choice=1))
        else:
            return redirect(url_for('index'))
    step += 1
    return render_template('quest.html',
                           message=message,
                           step=step)


if __name__ == "__main__":
    app.run(host='localhost', port=5000)
