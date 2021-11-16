from django.shortcuts import render


     

def reviewers(request):
    return render(request, 'reviewers.html')

def journalPolicies(request):
    return render(request, 'journal_Policies.html')



def editors(request):
    return render(request, 'Editors.html')

def privacyPolicy(request):
    return render(request, 'privacyPolicy.html')
