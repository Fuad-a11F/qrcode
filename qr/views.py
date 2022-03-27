from rest_framework.response import Response
from rest_framework.views import APIView
import qrcode as code


class CodeView(APIView):
    def get(self, request):
        qr = code.QRCode(
            version=1,
            error_correction=code.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        print(self.request.query_params.get('location'))
        qr.add_data(self.request.query_params.get('location'))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        img.save('media/qwq1.jpg', 'JPEG')

        return Response({"code": 'https://qr-code-for-mobile.herokuapp.com/media/qwq1.jpg'})
