from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/guess", methods=['POST', 'GET'])
def guess():

   if request.method == 'GET':
       return render_template('guess_number.html', min = '0', max = '1000', guess = '500')
   else:
       min_num = int(request.form['min']) # min value from users browses
       max_num = int(request.form['max']) # max value from users browser
       guess = int(((max_num - min_num) / 2) + min_num) # this is last computers hit
       usr_ans = request.form['answer'] # users answer for computers hit
       if usr_ans == 'win':
           return render_template('guess_number.html', guess='I won!!!')
       if usr_ans == 'big':
           max_num = guess
       if usr_ans == 'small':
           if guess == 999:  # int(5 / 2) == 2. this fix is for users who picked 1000
               guess = 1000
               min_num = guess
               return render_template('guess_number.html', min = str(min_num), max = str(max_num), guess = str(guess))
           min_num  = guess
       guess = int(((max_num - min_num) / 2) + min_num) # this is next computers hit
       return render_template('guess_number.html', min = str(min_num), max = str(max_num), guess = str(guess))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
