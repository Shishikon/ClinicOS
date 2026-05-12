
import qrcode
import io
import base64
from django.contrib import messages

from django.shortcuts import render

from clinicos.forms import BookAppointmentForm, QrCodeForm


def index(request):
    form = BookAppointmentForm
    context = {
        'form': form,
    }
    return render(request, 'app/index.html', context)


def book_app(request):
    if request.method == 'POST':

        qrcode_app_form = QrCodeForm(data=request.POST)
        book_app_form = BookAppointmentForm(data=request.POST)

        if qrcode_app_form.is_valid() and book_app_form.is_valid():
            qrcode_app_form.save()
            book_app_form.save()
            messages.success(request, 'Your appointment was booked successfully !!!')

        data = request.POST

        name = data['name']
        email = data['email']
        phone = data['phone']
        date = data['date']
        picktime = data['picktime']
        people = data['people']
        type_of = data['type_of']
        message = data['message']

        context_data = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Date: {date}
        Time: {picktime}
        People: {people}
        Type of : {type_of}
        Message: {message}
        """


        qr = qrcode.make(context_data)
        buffer = io.BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)
        qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return render(request, 'app/qr_code_detail.html', context={
            'qr_code_base64': qr_base64,
            'name': name,
            'email': email,
            'phone': phone,
            'date': date,
            'picktime': picktime,
            'people': people,
            'type_of': type_of,
            'message': message,
        })

    return render(request, 'app/components/sub_components/__book_table_form.html')
