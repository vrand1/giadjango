from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Partner, Sale, PartnerType
from django.db.models import Sum, Count


# Create your views here.

def index(request):
    partners = Partner.objects.all()
    return render(request, 'partner/index.html', {'partners': partners, 'title': 'Список партнеров'})


def PartnerHistory(request, partner_id):
    sales = Sale.objects.filter(PartnerID=partner_id)
    return render(request, 'partner/history.html', {'sales': sales})


def add_partner(request):
    if request.method == 'POST':

        partner_type_id = request.POST.get('partner_type')
        partner_type = PartnerType.objects.get(ID=partner_type_id)
        Name = request.POST.get('partner_name')
        Director = request.POST.get('director')
        Email = request.POST.get('email')
        PhoneNumber = request.POST.get('phone_number')
        LegalAddress = request.POST.get('legal_address')
        Rating = request.POST.get('partner_rating')

        # Создаем и сохраняем нового партнера
        Partner.objects.create(
            Partner_type=partner_type,
            Name=Name,
            Director=Director,
            Email=Email,
            PhoneNumber=PhoneNumber,
            LegalAddress=LegalAddress,
            Rating=Rating,
        )
        return redirect('/')  # Перенаправляем после успешного сохранения

    return render(request, 'partner/form.html')

def delete_partner(request, partner_id):
    if request.method == 'POST':
        partner = get_object_or_404(Partner, ID=partner_id)
        partner.delete()
    return redirect('/')


def update_partner(request, partner_id):
    partner = get_object_or_404(Partner, ID=partner_id)
    partner_types = PartnerType.objects.all()

    return render(request, 'partner/update.html', {
        'partner': partner,
        'partner_types': partner_types
    })

def update_partner_save(request, partner_id):
    if request.method == 'POST':
        partner = get_object_or_404(Partner, ID=partner_id)
        partner_type = get_object_or_404(PartnerType, ID=request.POST.get('partner_type'))

        partner.Partner_type = partner_type
        partner.Name = request.POST.get('partner_name')
        partner.Director = request.POST.get('director')
        partner.Email = request.POST.get('email')
        partner.PhoneNumber = request.POST.get('phone_number')
        partner.LegalAddress = request.POST.get('legal_address')
        partner.Rating = request.POST.get('partner_rating')
        partner.save()

        return redirect('/')

    return redirect('update', partner_id=partner_id)