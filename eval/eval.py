from flask import request

def main():
    num_1 = int(request.args.get('num_1'))
    num_2 = int(request.args.get('num_2'))
    operator = request.args.get('operator')

    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
        
    return "%s %s %s = %s" % (num_1, operator, num_2, result)