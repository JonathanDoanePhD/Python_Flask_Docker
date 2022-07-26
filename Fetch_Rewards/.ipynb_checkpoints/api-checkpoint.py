{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "a576b075-eafe-457e-af27-cf2cefb0e316",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__' (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on all addresses (0.0.0.0)\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      " * Running on http://127.0.0.1:5000\n",
      " * Running on http://192.168.1.116:5000 (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template,jsonify\n",
    "app = Flask(__name__)\n",
    "def do_something(text1,text2):\n",
    "   text1 = text1.upper()\n",
    "   text2 = text2.upper()\n",
    "   combine = text1 + text2\n",
    "   return combine\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('home.html')\n",
    "@app.route('/join', methods=['GET','POST'])\n",
    "def my_form_post():\n",
    "    text1 = request.form['text1']\n",
    "    word = request.args.get('text1')\n",
    "    text2 = request.form['text2']\n",
    "    combine = do_something(text1,text2)\n",
    "    result = {\n",
    "        \"output\": combine\n",
    "    }\n",
    "    result = {str(key): value for key, value in result.items()}\n",
    "    return jsonify(result=result)\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=False, host='0.0.0.0', port=5000)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
