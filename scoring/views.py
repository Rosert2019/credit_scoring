from django.shortcuts import render
from .forms import single_form
from .models import Age, Amount, Duration, Rate
from .user_functions import handle_uploaded_file, get_score, switch_note, grade_score
import pandas as pd
from django.http import HttpResponse
from django.conf import settings
import os
from bokeh.plotting import figure
from bokeh.embed import components


# Create your views here.
 
def single_view(request):
	#if form is submitted
	if request.method == 'POST':
		#will handle the request later
		form = single_form(request.POST)
 
		#checking the form is valid or not 
        #if valid rendering new view with values
		#the form values contains in cleaned_data dictionary
		if form.is_valid(): return render(request, 'single_result.html', {'single_score': grade_score([form.cleaned_data['amount'], form.cleaned_data['age'], form.cleaned_data['duration'], form.cleaned_data['rate']])} )
 
	else:
		#creating a new form
		form = single_form()
 
	#returning form 
	return render(request, 'single_form.html', {'form':form})

#-------------------------------------------------------------------------------------------------------

def file_view(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        #we made an orm request to get the content of Amount,.. and we transform in pandas dataframe
        amount = Amount.objects.all().values('modalities', 'grades')
        amount = pd.DataFrame.from_records(amount)
            
        age = Age.objects.all().values('modalities', 'grades')
        age = pd.DataFrame.from_records(age)
            
        duration = Duration.objects.all().values('modalities', 'grades')
        duration = pd.DataFrame.from_records(duration)
            
        rate = Rate.objects.all().values('modalities', 'grades')
        rate = pd.DataFrame.from_records(rate)
            
        data_to_score = handle_uploaded_file(myfile)
        df = get_score(data_to_score,[age, amount, duration, rate]) #for score of the whole file
        numb_lines = df.shape[0] #getting the number of line
        #frequency of each score in the file, columns renamed and sort by scores column
        numb_scores = df['score'].value_counts().rename_axis('scores').reset_index(name='counts').sort_values(by=['scores'])
        numb_scores = pd.DataFrame(numb_scores)
        numb_scores_html = pd.DataFrame(numb_scores).to_html()#transforms pandas dataframe to html table

    
        #the file scored is given the name score_file that we saved in media directory.
        # Scored_file will be deleted there is already in the media directory
        #we convert it to a pdf before storing it
        uploaded_file_url = settings.MEDIA_ROOT[0]+ '/scored_file.csv'
        os.remove(uploaded_file_url) if os.path.exists(uploaded_file_url) else None
        df.to_csv(uploaded_file_url, index = False)
        
        #create a plot using bokeh
        
        fig = figure(x_range = numb_scores['scores'].to_list(), plot_width=400, plot_height=200, title = "Analysis of file quality")
        fig.vbar(x = numb_scores['scores'].to_list(), top = numb_scores['counts'].to_list(), width = 0.5)
        script, div = components(fig)

        #we saved all in dictionnary 
        all_result = {'uploaded_file_url': uploaded_file_url, 'numb_lines':numb_lines, 'numb_scores_html':numb_scores_html,'script': script, 'div': div}


        return render(request, 'file_form.html',{'final':all_result})

       
  

    return render(request, 'file_upload.html')

def home(request):
    return render(request, 'home.html')   

