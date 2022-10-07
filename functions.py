{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 1 2 3 5 8 13 21 34 "
     ]
    }
   ],
   "source": [
    "def fibonacci(limit = 10):\n",
    "    a, b = 0, 1\n",
    "    for i in range(0, limit):\n",
    "        print(f'{a}', end=' ')\n",
    "        a, b = b, a+b\n",
    "\n",
    "fibonacci(10)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.7 64-bit (microsoft store)",
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
   "version": "3.10.7"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "b91a4ebecf888e385640dc72091d7799c60f531adf494a45587fe0bb62283323"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
