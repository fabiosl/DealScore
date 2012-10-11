# Create your views here.
from django.shortcuts import render_to_response
from dealapp.models import *

def home(request):
        deals = Deal.objects.all()
        
        category_dict = {}
        for deal in deals:
            for category in deal.categories.all():
                if (category_dict.get(category) == None):
                    category_dict[(category)] = []
                category_dict[category].append(deal) 
        print category_dict;
        return render_to_response('home.html', {"categories_dictionary" : category_dict})


def vote(request, deal_code):
        deal = Deal.objects.get(code=deal_code)
        if(request.GET.get('isDeal', False)):
            deal.positive_votes+=1;
        else:
            deal.negative_votes+=1;
        print "voted" + str(request.GET.get('isDeal', False)) + " on deal " + deal_code;     
        deal.save() ;
        return render_to_response('voted.html', {})

def show_deal(request, deal_code):
        deal = Deal.objects.get(code=deal_code)
        return render_to_response('show_deal.html',{'deal':deal})