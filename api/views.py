from rest_framework.views import APIView
from rest_framework.response import Response


class Hello(APIView):
    def get(self, request, format=None):
        num = request.query_params.get('num')
        res_dict = {
            'greet': '' 
        }
        if num:
            count = int(num)
            res_dict['greet_list'] = []
            for i in range(count):
                res_dict['greet'] += 'Hello World!'
                res_dict['greet_list'] += ['Hello World!']
            res_dict['num'] = count
        else:
            res_dict['greet'] = 'Hello World!'        
        return Response(res_dict)